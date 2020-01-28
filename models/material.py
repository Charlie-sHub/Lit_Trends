from odoo import fields
from odoo import models

class Material(models.Model):
    _name = 'littrends.material'
    
    name = fields.Char(string="Material", required=True)
