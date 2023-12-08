import unittest
from unittest.mock import patch
from gerenciador import Gerenciador

class TestGerenciador(unittest.TestCase):

    def setUp(self):
        self.gerenciador = Gerenciador()

    def test_add_contato(self):
        self.gerenciador.add_contato("João", "Silva", "123456789")
        self.assertEqual(len(self.gerenciador.contatos), 1)

    def test_remove_contato(self):
        self.gerenciador.add_contato("João", "Silva", "123456789")
        self.gerenciador.remove_contato("João", "Silva")
        self.assertEqual(len(self.gerenciador.contatos), 0)

    @patch('builtins.print')
    @patch('os.remove')
    def test_delete_contatos_file_exists(self, mock_remove, mock_print):
        self.gerenciador.delete_contatos()
        mock_remove.assert_called_once_with("contatos.json")

    @patch('builtins.print')
    @patch('os.remove', side_effect=FileNotFoundError())
    def test_delete_contatos_file_not_exists(self, mock_remove, mock_print):
        self.gerenciador.delete_contatos()
        mock_print.assert_called_once_with("O Arquivo 'contatos.json' Não Existe! \n")

    @patch('os.path.exists', return_value=True)
    def test_arquivo_exist_file_exists(self, mock_exists):
        result = self.gerenciador.arquivo_exist("contatos.json")
        self.assertTrue(result)

    @patch('os.path.exists', return_value=False)
    def test_arquivo_exist_file_not_exists(self, mock_exists):
        result = self.gerenciador.arquivo_exist("contatos.json")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
