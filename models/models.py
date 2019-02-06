# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PartyouChallenge(models.Model):
     _name = 'partyou.challenge.product' # Table in DB
     _description = "Partyou Challenge"

     nome = fields.Char(string="Nome", required=True)
     validade = fields.Datetime(string="Validade", required=False, default=fields.Datetime.now)
     preco = fields.Float(string="Preco", required=False)
     peso = fields.Float(string="Peso", required=False)

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100