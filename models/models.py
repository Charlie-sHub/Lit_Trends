# -*- coding: utf-8 -*-

from odoo import models, fields, api

# author: Asier Vila

class Garment(models.Model): #Extends Product 
	_inherit = 'product.product'
	#_name = 'lit_trends.garment'

	# Inherited fields:
	# barcode
	# price
	# color
	
	designer = fields.Char()
	material = fields.Char()
	mood = fields.Char()
	garment_type = fields.Char()
	body_part = fields.Char()
	available = fields.Boolean(default=False)
	promotion_request = fields.Boolean(default=False)
	promoted = fields.Boolean(default=False)


class Trends(models.Model):
	_name = 'lit_trends.trends'

	start_date = fields.Date(default = fields.date.today)
	end_date = fields.Date(default = fields.date.today)


class User_Trends(models.Model): #Extends Trends
	_inherit = 'lit_trends.trends'
	#_name = 'lit_trends.user_trends'


class Expert_Trends(models.Model): #Extends Trends
	_inherit = 'lit_trends.trends'
	#_name = 'lit_trends.expert_trends'


# class lit_trends(models.Model):
#     _name = 'lit_trends.lit_trends'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
