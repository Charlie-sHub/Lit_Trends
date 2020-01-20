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
    colors = fields.Many2Many(litTrends.color, string="Colors", help="What colors does it have?")
    
    @api.onchange('promoted', 'promotionRequest')
    def __verify_promoted_or_requested(self):
        if r.promoted and r.promotionRequest:
            return {'warning' : {'title': "Contradiction", 'message': "A garment can't be both requesting a promotion and being promoted",},}
    
    @api.constrais('promoted', 'promotionRequest')
    def __check_promoted_or_requested(self):
        for r in self:
            if r.promoted and r.promotionRequest:
                raise exceptions.ValidationError("A garment can't be both requesting a promotion and being promoted") 