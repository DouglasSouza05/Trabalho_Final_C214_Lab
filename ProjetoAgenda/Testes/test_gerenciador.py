# ProjetoAgenda/Testes/test_gerenciador.py

import pytest
import json
from unittest.mock import patch, MagicMock
from ProjetoAgenda.Agenda.gerenciador import Gerenciador, Contato, Config

@pytest.fixture
def gerenciador_com_contatos(tmp_path):
    gerenciador = Gerenciador(config=Config(contatos_file=tmp_path / "contatos.json"))
    gerenciador.add_contato(nome="João", sobrenome="Silva", telefone="123456789", empresa="ABC LTDA", email="joao.silva@example.com")
    gerenciador.add_contato(nome="Maria", sobrenome="Souza", telefone="987654321", empresa="XYZ S/A", email="maria.souza@example.com")
    return gerenciador

def test_add_contato():
    gerenciador = Gerenciador()
    gerenciador.add_contato(nome="João", sobrenome="Silva", telefone="123456789", empresa="ABC LTDA", email="joao.silva@example.com")
    assert len(gerenciador.contatos) == 1

def test_list_contatos(capsys, gerenciador_com_contatos):
    gerenciador_com_contatos.list_contatos()
    captured = capsys.readouterr()
    assert "João Silva" in captured.out
    assert "Maria Souza" in captured.out

@patch("builtins.open", new_callable=MagicMock)
def test_save_contatos(mock_open, gerenciador_com_contatos):
    with patch("ProjetoAgenda.Agenda.gerenciador.Config.formatar_contato", return_value={"nome": "João", "sobrenome": "Silva"}):
        with patch("builtins.open", mock_open):
            gerenciador_com_contatos.save_contatos()

    mock_open.assert_called_once_with(gerenciador_com_contatos.config.contatos_file, "w")
    mock_open.return_value.__enter__.return_value.write.assert_called_once()

def test_save_contatos_integration(tmp_path, gerenciador_com_contatos):
    contatos_file = tmp_path / "contatos_integration.json"
    gerenciador = Gerenciador(config=Config(contatos_file=contatos_file))
    gerenciador.add_contato(nome="João", sobrenome="Silva", telefone="123456789", empresa="ABC LTDA", email="joao.silva@example.com")
    gerenciador.save_contatos()

    with open(contatos_file, "r") as file:
        saved_data = json.load(file)

    assert len(saved_data) == 1
    assert saved_data[0]["nome"] == "João"
    assert saved_data[0]["sobrenome"] == "Silva"
    assert saved_data[0]["telefone"] == "123456789"
    assert saved_data[0]["empresa"] == "ABC LTDA"
    assert saved_data[0]["email"] == "joao.silva@example.com"
