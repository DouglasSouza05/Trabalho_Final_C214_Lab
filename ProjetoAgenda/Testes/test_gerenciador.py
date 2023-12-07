# ProjetoAgenda/Testes/test_gerenciador.py

import pytest
import json
from unittest.mock import patch, MagicMock
from ProjetoAgenda.Agenda.gerenciador import Gerenciador, Config

@pytest.fixture
def gerenciador_com_contatos(tmp_path):
    gerenciador = Gerenciador(config=Config(contatos_file=tmp_path / "contatos.json"))
    gerenciador.add_contato(nome="João", sobrenome="Silva", telefone="123456789", empresa="ABC LTDA", email="joao.silva@example.com")
    return gerenciador

def test_list_contatos(capsys, gerenciador_com_contatos):
    gerenciador_com_contatos.list_contatos()
    captured = capsys.readouterr()
    assert "João Silva" in captured.out

@patch("builtins.open", new_callable=MagicMock)
def test_save_contatos(mock_open, gerenciador_com_contatos):
    with patch("ProjetoAgenda.Agenda.gerenciador.Config.formatar_contato", return_value={"nome": "João", "sobrenome": "Silva"}):
        with patch("builtins.open", mock_open):
            gerenciador_com_contatos.save_contatos()

    mock_open.assert_called_once_with(gerenciador_com_contatos.config.contatos_file, "w")
    mock_open.return_value.__enter__.return_value.write.assert_called_once()
