# -*- coding: utf-8 -*-
{
    'name': "imw_Customization",
    'installable': True,
    'application': False,
    'auto_install': False,
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Sky",
    'website': "http://www.Sky.com.eg",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly     
 'depends': ['base','stock_account', 'barcodes' ,'purchase', 'sale_management','account', 'analytic'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account.xml',
        'views/product.xml',
        'views/purchase.xml',
        'views/sale.xml',
        'views/sale_report.xml',
        'views/report_saleorder_wo_subtotal.xml',
        'views/report_saleorder_wo_totals.xml',
        'views/templates.xml',
        'views/views.xml',
        'views/account_report.xml',
        'views/report_journal_entries.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
