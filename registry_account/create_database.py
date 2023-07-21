import erppeek
import configparser
import os
url = 'http://localhost:8069'

# # Đọc thông tin từ tệp
config = configparser.ConfigParser()
# custom_module_path = os.path.dirname(__file__)
# config_file_path = os.path.join(custom_module_path, 'database_info.ini')
config.read('database_info.ini')
db_name = config['DATABASE']['db_name']
admin_password = config['DATABASE']['admin_password']
user_password = config['DATABASE']['user_password']
login = config['DATABASE']['login_name']
name_user = config['DATABASE']['name_user']
#get list app from file:
selected_apps = config['DATABASE']['selected_apps'].split(',')
client = erppeek.Client(server=url)

#tạo database và các app được chọn
client.create_database(admin_password, db_name,demo=False,user_password=user_password,login=login)



# Cài đặt các module đã chọn
def install_modules(client, selected_apps):
    module_obj = client.model('ir.module.module')
    for app in selected_apps:
        module = module_obj.search([('name', '=', app)])
        print(module)
        if module:
            module_obj.button_immediate_install(module[0])

install_modules(client, selected_apps)


#sửa đổi tên user
user = client.model('res.users').search([('login', '=', login)])
client.model('res.users').write(user, {'name': name_user})
