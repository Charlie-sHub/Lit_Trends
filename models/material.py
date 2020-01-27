from Odoo import fields
from Odoo import models

class Material(models.Model):
    _name = 'littrends.material'
    
    name = fields.Char(string="Material", required=True)
