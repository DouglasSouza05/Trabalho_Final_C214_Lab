from Agenda.contatos import Contato
from Agenda.gerenciador import Gerenciador

class Main:
    def run(self):
        # Exemplos de uso do construtor
        contato1 = Contato(nome="João", sobrenome="Silva", telefone="123456789")
        contato2 = Contato(nome="Maria", sobrenome="Souza", telefone="987654321")
        contato3 = Contato(nome="Carlos", sobrenome="Ferreira", telefone="987654321", empresa="XYZ Ltda")

        # Imprimir informações dos contatos
        # self.info_contatos(contato1)
        # self.info_contatos(contato2)
        # self.info_contatos(contato3)

        gerenciador = Gerenciador()

        gerenciador.add_contato("João", "Silva", "123456789")
        gerenciador.add_contato("Maria", "Souza", "987654321")

        gerenciador.all_contatos()

        gerenciador.remove_contato("Maria", "Souza")

        gerenciador.all_contatos()

        gerenciador.add_contato("Carlos", "Ferreira", "147258369", "XYZ Ltda")

        gerenciador.all_contatos()

        contato = gerenciador.search_contato(nome="Carlos", sobrenome="Ferreira")

        if contato:
            print("----------------------------------------------------------------------------------")
            print(f"Nome: {contato.nome}, Sobrenome: {contato.sobrenome}, Telefone: {contato.telefone}, Empresa: {contato.empresa}, Email: {contato.email}")
        else:
            "Contato não foi encontrado na Agenda!"

        gerenciador.remove_contato("João", "Silva")

    # def info_contatos(self, contato):
    #     print(f"Nome: {contato.nome}, Sobrenome: {contato.sobrenome}, Telefone: {contato.telefone}, Empresa: {contato.empresa}, Email: {contato.email}")

# Instanciar e executar a classe Main
if __name__ == "__main__":
    main_instance = Main()
    main_instance.run()