import erppeek
import configparser
url = 'http://localhost:8069'
# db_name = 'TAMBIETANHPHONGgggg'
# admin_password = '123456'
# # Đọc thông tin từ tệp
config = configparser.ConfigParser()
config.read('database_info.ini')
db_name = config['DATABASE']['db_name']
admin_password = config['DATABASE']['admin_password']
print("OK got data")

client = erppeek.Client(server=url)
client.create_database(admin_password, db_name)
# import erppeek
# import sys


# url = 'http://localhost:8069'

# # Sử dụng Odoo ORM để lấy thông tin từ model "auto.create.db"
# AutoCreateDB = request.env['auto.create.db']
# record = AutoCreateDB.search([], limit=1)

# # Lấy giá trị từ record
# db_name = record.db_name
# admin_password = record.admin_password

# client = erppeek.Client(server=url)
# client.create_database(admin_password, db_name)
# import configparser

# # Đọc thông tin từ tệp
# config = configparser.ConfigParser()
# config.read('database_info.ini')
# db_name = config['DATABASE']['db_name']
# admin_password = config['DATABASE']['admin_password']

# url = 'http://localhost:8069'

# # Lấy các giá trị từ controllers.py


# client = erppeek.Client(server=url)
# client.create_database(admin_password, db_name)