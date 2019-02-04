# -*- coding: utf-8 -*-
from odoo import http

# class PartyouChallenge(http.Controller):
#     @http.route('/partyou_challenge/partyou_challenge/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partyou_challenge/partyou_challenge/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partyou_challenge.listing', {
#             'root': '/partyou_challenge/partyou_challenge',
#             'objects': http.request.env['partyou_challenge.partyou_challenge'].search([]),
#         })

#     @http.route('/partyou_challenge/partyou_challenge/objects/<model("partyou_challenge.partyou_challenge"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partyou_challenge.object', {
#             'object': obj
#         })