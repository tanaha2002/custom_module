from odoo import api, models
import logging

_logger = logging.getLogger(__name__)

class AutoCreateDB(models.AbstractModel):
    _name = 'auto.create.db'

    @api.model
    def _create_database(self):
        db_name = 'basicdatabase'
        admin_password = '123456'
        try:

        
            self._create_empty_database(db_name)

            self._set_admin_password(admin_password, db_name)
        except Exception as e:
            _logger.error("error at: %s", str(e))


    @api.model
    def _create_empty_database(self, db_name):
        self.env.cr.create_empty_db(db_name)

    @api.model
    def _set_admin_password(self, admin_password, db_name):
        admin_user = self.env['res.users'].sudo().search([('login', '=', 'admin')], limit=1)
        admin_user.with_context(force_company=db_name).write({'password': admin_password})