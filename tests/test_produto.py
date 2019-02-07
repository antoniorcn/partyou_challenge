from odoo.tests.common import TransactionCase


class TestProduto(TransactionCase):

    def setUp(self, *args, **kwargs):
        result = super(TestProduto, self).setUp(*args, **kwargs)
        # Prepare environment with the Admin user
        # user_admin = self.env.ref('base.user_admin')
        # self.env = self.env(user=user_admin)
        # Setup test data
        self.produto = self.env['partyou.challenge.produto']
        self.produto_ode = self.produto.create({
            'name': 'Iogurte Vigor - Morango 900ml',
            'preco': 6.8,
            'quantidade': 900,
            'descricao':'Iogurte Vigor sabor morango'})
        return result

    def test_create(self):
        "Teste Produto sao ativos por default"
        self.assertEqual(self.produto_ode.quantidade, 900)

