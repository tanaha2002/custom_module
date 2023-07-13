# from odoo import api, models
# from odoo import http
# from odoo.http import request
# import subprocess
# import sys



# class RegistryAccount(http.Controller):

#     @http.route('/create_database', type='http', auth='public', website=True)
#     def main(self, **kw):
#         return request.render('auto_create_db.auto_create_db_menu',{})
#     @http.route('/auto_create_db/create_database', type='http', auth='public', website=True)
#     def create_database(self):
#         try:
#             subprocess.check_output([sys.executable, 'D:\Odoo16\server\odoo\custom_addons\\auto_create_db\create_database.py'])
#             return "Database created successfully!"
#         except subprocess.CalledProcessError as e:
#             return f"Error creating database: {e.output}"
        
from odoo import http
from odoo.http import request
import subprocess
import sys
from odoo import models, fields
import configparser
import os

class RegistryAccount(http.Controller):

    @http.route('/create_database', type='http', auth='public', website=True)
    def main(self, **kw):
        return request.render('auto_create_db.auto_create_db_menu', {})

    @http.route('/auto_create_db/create_database', type='http', auth='public', website=True)
    def create_database(self, **post):
        try:
            db_name = post.get('db_name')  # Lấy giá trị từ trường db_name trong form
            admin_password = post.get('admin_password')  # Lấy giá trị từ trường admin_password trong form
            
            # # Tạo record mới trong model "auto.create.db" với các giá trị từ form
            # AutoCreateDB = request.env['auto.create.db']
            # AutoCreateDB.create({
            #     'db_name': db_name,
            #     'admin_password': admin_password
            # })
            # Lưu thông tin vào tệp

            config = configparser.ConfigParser()
            config['DATABASE'] = {
                'db_name': str(db_name),
                'admin_password': str(admin_password)
            }
            with open('database_info.ini', 'w') as configfile:
                config.write(configfile)

            # Thực thi file create_database.py
            subprocess.check_output([sys.executable, 'D:\Odoo16\server\odoo\custom_addons\\auto_create_db\create_database.py'])

            return "Database created successfully!"
        except subprocess.CalledProcessError as e:
            return f"Error creating database: {e.output}"
