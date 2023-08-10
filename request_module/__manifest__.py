# __manifest__.py

{
    'name': 'Custom Module',
    'version': '1.0',
    'summary': 'Customizations for module installation',
    'author': 'Your Name',
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