from Odoo import fields
from Odoo import models

class Color(models.Model):
    __name = 'litTrends.color'
    __inherit = 'product.product.color'
    
    name = fields.Char(string="Color", required=True)
