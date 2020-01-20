from Odoo import fields
from Odoo import models

class Garment(models.Model):
    __name = 'litTrends.garment'
    __inherit = 'product.product'
    
    designer = fields.Char(string="Designer", help="Who designed the garment?")
    mood = fields.Selection(('f' 'Formal')('i' 'Informal')('s' 'Sporty'), "Moods", help="In what kind of situation it should be worn?")
    bodyPart = fields.Selection(('t' 'Top')('b' 'Bottom')('s' 'Shoe')('h' 'Head'), "Body Part", help="Where to wear it?")
    garmentType = fields.Selection(('sw' 'SWEATER')('sh' 'SHIRT')('p' 'PANTS')('sho' 'SHORTS')('b' 'BOOTS')('sn' 'SNEAKERS')('b' 'BEANIE')('h' 'HAT'), "Type of Garment", help="What kind of garment is it?")
    promotionRequest = fields.Boolean(string="Requested for promotion", help="Should it be promoted?") 
    promoted = fields.Boolean(string="Promoted", help="Is it promoted?")
    materials = fields.Many2Many(litTrends.material, string="Materials", help="What is it made of?")