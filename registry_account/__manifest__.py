{
    'name': 'Company Registry',
    'version': '1.0',
    'summary': 'Customize the registry page of Odoo',
    'description': 'Custom module to customize the registry page for Odoo',
    'category': 'Website',
    'author': 'Your Name',
    'depends': ['base', 'web'],
    'images': ['static/src/images/CRM.png',
               'static/src/images/Sales.png',
               'static/src/images/Online Chat.png',
               'static/src/images/Booking.png'
               ],
    'data': [
        'views/sign_up_account.xml',
        'views/add_in_login.xml',
        'views/choose_apps_views.xml',
        'templates.xml',
        
    ],
    # 'assets': {
    #     'web.assets_backend': [
    #         'registry_account/static/src/css/select_apps.css',
    #     ]
    # },
    'qweb': ['static/src/xml/select_apps_assets.xml',
             'static/src/xml/sign_up_assets.xml',],
    'installable': True,



}