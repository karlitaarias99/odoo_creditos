# -*- coding: utf-8 -*-
{
    'name': "Créditos",

    'summary': """
    Aplicación creada para ASET-UPEC
       """,

    'description': """
        Aplicación creada para ASET-UPEC
    """,

    'author': "Cristopher Tenelema, Karla Arias",
    'website': "Estudiantes UPEC",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/operaciones.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
