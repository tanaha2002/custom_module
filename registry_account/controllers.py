# -*- coding: utf-8 -*-
from odoo import http
import subprocess
import sys
import configparser
from odoo.http import request
class RegistryAccount(http.Controller):


    @http.route('/registryAccount', type='http', auth='public', website=True)
    def main(self, **kw):
        return request.render('registry_account.signup', {})
    
    @http.route('/addDatabase', type='http', auth='public', website=True, methods=['POST'])
    def create_database(self, **post):
        try:
            admin_password = '123456'
            db_name = post.get('company')  # Lấy giá trị từ trường db_name trong form
            user_password = post.get('password')
            login = post.get('email')

            
            config = configparser.ConfigParser()
            config['DATABASE'] = {
                'db_name': str(db_name),
                'admin_password': str(admin_password),
                'user_password': str(user_password),
                'login_name': str(login)

            }
            with open('database_info.ini', 'w') as configfile:
                config.write(configfile)

            # Thực thi file create_database.py
            subprocess.check_output([sys.executable, 'D:\Odoo16\server\odoo\custom_addons\\registry_account\create_database.py'])

            return request.redirect('/web/login?%s')
        except subprocess.CalledProcessError as e:
            return f"Error creating database: {e.output}"

        