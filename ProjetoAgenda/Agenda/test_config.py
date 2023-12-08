import unittest
from config import Config

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

if __name__ == '__main__':
    unittest.main()
