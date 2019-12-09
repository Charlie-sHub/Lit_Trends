from Odoo import fields
from Odoo import models

class Material(models.Model):
    __name = 'litTrends.material'
    
    name = fields.Char(string="Barcode", required=True)
