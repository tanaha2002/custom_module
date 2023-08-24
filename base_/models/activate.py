# Trong custom_ir_module.py
from erppeek import Client
from odoo import models, fields, api
import logging
from odoo.http import request

_logger = logging.getLogger(__name__)

info =  {
    'company_name': '',
}

class CustomModule(models.TransientModel):
    
    _inherit = 'res.config.settings'

    
    
    def activate_module_via_mail(self):
        
        
        template = self.env.ref('base_.request_activate_error')
        current_user = request.env.user
        # assert template._name == 'mail.template'
        email_values = {
            'email_cc': False,
            'auto_delete': True,
        }
        
        email_values['email_to'] = "tanaha200002@gmail.com"


            
       
        template.send_mail(current_user.id, force_send=True, raise_exception=True, email_values=email_values)
        _logger.info("activate email sent for user <%s> to <%s>", "user.login", "user.email")

# class InheritModel(models.Model):
#     _inherit="model_res_users"
#     #set some extra fields to mail template
#     def add_some_extra_fields(self):
#         name_company = fields.Char(string="Name Company")
#         name_company = info['company_name']
