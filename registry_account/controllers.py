# -*- coding: utf-8 -*-
from odoo import http
import subprocess
import sys
import configparser
import os
from odoo.http import request
import erppeek
#list of apps
apps_1 = [
    {'name': 'CRM', 'value': 'crm','icon':'registry_account/static/src/images/CRM.png'},
    {'name': 'LIÊN HỆ', 'value': 'contacts','icon':'registry_account/static/src/images/Approved.png'},
    {'name': 'BÁN HÀNG', 'value': 'sale_management','icon':'registry_account/static/src/images/Sales.png'},
    {'name': 'CHAT NỘI BỘ', 'value': 'mail','icon':'registry_account/static/src/images/Online Chat.png'},
    {'name': 'BÁO CÁO', 'value': 'account_accountant','icon':'registry_account/static/src/images/Survey.png'},
    {'name': 'LỊCH', 'value': 'calendar','icon':'registry_account/static/src/images/Booking.png'}
    
]
apps_2 = [
    {'name': 'QUẢN LÝ DỰ ÁN', 'value': 'project','icon':'registry_account/static/src/images/Project.png'},
    {'name': 'BẢNG CHẤM CÔNG', 'value': 'hr_attendance','icon':'registry_account/static/src/images/Employee.png'},
    {'name': 'TO DO', 'value': 'note','icon':'registry_account/static/src/images/Sales.png'},
    {'name': 'CHAT NỘI BỘ', 'value': 'mail','icon':'registry_account/static/src/images/Online Chat.png'},
    {'name': 'BÁO CÁO', 'value': 'account_accountant','icon':'registry_account/static/src/images/Survey.png'},
    {'name': 'LỊCH', 'value': 'calendar','icon':'registry_account/static/src/images/Booking.png'}
    
]

user_info = {
    'db_name': '',
    'admin_password': '123456',
    'user_password': '',
    'login_name': '',
    'name_user': '',
    'selected_apps': ''
}
class RegistryAccount(http.Controller):


    @http.route('/registryAccount', type='http', auth='public', website=True)
    def main(self, **kw):
        return request.render('registry_account.signup', {})
    
    @http.route('/addDatabase', type='http', auth='public', website=True, methods=['POST'])
    def create_database(self, **post):
        try:
            #get list app id selected (1 or 2)
            selected_id = post.get('apps_1')
            print(selected_id)
            if selected_id == '1':
                #just join the value of apps_1
                user_info['selected_apps'] = ','.join([app['value'] for app in apps_1])
                user_info['selected_apps'] += ',web,modern_theme'
            elif selected_id == '2':
                #just join the value of apps_2
                user_info['selected_apps'] = ','.join([app['value'] for app in apps_2])
                user_info['selected_apps'] += ',web,modern_theme'
            

            #write all info to file database_info.ini
            config = configparser.ConfigParser()
            config['DATABASE'] = {
                'db_name': user_info['db_name'],
                'admin_password': user_info['admin_password'],
                'user_password': user_info['user_password'],
                'login_name': user_info['login_name'],
                'name_user': user_info['name_user'],
                'selected_apps': user_info['selected_apps']

            }
            if self.check_db_exist(user_info['db_name']):
                # Hiển thị pop-up thông báo
                alert_message = "Tên database đã tồn tại. Hãy chọn một tên khác."
                return """
                    <script>
                        alert('%s');
                        window.location.href = '/registryAccount';
                    </script>
                """ % alert_message
            else:
            # custom_module_path = os.path.dirname(__file__)
            # config_file_path = os.path.join(custom_module_path, 'database_info.ini')
                with open('database_info.ini', 'w') as configfile:
                    config.write(configfile)
                # Thực thi file create_database.py
                subprocess.check_output([sys.executable, 'odoo/custom_addons/registry_account/create_database.py'])
                return request.redirect('/web/login?%s')
            # return request.redirect('/selectModules')
        except subprocess.CalledProcessError as e:
            return f"Error creating database: {e.output}"
    @http.route('/selectModules', type='http', auth='public', website=True)
    # def main_select_apps(self, **kw):
    #     return request.render('registry_account.select_apps', {'apps_1': apps_1, 'apps_2': apps_2})
    def get_user_info(self, **post):
        try:
            user_info['db_name'] = post.get('company')  # Lấy giá trị từ trường db_name trong form
            user_info['user_password'] = post.get('password')
            user_info['login_name'] = post.get('email')
            user_info['name_user'] = post.get('name')
            print(self.check_db_exist(user_info['db_name']))
            
            # Chuyển hướng đến trang chọn ứng dụng
            return request.render('registry_account.select_apps', {'apps_1': apps_1, 'apps_2': apps_2})
        except subprocess.CalledProcessError as e:
            return f"Error creating database: {e.output}"
        
    def check_db_exist(self, db_name):
        url = 'http://localhost:8069'
        client = erppeek.Client(server=url)
        db_list = client.db.list()
        print(db_list)
        if db_name in db_list:
            return True
        return False
    




        