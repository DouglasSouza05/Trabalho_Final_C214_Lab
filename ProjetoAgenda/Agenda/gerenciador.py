from .contatos import Contato
import json

class Gerenciador:
    def __init__(self):
        self.contatos = []

    def add_contato(self, contato):
        self.contatos.append(contato)
        self.save_contatos()

    def all_contatos(self):
        return self.contatos

    def search_contato(self, nome, sobrenome):
        pass

    def remove_contato(self, nome, sobrenome):
        pass

    def save_contatos(self):
        pass