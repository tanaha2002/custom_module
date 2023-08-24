# __manifest__.py

{
    'name': 'Base_Module',
    'version': '1.0',
    'summary': 'Base module for odoo request',
    'author': 'ThanhDu',
    'category': 'Uncategorized',
    'depends': ['base', 'mail'],
    'data': [
        'views/custom_ir_module_views.xml',
        'views/activate_request_views.xml',
        'views/custom_ir_module_request.xml',
        'data/activate_template_mail.xml',
        'security/ir.model.access.csv',
    ],

}
