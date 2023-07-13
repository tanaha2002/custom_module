from odoo import http
from odoo.http import request

class CustomPageController(http.Controller):
    
    @http.route('/web/login', auth='public', website=True)
    def custom_page(self, **kwargs):
        return request.render('custom_page.custom_page_template')
