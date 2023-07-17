{
    'name': 'Company Registry',
    'version': '1.0',
    'summary': 'Customize the registry page of Odoo',
    'description': 'Custom module to customize the registry page for Odoo',
    'category': 'Website',
    'author': 'Your Name',
    'depends': ['base', 'web'],
    'data': [
        'views/sign_up_account.xml',
        'views/add_in_login.xml',
        'templates.xml',
    ],
    'installable': True,
    'auto_install': True


}