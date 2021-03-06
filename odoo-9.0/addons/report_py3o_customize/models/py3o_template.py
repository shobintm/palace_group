# -*- coding: utf-8 -*-
# Copyright 2013 XCG Consulting (http://odoo.consulting)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from openerp import fields, models


class Py3oTemplate(models.Model):
    _name = 'py3o.template'

    name = fields.Char(required=True)
    py3o_template_data = fields.Binary("LibreOffice Template")
    filetype = fields.Selection(
        selection=[
            ('odt', "Template ODT File"),
            ('ods', "Template ODS File"),
        ],
        string="File Type",
        required=True,
        default='odt')
