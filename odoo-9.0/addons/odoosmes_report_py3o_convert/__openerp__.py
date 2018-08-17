# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Excel, Word, Pdf Report Convert",
    'category': 'Extra Tools',
    "summary": """Convert ods, odt report
    to xlsx, pdf, xls, docx, doc ... with Libreoffice""",
    "version": "9.0",
    "author": "Elico Corp, Cybers Thang",
    "support": "support@elico-corp.com, ducthangict.dhtn@gmail.com",
    "license": "AGPL-3",
    "website": "https://odoosmes.com",
    "depends": [
        "report_py3o_customize",
    ],
    'data': [
        'report/SO/docx/sale_order.xml'
    ],
    'images': ['static/description/bg.png'],
    "installable": True,
    "application": True,
}
