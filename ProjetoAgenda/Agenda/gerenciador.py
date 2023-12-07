# ProjetoAgenda/Agenda/gerenciador.py

from .contatos import Contato
from .config import Config
import json
import os


class Gerenciador:
    def __init__(self):
        self.contatos = []

    def add_contato(self, nome, sobrenome, telefone, empresa=None, email=None):
        contato = Contato(nome=nome, sobrenome=sobrenome,
                          telefone=telefone, empresa=empresa, email=email)
        self.contatos.append(contato)
        self.save_contatos()

    def list_contatos(self):
        config = Config()

        if not self.contatos:
            print("Não Há Contatos Salvos na Agenda!")
        else:
            for contato in self.contatos:
                print(config.formatar_contato(contato))

    def search_contato(self, nome, sobrenome):

        nome = nome.strip().lower()
        sobrenome = sobrenome.strip().lower()

        for contato in self.contatos:
            if contato.nome.strip().lower() == nome and contato.sobrenome.strip().lower() == sobrenome:
                return contato
        return None

    def remove_contato(self, nome, sobrenome):
        contato = self.search_contato(nome, sobrenome)
        if contato:
            self.contatos.remove(contato)
            self.save_contatos()
            return True
        else:
            return False

    def save_contatos(self):
        try:
            with open("contatos.json", 'w') as file:
                contatos_formatados = [Config.formatar_contato(
                    contato) for contato in self.contatos]
                file.write(json.dumps(contatos_formatados, indent=2))
        except Exception as e:
            print(f"Erro Ao Salvar os Contatos: {e}")

    def delete_contatos(self):
        try:
            os.remove("contatos.json")
            print("Arquivo 'contatos.json' Removido com Sucesso. \n")
        except FileNotFoundError:
            print("O Arquivo 'contatos.json' Não Existe! \n")

    def arquivo_exist(self, arquivo):
        return os.path.exists(arquivo)

    def list_contatos(self):
        config = Config()

        if not self.contatos:
            print("Não Há Contatos Salvos na Agenda!")
        else:
            for contato in self.contatos:
                # Verifica se o contato não é None antes de formatá-lo
                if contato is not None:
                    print(config.formatar_contato(contato))


if __name__ == "__main__":
    menu = Gerenciador()
