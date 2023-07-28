# Trong custom_ir_module.py

from odoo import models, fields, api
from odoo.modules.module import Module

class CustomModule(Module):
    _inherit = 'ir.module.module'

    def my_custom_function(self):
        print("Hello from my_custom_function!")
    
