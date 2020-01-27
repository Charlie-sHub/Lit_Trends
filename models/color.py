from Odoo import fields
from Odoo import models

class Color(models.Model):
    _name = 'littrends.color'
    _inherit = 'product.product.color'
    
    name = fields.Char(string="Color", required=True)
