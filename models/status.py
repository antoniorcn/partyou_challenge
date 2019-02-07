from odoo import models, fields, api


class Pedidos(models.Model):
    _name = 'partyou.challenge.status'  # Table in DB
    _description = "Partyou Challenge Status"

    name = fields.Char(string="Nome do Status", required=True)
    descricao = fields.Text()