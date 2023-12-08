import unittest
from contatos import Contato
import xmlrunner

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

    def test_nome_diferente(self):
        outro_contato = Contato("Maria", "Silva", "123456789", "EmpresaX", "maria.silva@email.com")
        self.assertNotEqual(self.contato, outro_contato)

    def test_sobrenome_diferente(self):
        outro_contato = Contato("João", "Oliveira", "123456789", "EmpresaX", "joao.oliveira@email.com")
        self.assertNotEqual(self.contato, outro_contato)

    def test_telefone_diferente(self):
        outro_contato = Contato("João", "Silva", "987654321", "EmpresaX", "joao.silva@email.com")
        self.assertNotEqual(self.contato, outro_contato)
        
if __name__ == '__main__':
    with open('resultados_testes_contatos.xml', 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output)
        unittest.main(testRunner=runner)
