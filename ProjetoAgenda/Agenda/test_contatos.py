import unittest
from contatos import Contato

class TestContato(unittest.TestCase):
    def setUp(self):
        # Cria um contato para uso nos testes
        self.contato = Contato("João", "Silva", "123456789", "EmpresaX", "joao.silva@email.com")

    def test_getters(self):
        self.assertEqual(self.contato.get_nome(), "João")
        self.assertEqual(self.contato.get_sobrenome(), "Silva")
        self.assertEqual(self.contato.get_telefone(), "123456789")
        self.assertEqual(self.contato.get_empresa(), "EmpresaX")
        self.assertEqual(self.contato.get_email(), "joao.silva@email.com")

    def test_setters(self):
        # Modifica alguns atributos do contato
        self.contato.set_nome("Maria")
        self.contato.set_sobrenome("Oliveira")
        self.contato.set_telefone("987654321")
        self.contato.set_empresa("EmpresaY")
        self.contato.set_email("maria.oliveira@email.com")

        # Verifica se os setters funcionaram corretamente
        self.assertEqual(self.contato.get_nome(), "Maria")
        self.assertEqual(self.contato.get_sobrenome(), "Oliveira")
        self.assertEqual(self.contato.get_telefone(), "987654321")
        self.assertEqual(self.contato.get_empresa(), "EmpresaY")
        self.assertEqual(self.contato.get_email(), "maria.oliveira@email.com")

if __name__ == '__main__':
    unittest.main()
