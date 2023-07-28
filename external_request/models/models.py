from odoo import fields, models, api
class TestModel(models.Model):
    _name = "test.model"
    _description = "Test Model"

    @api.model
    def custom_function(self):
        # Hàm custom của bạn ở đây
        # Ví dụ: In ra thông báo khi gọi hàm
        print("Hello from custom_function!")

