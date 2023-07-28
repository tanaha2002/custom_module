from odoo import models
import xmlrpc.client
from odoo import fields
from odoo.models import api
class CustomModule(models.Model):
    _name = 'request_module.module'

    @api.model
    def custom_function(self):
        # Thông tin kết nối database A
        db_name_a = 'regisssss'
        db_user_a = 'admin1'
        db_password_a = '123'
        db_host_a = 'http://localhost'
        db_port_a = '8069'

        # Kết nối tới database A sử dụng XML-RPC
        common = xmlrpc.client.ServerProxy(f'http://{db_host_a}:{db_port_a}/xmlrpc/common')
        uid = common.authenticate(db_name_a, db_user_a, db_password_a, {})
        if not uid:
            raise Exception('Không thể xác thực người dùng trên database A.')

        # Gửi yêu cầu tới database A
        models = xmlrpc.client.ServerProxy(f'http://{db_host_a}:{db_port_a}/xmlrpc/object')
        request_model = 'module.request'  # Tên model trên database A
        new_request_id = models.execute_kw(db_name_a, uid, db_password_a, request_model, 'create', [{
            'module_id': self.id,
            'request_user_id': self.env.user.id,
            # Thêm các trường và giá trị bạn cần lưu trong record mới
        }])

        # Sau khi gửi yêu cầu thành công, bạn có thể thực hiện các thao tác khác tại đây
