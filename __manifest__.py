# -*- coding: utf-8 -*-
{
    'name': "Lit Trends",

    'summary': """Check the trends""",

    'description': """
        This module allows your company to check what is trending in the Lit Fits application, helping your company make better decisions
    """,

    'author': "EuskoCode",
    'website': "http://www.euskocode.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Fashion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/garmentFormView.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
