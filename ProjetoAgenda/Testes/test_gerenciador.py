import os, sys
import unittest
import xmlrunner

# Obtém o caminho do diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtém o caminho do diretório "ProjetoAgenda"
projeto_agenda_dir = os.path.abspath(os.path.join(script_dir, ".."))

# Adiciona o diretório "ProjetoAgenda" ao caminho do Python
sys.path.append(projeto_agenda_dir)

from Agenda.gerenciador import Gerenciador


class TestGerenciador(unittest.TestCase):

    def setUp(self):
        # Cria um gerenciador para uso nos testes
        self.gerenciador = Gerenciador()

    def test_adicionar_contato(self):
        self.gerenciador.add_contato("João", "Silva", "123456789", "EmpresaX", "joao.silva@email.com")
        self.assertEqual(len(self.gerenciador.contatos), 1, "O contato não foi adicionado corretamente.")

    def test_listar_contatos(self):
        contatos_iniciais = len(self.gerenciador.contatos)
        self.gerenciador.list_contatos()
        self.assertEqual(len(self.gerenciador.contatos), contatos_iniciais, "A lista de contatos não deveria ser modificada ao listar.")

    def test_pesquisar_contato_existente(self):
        self.gerenciador.add_contato("Maria", "Oliveira", "987654321", "EmpresaY", "maria.oliveira@email.com")
        contato = self.gerenciador.search_contato("Maria", "Oliveira")
        self.assertIsNotNone(contato, "O contato existente não foi encontrado.")

    def test_pesquisar_contato_inexistente(self):
        contato = self.gerenciador.search_contato("Inexistente", "Contato")
        self.assertIsNone(contato, "Um contato inexistente foi encontrado.")

    def test_remover_contato_existente(self):
        self.gerenciador.add_contato("Alice", "Silva", "111111111", "EmpresaZ", "alice.silva@email.com")
        contatos_iniciais = len(self.gerenciador.contatos)
        self.gerenciador.remove_contato("Alice", "Silva")
        self.assertEqual(len(self.gerenciador.contatos), contatos_iniciais - 1, "O contato existente não foi removido corretamente.")

    def test_remover_contato_inexistente(self):
        contatos_iniciais = len(self.gerenciador.contatos)
        self.gerenciador.remove_contato("Inexistente", "Contato")
        self.assertEqual(len(self.gerenciador.contatos), contatos_iniciais, "A lista de contatos não deveria ser modificada ao remover um contato inexistente.")

if __name__ == '__main__':
    unittest.main()
