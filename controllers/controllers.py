# -*- coding: utf-8 -*-
from odoo import http

# class LitTrends(http.Controller):
#     @http.route('/lit__trends/lit__trends/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lit__trends/lit__trends/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('lit__trends.listing', {
#             'root': '/lit__trends/lit__trends',
#             'objects': http.request.env['lit__trends.lit__trends'].search([]),
#         })

#     @http.route('/lit__trends/lit__trends/objects/<model("lit__trends.lit__trends"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lit__trends.object', {
#             'object': obj
#         })