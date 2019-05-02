# -*- coding: utf-8 -*-
{
    'name': "Ecole",

    'summary': """
        Module de gestion d'une école""",

    'description': """
        Gestion des services d'une école
    """,

    'author': "Judais Steeven",
    'website': "http://www.team-dsi.fr",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/res_partner_views.xml',
        'security/ir.model.access.csv',
        'views/classe_views.xml',
        'views/professeur_views.xml',
        'views/eleve_views.xml',
        'views/cours_views.xml',
        'views/agenda_views.xml',
        'views/ecole_views.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
