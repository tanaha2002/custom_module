# Trong custom_ir_module.py
from erppeek import Client

from odoo import models, fields, api

class CustomModule(models.Model):
    _inherit = 'ir.module.module'
    
    def open_custom_module(self):
        # Đoạn code xử lý khi bấm vào nút (button) trong đây
        # Ví dụ: In ra thông báo
        #call function sent_messenger
        self.sent_messenger()
        print("Hello from open_custom_module!")

    def sent_messenger(self):
        dbA = Client('http://localhost:8069', 'regisssss', 'admin1', 'admin')
        # Tạo người dùng tạm thời trong cơ sở dữ liệu A
        #get current user login in odoo

        current_user = self.env.user

        # Gửi tin nhắn đến kênh "Discuss"
        channel_id = self.env['mail.channel'].search([('name', '=', 'general')], limit=1)
        
        if channel_id:
            message_data = {
                'model': 'mail.channel',
                'res_id': channel_id.id,
                'body': 'Công ty %s vừa yêu cầu cài đặt module %s' % (current_user.company_id.name, self.name),
                'subject': 'Request Module',
                'email_from': current_user.email,
                'author_id': current_user.partner_id.id,
            }
            dbA.MailMessage.create(message_data)
        else:
            print("Không tìm thấy kênh discuss.")
