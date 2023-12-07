from .contatos import Contato
import json
import os

class Gerenciador:
    def __init__(self):
        self.contatos = []

    def add_contato(self, nome, sobrenome, telefone, empresa=None, email=None):
        contato = Contato(nome=nome, sobrenome=sobrenome, telefone=telefone, empresa=empresa, email=email)
        self.contatos.append(contato)
        self.save_contatos()

    def list_contatos(self):
        for contato in self.contatos:
            print((f"Nome: {' '.join(contato.nome.strip().split())} / Sobrenome: {' '.join(contato.sobrenome.strip().split())} / Telefone: {' '.join(contato.telefone.strip().split())} / Empresa: {' '.join(contato.empresa.strip().split())} / Email: {' '.join(contato.email.strip().split())}"))

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
            print()
            print("Contato Removido com Sucesso!")
        else:
            print()
            print("Não Há Nenhum Contato com essas Informações!")

    def save_contatos(self):
        with open("contatos.json", 'w') as lista:
            contatos_json = []

            for contato in self.contatos:
                # Remover espaços extras antes de salvar
                nome = ' '.join(contato.nome.strip().split())
                sobrenome = ' '.join(contato.sobrenome.strip().split())
                telefone = ' '.join(contato.telefone.strip().split())
                empresa = ' '.join(contato.empresa.strip().split())
                email = ' '.join(contato.email.strip().split())

                contato = {
                    "nome": nome,
                    "sobrenome": sobrenome,
                    "telefone": telefone,
                    "empresa": empresa,
                    "email": email
                }
                contatos_json.append(contato)

            json.dump(contatos_json, lista)

            # json.dump([vars(contato) for contato in self.contatos], lista)

    def delete_contatos(self):
        try:
            os.remove("contatos.json")
            print("Arquivo 'contatos.json' Removido com Sucesso. \n")
        except FileNotFoundError:
            print("O Arquivo 'contatos.json' Não Existe! \n")

    def arquivo_exist(self, arquivo):
        return os.path.exists(arquivo)