from odoo import models, fields

class AutoCreateDB(models.Model):
    _name = 'auto.create.db'

    db_name = fields.Char('Database Name')
    admin_password = fields.Char('Admin Password')