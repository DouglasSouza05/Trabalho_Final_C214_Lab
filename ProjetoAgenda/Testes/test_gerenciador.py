# ProjetoAgenda/Testes/test_gerenciador.py

import unittest
from unittest.mock import patch
from ProjetoAgenda.Agenda.gerenciador import Gerenciador
from ProjetoAgenda.Agenda.contatos import Contato
import HtmlTestRunner


class TestGerenciador(unittest.TestCase):
    def setUp(self):
        self.gerenciador = Gerenciador()

    def test_search_contato_not_found(self):
        resultado = self.gerenciador.search_contato("Nome", "Sobrenome")
        self.assertIsNone(resultado)

    def test_remove_contato_not_found(self):
        resultado = self.gerenciador.remove_contato("Nome", "Sobrenome")
        self.assertFalse(resultado)

    @patch('os.remove')
    def test_delete_contatos(self, mock_remove):
        self.gerenciador.delete_contatos()
        mock_remove.assert_called_once_with("contatos.json")

    @patch('os.path.exists', return_value=True)
    def test_arquivo_exist(self, mock_exists):
        resultado = self.gerenciador.arquivo_exist("contatos.json")
        self.assertTrue(resultado)

    @patch('os.path.exists', return_value=False)
    def test_arquivo_nao_exist(self, mock_exists):
        resultado = self.gerenciador.arquivo_exist("contatos.json")
        self.assertFalse(resultado)


if __name__ == '__main__':
    # Carregue todos os testes do módulo test_gerenciador
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(test_gerenciador)

    # Crie um runner com HtmlTestRunner
    runner = HtmlTestRunner.HTMLTestRunner(output='test_reports/')

    # Execute os testes usando o runner
    runner.run(suite)