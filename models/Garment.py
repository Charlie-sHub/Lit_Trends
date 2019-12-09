from Odoo import fields
from Odoo import models

class Garment(models.Model):
    __name = 'litTrends.garment'
    
    barcode = fields.Integer(string="Barcode", required=True)
    mood # enum
    designer = fields.Char(string="Designer")
    price = fields.Float(string="Price")
    bodyPart # enum
    garmentType # enum
    available = fields.Boolean(string="Is it available")
    promotionRequest = fields.Boolean(string="Requested for promotion") 
    promoted = fields.Boolean(string="Promoted")
    materials # enum
    colors # enum
    image # What to do with this?