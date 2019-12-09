from Odoo import fields
from Odoo import models

class Garment(models.Model):
    __name = 'litTrends.garment'
    
    barcode = fields.Integer(string="Barcode", required=True)
    designer = fields.Char(string="Designer")
    price = fields.Float(string="Price")
    mood = fields.Selection(('f' 'Formal')('i' 'Informal')('s' 'Sporty'), "Moods")
    bodyPart = fields.Selection(('t' 'Top')('b' 'Bottom')('s' 'Shoe')('h' 'Head'), "Body Part")
    garmentType = fields.Selection(('sw' 'SWEATER')('sh' 'SHIRT')('p' 'PANTS')('sho' 'SHORTS')('b' 'BOOTS')('sn' 'SNEAKERS')('b' 'BEANIE')('h' 'HAT'), "Type of Garment")
    available = fields.Boolean(string="Is it available")
    promotionRequest = fields.Boolean(string="Requested for promotion") 
    promoted = fields.Boolean(string="Promoted")
    materials = fields.Many2Many(litTrends.material, string="Materials")
    colors = fields.Many2Many(litTrends.color, string="Colors")
    image # What to do with this?