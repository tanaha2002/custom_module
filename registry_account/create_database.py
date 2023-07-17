import erppeek
import configparser
url = 'http://localhost:8069'

# # Đọc thông tin từ tệp
config = configparser.ConfigParser()
config.read('database_info.ini')
db_name = config['DATABASE']['db_name']
admin_password = config['DATABASE']['admin_password']
user_password = config['DATABASE']['user_password']
login = config['DATABASE']['login_name']
name_user = config['DATABASE']['name_user']
client = erppeek.Client(server=url)
client.create_database(admin_password, db_name,demo=False,user_password=user_password,login=login)
#sửa đổi tên user
user = client.model('res.users').search([('login', '=', login)])
client.model('res.users').write(user, {'name': name_user})