from odoo import fields
from odoo import models
from odoo import api
from odoo import exceptions

class Garment(models.Model):
    _name = 'littrends.garment'
    _inherit = 'product.product'
        
    designer = fields.Char(string="Designer", help="Who designed the garment?")
    mood = fields.Selection([('f', 'Formal'), ('i', 'Informal'), ('s', 'Sporty')], "Moods", help="In what kind of situation it should be worn?")
    bodyPart = fields.Selection([('t', 'Top'), ('b', 'Bottom'), ('s', 'Shoe'), ('h', 'Head')], "Body Part", help="Where to wear it?")
    garmentType = fields.Selection([('sw', 'SWEATER'), ('sh', 'SHIRT'), ('p', 'PANTS'), ('sho', 'SHORTS'), ('b', 'BOOTS'), ('sn', 'SNEAKERS'), ('b', 'BEANIE'), ('h', 'HAT')], "Type of Garment", help="What kind of garment is it?")
    promotionRequest = fields.Boolean(string="Requested for promotion", help="Should it be promoted?") 
    promoted = fields.Boolean(string="Promoted", help="Is it promoted?")
    # materials = fields.Many2many('littrends.material', ondelete='set null', string="Materials", help="What is it made of?")
    # colors = fields.Many2many('littrends.color', ondelete='set null', string="Colors", help="What colors does it have?")
    materials = fields.Many2many('littrends.material', 
        'garments_materials', 
        'garment', 
        'material',
        ondelete='set null', 
        string="Materials", 
        help="What is it made of?")
    colors = fields.Many2many('littrends.color', 
        'garments_colors', 
        'garment', 
        'color', 
        ondelete='set null', 
        string="Colors", 
        help="What colors does it have?")
    
    @api.onchange('promoted', 'promotionRequest')
    def _verify_promoted_or_requested(self):
        if self.promoted and self.promotionRequest:
            return {'warning': {'title': "Contradiction", 'message': "A garment can't be both requesting a promotion and being promoted", }, }
    
    @api.constrains('promoted', 'promotionRequest')
    def _check_promoted_or_requested(self):
        if self.promoted and self.promotionRequest:
            raise exceptions.ValidationError("A garment can't be both requesting a promotion and being promoted") 