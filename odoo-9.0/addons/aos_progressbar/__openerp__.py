# -*- coding: utf-8 -*-
##############################################################################
#
#    
#    Copyright (C) 2009-TODAY Alphasoft(<http://www.alphasoft.co.id>).
#    Author: Nilmar Shereef(<http://www.alphasoft.co.id>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Tree Progress Bar",
    'version' : '9.0.0.1.0',
    'license': 'AGPL-3',
    'sequence': 1,
    'author': 'Alphasoft',
    'website': "http://www.alphasoft.co.id",
    'summary': """Progress bar for tree view""",
    'description': """Added percentage default progress tree.""",
    'category': 'Extra Tools',
    'images' : ['static/description/main_screenshot.png'],
    'depends': ['base'],
    'data': [
        'views/progressbar_view.xml',
    ],
    'demo': [
        
    ],
    'qweb': [
        
    ],
    'installable': True,
}
