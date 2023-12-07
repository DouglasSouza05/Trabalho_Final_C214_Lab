# ProjetoAgenda/Testes/test_gerenciador.py

import pytest
import json
from unittest.mock import patch, MagicMock
from ProjetoAgenda.Agenda.gerenciador import Gerenciador, Config

def test_add_contato():
    gerenciador = Gerenciador()
    gerenciador.add_contato(nome="João", sobrenome="Silva", telefone="123456789", empresa="ABC LTDA", email="joao.silva@example.com")
    assert len(gerenciador.contatos) == 1

def test_list_contatos(capsys):
    gerenciador = Gerenciador()
    gerenciador.add_contato(nome="João", sobrenome="Silva", telefone="123456789", empresa="ABC LTDA", email="joao.silva@example.com")
    
    gerenciador.list_contatos()
    captured = capsys.readouterr()
    assert "João Silva" in captured.out

@patch("builtins.open", new_callable=MagicMock)
def test_save_contatos(mock_open):
    gerenciador = Gerenciador()
    gerenciador.add_contato(nome="João", sobrenome="Silva", telefone="123456789", empresa="ABC LTDA", email="joao.silva@example.com")

    with patch("ProjetoAgenda.Agenda.gerenciador.Config.formatar_contato", return_value={"nome": "João", "sobrenome": "Silva"}):
        with patch("builtins.open", mock_open):
            gerenciador.save_contatos()

    mock_open.assert_called_once_with(gerenciador.config.contatos_file, "w")
    mock_open.return_value.__enter__.return_value.write.assert_called_once()
