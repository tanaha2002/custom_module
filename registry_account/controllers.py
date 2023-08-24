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
    {'name': 'BÁO CÁO', 'value': 'account','icon':'registry_account/static/src/images/Survey.png'},
    {'name': 'LỊCH', 'value': 'calendar','icon':'registry_account/static/src/images/Booking.png'}
    
]
apps_2 = [
    {'name': 'QUẢN LÝ DỰ ÁN', 'value': 'project','icon':'registry_account/static/src/images/Project.png'},
    {'name': 'BẢNG CHẤM CÔNG', 'value': 'hr_attendance','icon':'registry_account/static/src/images/Employee.png'},
    {'name': 'TO DO', 'value': 'note','icon':'registry_account/static/src/images/Sales.png'},
    {'name': 'CHAT NỘI BỘ', 'value': 'mail','icon':'registry_account/static/src/images/Online Chat.png'},
    {'name': 'BÁO CÁO', 'value': 'account','icon':'registry_account/static/src/images/Survey.png'},
    {'name': 'LỊCH', 'value': 'calendar','icon':'registry_account/static/src/images/Booking.png'}
    
]

user_info = {
    'db_name': '',
    #make sure replace with ur admin password
    'admin_password': 'admin123',
    'user_password': '',
    'login_name': '',
    'name_user': '',
    'selected_apps': '',
    'type_of_db': ''
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
                #using crm-base database to clone 
                type_db = "CRM-BASE"

            elif selected_id == '2':
                #using pm-base database to clone
                type_db = "PM-BASE"
            
            with open('database_info.ini', 'r') as configfile:
                lines = configfile.readlines()

            # Find the line with 'type_of_db' and replace it
            #get name of db
            db_name = ''
            for line in lines:
                if line.startswith('db_name'):
                    db_name = line.split(' = ')[1].strip()
                    break
            
            with open('database_info.ini', 'w') as configfile:
                for line in lines:
                    if line.startswith('type_of_db'):
                        configfile.write('type_of_db = ' + type_db + '\n')

                    else:
                        configfile.write(line)
                    
            
            subprocess.check_output([sys.executable, 'custom_addons/registry_account/create_database.py'])
                   
            #redirect to login page of new database
            return request.redirect('/web/login?db=%s' % db_name)
            # return request.redirect('/selectModules')
        except subprocess.CalledProcessError as e:
            return f"Error creating database: {e.output}"
    @http.route('/selectModules', type='http', auth='public', website=True)
    def get_user_info(self, **post):
        try:
            user_info['db_name'] = post.get('company')  # Lấy giá trị từ trường db_name trong form            
            user_info['user_password'] = post.get('password')
            user_info['login_name'] = post.get('email')
            user_info['name_user'] = post.get('name')

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
                config = configparser.ConfigParser()
                config['DATABASE'] = {
                    'db_name': user_info['db_name'],
                    'admin_password': user_info['admin_password'],
                    'user_password': user_info['user_password'],
                    'login_name': user_info['login_name'],
                    'name_user': user_info['name_user'],
                    'selected_apps': user_info['selected_apps'],
                    'type_of_db': user_info['type_of_db']

                }
                with open('database_info.ini', 'w') as configfile:
                    config.write(configfile)

            
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
    




        