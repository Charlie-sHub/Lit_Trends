from Odoo import models

class Color(models.Model):
    __name = 'litTrends.color'
    
    name = fields.Char(required=True)