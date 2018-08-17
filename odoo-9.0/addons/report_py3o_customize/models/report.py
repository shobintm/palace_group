# -*- coding: utf-8 -*-
# Copyright 2017 Akretion (http://www.akretion.com/)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class Report(models.Model):

    _inherit = 'report'

    @api.model
    def _get_report_from_name(self, report_name):
        """Get the first record of ir.actions.report.xml having the
        ``report_name`` as value for the field report_name.
        """
        res = super(Report, self)._get_report_from_name(report_name)
        if res:
            return res
        # maybe a py3o report
        report_obj = self.env['ir.actions.report.xml']
        context = self.env['res.users'].context_get()
        return report_obj.with_context(context).search(
            [('report_type', '=', 'py3o'),
             ('report_name', '=', report_name)], limit=1)

    @api.model
    def _check_attachment_use(self, docids, report):
        """ Check attachment_use field. If set to true and an existing pdf is already saved, load
        this one now. Else, mark save it.
        """
        save_in_attachment = {}
        save_in_attachment['model'] = report.model
        save_in_attachment['loaded_documents'] = {}

        if report.attachment:
            records = self.env[report.model].browse(docids)
            filenames = self._attachment_filename(records, report)
            attachments = None
            if report.attachment_use:
                attachments = self._attachment_stored(records, report, filenames=filenames)
            for record_id in docids:
                filename = filenames[record_id]

                # If the user has checked 'Reload from Attachment'
                if attachments:
                    attachment = attachments[record_id]
                    if attachment:
                        # Add the loaded pdf in the loaded_documents list
                        pdf = attachment.datas
                        pdf = base64.decodestring(pdf)
                        save_in_attachment['loaded_documents'][record_id] = pdf
                        _logger.info('The PDF document %s was loaded from the database' % filename)

                        continue  # Do not save this document as we already ignore it

                # If the user has checked 'Save as Attachment Prefix'
                if filename is False:
                    # May be false if, for instance, the 'attachment' field contains a condition
                    # preventing to save the file.
                    continue
                else:
                    save_in_attachment[record_id] = filename  # Mark current document to be saved

        return save_in_attachment
