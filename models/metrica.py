from odoo import models, fields, api


class Pedidos(models.Model):
    _name = 'partyou.challenge.metrica'  # Table in DB
    _description = "Partyou Challenge Metrica"

    sigla = fields.Char(string="Sigla", required=True)
    name = fields.Char(string="Nome", required=True)
    descricao = fields.Text()