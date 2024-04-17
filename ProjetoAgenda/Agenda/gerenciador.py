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
        print(self.contatos)
        self.save_contatos()

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
        config = Config()

        try:
            with open("contatos.json", 'w') as file:
                contatos_formatados = [
                    config.formatar_contato(contato) if contato is not None else None for contato in self.contatos
                ]
                contatos_formatados = [c for c in contatos_formatados if c is not None]  # Remove contatos None
                if contatos_formatados:
                    file.write(json.dumps(contatos_formatados, indent=2))
                else:
                    print("Nenhum contato para salvar.")
        except Exception as e:
            print(f"Erro Ao Salvar os Contatos: {e}")

    def delete_contatos(self):
        try:
            os.remove("contatos.json")
        except FileNotFoundError:
            print("O Arquivo 'contatos.json' Não Existe! \n")

    def arquivo_exist(self, arquivo):
        return os.path.exists(arquivo)

if __name__ == "__main__":
    menu = Gerenciador()