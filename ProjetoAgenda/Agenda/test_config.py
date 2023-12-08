import unittest
from config import Config
import xmlrunner

class Contato:
    def __init__(self, nome, sobrenome, telefone, empresa, email):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.empresa = empresa
        self.email = email

class TestConfig(unittest.TestCase):

    def test_formatar_contato(self):
        """
        Testa se a função formatar_contato da classe Config formata corretamente um objeto Contato.
        """
        config = Config()

        # Criar um objeto Contato para teste
        contato = Contato(nome="   João  ", sobrenome="   Silva   ", telefone="   123  ", empresa="   Empresa X   ", email="   joao.silva@example.com   ")

        resultado = config.formatar_contato(contato)

        # Verificar se a formatação está correta
        self.assertEqual(resultado, "Nome: João / Sobrenome: Silva / Telefone: 123 / Empresa: Empresa X / Email: joao.silva@example.com")

    def test_formatar_json(self):
        """
        Testa se a função formatar_json da classe Config gera corretamente um JSON a partir de um objeto Contato.
        """
        config = Config()

        # Criar um objeto Contato para teste
        contato = Contato(nome="Alice", sobrenome="Silva", telefone="987654321", empresa="Empresa Y", email="alice.silva@example.com")

        resultado = config.formatar_json(contato)

        # Verificar se o JSON gerado está correto
        self.assertEqual(resultado, {
            "nome": "Alice",
            "sobrenome": "Silva",
            "telefone": "987654321",
            "empresa": "Empresa Y",
            "email": "alice.silva@example.com"
        })

    def test_formatar_contato_diferente(self):
        """
        Testa se a função formatar_contato da classe Config gera resultados diferentes para contatos distintos.
        """
        config = Config()

        contato1 = Contato(nome="Alice", sobrenome="Silva", telefone="987654321", empresa="Empresa Y", email="alice.silva@example.com")
        contato2 = Contato(nome="Bob", sobrenome="Jones", telefone="123456789", empresa="Empresa Z", email="bob.jones@example.com")

        resultado_contato1 = config.formatar_contato(contato1)
        resultado_contato2 = config.formatar_contato(contato2)

        self.assertNotEqual(resultado_contato1, resultado_contato2, "A formatação de contatos diferentes deveria ser diferente.")

    def test_formatar_json_diferente(self):
        """
        Testa se a função formatar_json da classe Config gera resultados diferentes para contatos distintos.
        """
        config = Config()

        contato1 = Contato(nome="Alice", sobrenome="Silva", telefone="987654321", empresa="Empresa Y", email="alice.silva@example.com")
        contato2 = Contato(nome="Bob", sobrenome="Jones", telefone="123456789", empresa="Empresa Z", email="bob.jones@example.com")

        resultado_json1 = config.formatar_json(contato1)
        resultado_json2 = config.formatar_json(contato2)

        self.assertNotEqual(resultado_json1, resultado_json2, "O JSON gerado para contatos diferentes deveria ser diferente.")

    def test_formatar_json_e_contato(self):
        """
        Testa se a função formatar_json e formatar_contato da classe Config geram resultados diferentes para o mesmo contato.
        """
        config = Config()

        contato = Contato(nome="Alice", sobrenome="Silva", telefone="987654321", empresa="Empresa Y", email="alice.silva@example.com")

        resultado_json = config.formatar_json(contato)
        resultado_contato = config.formatar_contato(contato)

        self.assertNotEqual(resultado_json, resultado_contato, "O JSON e a formatação de contato para o mesmo contato deveriam ser diferentes.")

if __name__ == '__main__':
    with open('resultados_testes_config.xml', 'wb') as output:
        runner = xmlrunner.XMLTestRunner(output=output)
        unittest.main(testRunner=runner)
