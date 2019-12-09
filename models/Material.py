from Odoo import models

class Material(models.Model):
    __name = 'litTrends.material'
    
    name = fields.Char(required=True)