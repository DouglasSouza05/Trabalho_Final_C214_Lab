import unittest.mock
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

    def test_list_contatos(self):
        # Testa se a listagem de contatos funciona corretamente.
        self.gerenciador.add_contato(nome="John", sobrenome="Doe", telefone="123456789")
        # Redireciona a saída padrão para um buffer para capturar a saída do print.
        with unittest.mock.patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
            self.gerenciador.list_contatos()
            output = mock_stdout.getvalue().strip()
        self.assertIn("John Doe", output)

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
