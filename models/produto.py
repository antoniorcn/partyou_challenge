from odoo import models, fields, api


class Produtos(models.Model):
     _name = 'partyou.challenge.produto' # Table in DB
     _description = "Partyou Challenge Produto"

     name = fields.Char(string="Nome", required=True)
     validade = fields.Datetime(string="Validade", required=False, default=fields.Datetime.now)
     preco = fields.Float(string="Preco", required=False)
     metrica = fields.Many2one('partyou.challenge.metrica', string='Metrica')
     quantidade = fields.Float(string="Quantidade", required=False)
     descricao = fields.Text()
     imagem = fields.Binary('Imagem')