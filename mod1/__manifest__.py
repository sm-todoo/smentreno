# -*- coding: utf-8 -*-
{
    'name': "mod1",

    'summary': """
        Mi primer modulo""",

    'description': """
        Este modulo permitira la experimentacion y entrenamiento para mejorar el entendimiento de odoo
    """,

    'author': "Santiago Mosquera Albarracin",
    'website': "http://www.todoo.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Entrenamiento',
    'version': '3.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
      #  'views/templates.xml',
    ],
    # only loaded in demonstration mode
   #'demo': [
   #    'demo/demo.xml',
   # ],
}
