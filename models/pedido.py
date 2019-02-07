from odoo import models, fields, api


class Pedidos(models.Model):
    _name = 'partyou.challenge.pedido'  # Table in DB
    _description = "Partyou Challenge Pedido"

    status = fields.Many2one('partyou.challenge.status', string='Status')
    data_despacho = fields.Date()
    produtos = fields.Many2many('partyou.challenge.produto', string="Produtos")