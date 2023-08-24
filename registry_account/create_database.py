import erppeek
import configparser
import os
import time
import subprocess
from xmlrpc import client
# # Đọc thông tin từ tệp
config = configparser.ConfigParser()
config.read('database_info.ini')
db_name = config['DATABASE']['db_name']
admin_password = config['DATABASE']['admin_password']
user_password = config['DATABASE']['user_password']
login = config['DATABASE']['login_name']
name_user = config['DATABASE']['name_user']
#get list app from file:
selected_apps = config['DATABASE']['selected_apps'].split(',')
db_name_clone = config['DATABASE']['type_of_db']
#replace with ur base-database info
base_login = "admin"
base_passwd = "admin123@"

# Source Odoo database info
url = 'http://localhost:8069'

# Target Odoo database info
base_login = 'admin'
base_passwd = 'admin123@'

#linux
shell_script_path = "custom_addons/registry_account/duplicate.sh"  # Use raw string to handle backslashes
subprocess.check_output([shell_script_path, db_name,db_name_clone, admin_password])

#create a new user in new database
client = erppeek.Client(server=url, db=db_name_clone, user=base_login, password=base_passwd)
client.create('res.users', {'login': login, 'password': user_password, 'name': name_user})
