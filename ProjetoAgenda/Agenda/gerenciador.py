from .contatos import Contato
import json

class Gerenciador:
    def __init__(self):
        self.contatos = []

    def add_contato(self, contato):
        self.contatos.append(contato)
        self.save_contatos()

    def all_contatos(self):
        for contato in self.contatos:
            print("----------------------------------------------------------------------------------")
            print((f"Nome: {contato.nome} / Sobrenome: {contato.sobrenome} / Telefone: {contato.telefone} / Empresa: {contato.empresa} / Email: {contato.email}"))
        print("----------------------------------------------------------------------------------")

    def search_contato(self, nome, sobrenome):
        for contato in self.contatos:
            if contato.nome == nome and contato.sobrenome == sobrenome:
                return contato
        return None

    def remove_contato(self, nome, sobrenome):
        contato = self.search_contato(nome, sobrenome)
        if contato:
            self.contatos.remove(contato)
            self.save_contatos()

    def save_contatos(self):
        with open("contatos.json", 'w') as lista:
            json.dump([vars(contato) for contato in self.contatos], lista)