from unittest.mock import patch
import unittest
import io
from ProjetoAgenda.Agenda.gerenciador import Gerenciador

class TestGerenciador(unittest.TestCase):

    def setUp(self):
        # Este método será chamado antes de cada teste.
        self.gerenciador = Gerenciador()

    def test_add_contato(self):
        # Testa se um contato é adicionado corretamente.
        self.gerenciador.add_contato(nome="John", sobrenome="Doe", telefone="123456789")
        self.assertEqual(len(self.gerenciador.contatos), 1)

    def test_remove_contato(self):
        # Testa se um contato é removido corretamente.
        self.gerenciador.add_contato(nome="John", sobrenome="Doe", telefone="123456789")
        resultado = self.gerenciador.remove_contato(nome="John", sobrenome="Doe")
        self.assertTrue(resultado)
        self.assertEqual(len(self.gerenciador.contatos), 0)

    def test_remove_contato_inexistente(self):
        # Testa a remoção de um contato que não existe.
        resultado = self.gerenciador.remove_contato(nome="Inexistente", sobrenome="Contato")
        self.assertFalse(resultado)

    def test_search_contato(self):
        # Testa se a busca por contato funciona corretamente.
        self.gerenciador.add_contato(nome="John", sobrenome="Doe", telefone="123456789")
        contato_encontrado = self.gerenciador.search_contato(nome="John", sobrenome="Doe")
        self.assertIsNotNone(contato_encontrado)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_contatos(self, mock_stdout):
        # Criar um contato para teste
        self.gerenciador.add_contato("João", "Silva", "123456789")

        # Adicionar um contato None para simular a situação
        self.gerenciador.contatos.append(None)

        # Chamar list_contatos
        self.gerenciador.list_contatos()

        # Obter a saída capturada
        output = mock_stdout.getvalue()

        # Verificar se o contato válido está presente na saída
        self.assertIn("João Silva", output)
        # Verificar se o contato None não causa erros
        self.assertNotIn("NoneType", output)

    def test_delete_contatos(self):
        # Testa se a exclusão do arquivo de contatos funciona corretamente.
        with unittest.mock.patch("os.remove") as mock_remove:
            self.gerenciador.delete_contatos()
            mock_remove.assert_called_once_with("contatos.json")

    def test_arquivo_exist(self):
        # Testa se a verificação de existência de arquivo funciona corretamente.
        with unittest.mock.patch("os.path.exists") as mock_exists:
            mock_exists.return_value = True
            resultado = self.gerenciador.arquivo_exist("arquivo_existente.txt")
            self.assertTrue(resultado)

    def test_arquivo_nao_exist(self):
        # Testa se a verificação de inexistência de arquivo funciona corretamente.
        with unittest.mock.patch("os.path.exists") as mock_exists:
            mock_exists.return_value = False
            resultado = self.gerenciador.arquivo_exist("arquivo_inexistente.txt")
            self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()
