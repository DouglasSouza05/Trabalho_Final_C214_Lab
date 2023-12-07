# test_gerenciador.py
import pytest
import json
from unittest.mock import patch, MagicMock
from ProjetoAgenda.Agenda.gerenciador import Gerenciador, Contato, Config

@pytest.fixture
def gerenciador_com_contatos():
    gerenciador = Gerenciador()
    gerenciador.add_contato(nome="John", sobrenome="Doe", telefone="123456789", empresa="ABC Inc.", email="john.doe@example.com")
    gerenciador.add_contato(nome="Jane", sobrenome="Doe", telefone="987654321", empresa="XYZ Corp.", email="jane.doe@example.com")
    return gerenciador

def test_add_contato():
    gerenciador = Gerenciador()
    gerenciador.add_contato(nome="John", sobrenome="Doe", telefone="123456789", empresa="ABC Inc.", email="john.doe@example.com")
    assert len(gerenciador.contatos) == 1

def test_list_contatos(capsys, gerenciador_com_contatos):
    gerenciador_com_contatos.list_contatos()
    captured = capsys.readouterr()
    assert "Nome: John / Sobrenome: Doe / Telefone: 123456789 / Empresa: ABC Inc. / Email: john.doe@example.com" in captured.out
    assert "Nome: Jane / Sobrenome: Doe / Telefone: 987654321 / Empresa: XYZ Corp. / Email: jane.doe@example.com" in captured.out

def test_search_contato(gerenciador_com_contatos):
    contato = gerenciador_com_contatos.search_contato(nome="John", sobrenome="Doe")
    assert isinstance(contato, Contato)
    assert contato.nome == "John"
    assert contato.sobrenome == "Doe"

def test_remove_contato(gerenciador_com_contatos, capsys):
    gerenciador_com_contatos.remove_contato(nome="John", sobrenome="Doe")
    assert len(gerenciador_com_contatos.contatos) == 1
    captured = capsys.readouterr()
    assert "Contato Removido com Sucesso!" in captured.out

@patch("builtins.open", new_callable=MagicMock)
def test_save_contatos(mock_open, gerenciador_com_contatos):
    mock_file = MagicMock()
    mock_open.return_value.__enter__.return_value = mock_file

    gerenciador_com_contatos.save_contatos()

    mock_open.assert_called_once_with("contatos.json", "w")
    mock_file.write.assert_called_once()

    # Verifica o que seria escrito no arquivo
    expected_content = json.dumps([{"nome": "John", "sobrenome": "Doe", "telefone": "123456789", "empresa": "ABC Inc.", "email": "john.doe@example.com"},
                                   {"nome": "Jane", "sobrenome": "Doe", "telefone": "987654321", "empresa": "XYZ Corp.", "email": "jane.doe@example.com"}], indent=2)
    mock_file.write.assert_called_once_with(expected_content)

@patch("os.remove")
def test_delete_contatos(mock_remove, gerenciador_com_contatos):
    gerenciador_com_contatos.delete_contatos()
    mock_remove.assert_called_once_with("contatos.json")

def test_arquivo_exist(gerenciador_com_contatos):
    assert gerenciador_com_contatos.arquivo_exist("contatos.json")

def test_arquivo_nao_exist(gerenciador_com_contatos):
    assert not gerenciador_com_contatos.arquivo_exist("arquivo_inexistente.json")
