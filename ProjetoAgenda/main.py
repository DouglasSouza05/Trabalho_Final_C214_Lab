from Agenda.config import Config
from Agenda.gerenciador import Gerenciador


class Main:
    def __init__(self):
        self.gerenciador = Gerenciador()

    def exibir_menu(self):

        while True:
            print("\n------- MENU -------\n")
            print("1. Adicionar Contato na Agenda.")
            print("2. Listar Contatos da Agenda.")
            print("3. Pesquisar Contato Específico.")
            print("4. Remover Contato Específico.")
            print("5. Deletar Agenda de Contatos.")
            print("6. Sair... \n")

            escolha = input("Escolha uma opção (1-6): ")

            if escolha == "1":
                self.adicionar_contato()
            elif escolha == "2":
                self.listar_contatos()
            elif escolha == "3":
                self.pesquisar_contato()
            elif escolha == "4":
                self.remover_contato()
            elif escolha == "5":
                self.deletar_agenda()
            elif escolha == "6":
                print()
                print("Saindo do programa. Até mais!")
                break
            else:
                print()
                print("Escolha inválida. Tente novamente.")

    def adicionar_contato(self):

        nome = input("\nDigite o Nome: ")
        sobrenome = input("Digite o Sobrenome: ")
        telefone = input("Digite o Telefone: ")

        flag_empresa = input("Deseja Adicionar o Nome de uma Empresa? (s/n): ")
        empresa = input("Digite a Empresa: ") if flag_empresa.lower() == "s" else "None"

        flag_email = input("Deseja Adicionar o Email? (s/n): ")
        email = input("Digite o Email: ") if flag_email.lower() == "s" else "None"
        print()

        self.gerenciador.add_contato(nome, sobrenome, telefone, empresa, email)
        print("Contato Adicionado com Sucesso! Agenda Salva.")

    def listar_contatos(self):

        config = Config()

        print("\n------- LISTA DE CONTATOS -------\n")
        contatos = self.gerenciador.list_contatos()

        if not contatos:
            print("Não Há Contatos Salvos na Agenda!")
        else:
            for contato in contatos:
                print(config.formatar_contato(contato))

    def pesquisar_contato(self):

        config = Config()

        nome = input("\nDigite o Nome do Contato: ")
        sobrenome = input("Digite o Sobrenome do Contato: ")

        contato = self.gerenciador.search_contato(nome, sobrenome)

        if contato:
            print("\n------- CONTATO ENCONTRADO -------\n")
            print(config.formatar_contato(contato))
        else:
            print("\nContato Não Encontrado na Agenda!")

    def remover_contato(self):

        nome = input("\nDigite o Nome do Contato a ser Removido: ")
        sobrenome = input("Digite o Sobrenome do Contato a ser Removido: ")

        contato = self.gerenciador.remove_contato(nome, sobrenome)

        if contato:
            print()
            print("Contato Removido com Sucesso!")
        else: 
            print()
            print("Não Há Nenhum Contato com essas Informações!")

    def deletar_agenda(self):

        print()
        arquivo = "contatos.json"

        if self.gerenciador.arquivo_exist(arquivo):
            confirmacao = input("Tem Certeza de que Deseja Excluir Todos os Contatos? (s/n): ")
            print()
            if confirmacao.lower() == "s":
                self.gerenciador.delete_contatos()
                self.gerenciador.contatos = []
                print("Arquivo 'contatos.json' Removido com Sucesso. \n")
                print("Todos os Contatos Foram Excluídos.")
            else:
                print("Operação Cancelada.")
        else:
            print(f"O Arquivo {arquivo} Não Existe.")

if __name__ == "__main__":
    menu = Main()
    menu.exibir_menu()