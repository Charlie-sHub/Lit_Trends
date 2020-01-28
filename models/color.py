from odoo import fields
from odoo import models

class Color(models.Model):
    _name = 'littrends.color'
    
    name = fields.Char(string="Color", required=True)
