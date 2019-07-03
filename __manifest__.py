# -*- coding: utf-8 -*-
{
    'name': "Partyou Challenge",

    'summary': """
        Sistema de cadastro e compra de produtos""",

    'description': """
        Projeto para gestão de produtos da empresa Partyou como avaliação de candidato
    """,

    'author': "Antonio Carvalho",
    'website': "http://www.antoniorodriguescarvalho.com.br",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/chatbot_security.xml',
        'security/ir.model.access.csv',
        'views/chatbot_views.xml',
        'views/templates.xml',
        'views/partyou.xml',
        'data/status_data.xml',
        'data/metrica_data.xml'


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True
}