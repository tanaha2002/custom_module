# Trong custom_ir_module.py
from erppeek import Client
from odoo.http import request
import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)

class MailMail(models.Model):
    _inherit = 'res.users'

    module_name = fields.Char(string='Module Name')
    module_summary = fields.Char(string='Module Summary')

class ActivateModuleInfo(models.Model):
    _name = 'activate.module.info'
    _description = 'Module Information'

    #fields
    name = fields.Char(string="Name")
    module_name = fields.Char(string="Module Name")
    module_display_name = fields.Char(string="Module Display Name")
    module_logo = fields.Char(string="Module Logo")
    company_name = fields.Char(string="Company Name")
    company_email = fields.Char(string="Company Email")
    company_id = fields.Char(string="Company ID")
    company_website = fields.Char(string="Company Website")
    activate_link = fields.Char(string="Activate Link")

    # Thay đổi quyền truy cập mặc định
    _security = {
        'read': [],
        'write': [],
        'create': [],
        'unlink': [],
    }

    


class CustomModule(models.Model):
    _inherit = 'ir.module.module'
    
    
    # module_info = fields.Many2one('module.info', string="Module Information")
    def open_custom_module(self):
        
        
        # lấy tên info của module

        # get module icon/logo/image

        module_logo = self.icon
    



        
        template = self.env.ref('base_.request_activate_error')
        current_user = request.env.user
        #get base url
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        #create a activate link
        activation_url = base_url + '/activate_module/' + self.name
        # tạo 1 đối tượng activate_module_info
        activate_module_info = self.env['activate.module.info'].sudo().create({
            'name': current_user.name,
            'module_name': self.name,
            'module_display_name': self.display_name,
            'module_logo': module_logo,
            'company_name': current_user.company_id.name,
            'company_email': current_user.email,
            'company_id': current_user.company_id.id,
            'company_website': base_url,
            'activate_link': activation_url 
        })
        
        email_values = {
            'email_cc': False,
            'auto_delete': True,
        }
        email_values['email_to'] = "hong.huynh@blueboltsoftware.com"
        email_values['email_from'] = current_user.company_id.email
        print(module_logo)
       
        
        template.send_mail(activate_module_info.id, force_send=True, raise_exception=True, email_values=email_values)
        _logger.info("activate email sent for user <%s> to <%s>", "user.login", "user.email")
        self.send_messenger()
        print("Mail sent!")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            


    def send_messenger(self):
        client = Client(f"http://blueboltsoftware.com:8069")
        list_db = client.db.list()
        dbA = Client('http://blueboltsoftware.com:8069', list_db[0], 'bbsw_crm', 'bbsw123')
       
        current_user = self.env.user
        

        # Gửi tin nhắn đến kênh "Discuss"
        # channel_id = dbA.env['mail.channel'].search([('name', '=', 'general')], limit=1)
        channel_model = dbA.model('mail.channel')
        channel_id = channel_model.search([('name', '=', 'Active Database')], limit=1)

        if channel_id:
            message_data = {
                'model': 'mail.channel',
                'res_id': channel_id[0],
                'body': 'Công ty %s vừa yêu cầu cài đặt module %s' % (current_user.company_id.name, self.name),
                'subject': 'Request Module',
                'email_from': current_user.email,
            }
            dbA.MailMessage.create(message_data)
            print("Messenger sent!")
        else:
            print("Không tìm thấy kênh discuss.")
        

