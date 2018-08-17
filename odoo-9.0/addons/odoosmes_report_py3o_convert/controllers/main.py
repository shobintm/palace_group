# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import json
import os
import mimetypes

from openerp.http import route, request

from openerp.addons.report_py3o_customize.controllers import main
from openerp.addons.web.controllers.main import (
    _serialize_exception,
    content_disposition
)
from openerp.tools import html_escape


class ReportController(main.ReportController):

    @route()
    def report_download(self, data, token):
        """This function is used by 'qwebactionmanager.js' in order to trigger
        the download of a py3o/controller report, and convert report from ods
        to xlsx with libreoffice

        :param data: a javascript array JSON.stringified containg report
        internal url ([0]) and type [1]
        :returns: Response with a filetoken cookie and an attachment header
        """
        response = super(ReportController, self).report_download(data, token)

        requestcontent = json.loads(data)
        url, type = requestcontent[0], requestcontent[1]
        if type != 'py3o':
            return super(ReportController, self).report_download(
                data,
                token
            )
        try:
            reportname = url.split('/report/py3o/')[1].split('?')[0]
            if '/' in reportname:
                reportname, docids = reportname.split('/')

            ir_action = request.env['ir.actions.report.xml']
            action_py3o_report = ir_action.get_from_report_name(
                reportname, "py3o").with_context(request.env.context)
            outputfile = action_py3o_report.py3o_filetype
            doutputfile = '.'+ outputfile
            tdoutfile = 'x.'  + outputfile
            if not action_py3o_report.py3o_filetype_template: 
                rftype = action_py3o_report.py3o_template_id.filetype
            else:
                rftype = action_py3o_report.py3o_filetype_template
            ftype = '.' + rftype

            with open(os.path.dirname(__file__) + '/' +
                      reportname + ftype, 'a+') as create_ods:
                create_ods.write(response.data)
            os.system(
                "unoconv -f "+outputfile+" '" + os.path.dirname(
                    __file__) + "/" + reportname + ftype +"'")
            with open(os.path.dirname(__file__) + '/' +
                      reportname + doutputfile , 'r+') as create_xlsx:
                res = create_xlsx.read()
            os.remove(
                os.path.dirname(__file__) + '/' + reportname + ftype
            )
            os.remove(
                os.path.dirname(__file__) + '/' + reportname + doutputfile
            )
            filename = action_py3o_report.gen_report_download_filename(
                docids, data)
            filename_without_type = filename.split('.')[0]

            content_type = mimetypes.guess_type(tdoutfile)[0]
            http_headers = [
                ('Content-Type',
                 content_type),
                ('Content-Length',
                 len(res)),
                ('Content-Disposition',
                 content_disposition(
                     filename_without_type +
                     doutputfile))]
            response = request.make_response(res, headers=http_headers)
            response.set_cookie('fileToken', token)
            return response
        except Exception as e:
            se = _serialize_exception(e)
            error = {
                'code': 200,
                'message': "Odoo Server Error",
                'data': se
            }
            return request.make_response(html_escape(json.dumps(error)))

