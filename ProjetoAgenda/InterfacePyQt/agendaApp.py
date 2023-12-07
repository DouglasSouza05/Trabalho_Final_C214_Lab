import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox
from PyQt5.QtGui import QIntValidator

# Obtém o caminho do diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtém o caminho do diretório "ProjetoAgenda"
projeto_agenda_dir = os.path.abspath(os.path.join(script_dir, ".."))

# Adiciona o diretório "ProjetoAgenda" ao caminho do Python
sys.path.append(projeto_agenda_dir)

from main import Main
from Agenda.gerenciador import Gerenciador
from Agenda.config import Config

class NumerosLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(NumerosLineEdit, self).__init__(parent)
        self.setValidator(QIntValidator(self))

class AgendaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.gerenciador = Gerenciador()

        self.setWindowTitle("Aplicativo Agenda de Contatos")
        self.setGeometry(200, 200, 800, 600)

        # Widgets
        self.label = QLabel("Entre com o Nome, Sobrenome, Telefone, Empresa e Email do Contato, respectivamente. OBs: Empresa e Email são Opcionais!")
        self.nome_input = QLineEdit()
        self.sobrenome_input = QLineEdit()
        self.telefone_input = NumerosLineEdit()
        self.empresa_input = QLineEdit()
        self.email_input = QLineEdit()

        self.result_label = QLabel("Resultado:")
        self.result_text = QTextEdit()
        self.result_text.setReadOnly(True)  # Tornar o QTextEdit somente leitura

        self.adicionar_button = QPushButton("Adicionar Contato", self)
        self.listar_button = QPushButton("Listar Contatos", self)
        self.pesquisar_button = QPushButton("Pesquisar Contato", self)
        self.remover_button = QPushButton("Remover Contato", self)
        self.deletar_button = QPushButton("Deletar Agenda", self)

        # Conectar botões aos métodos correspondentes
        self.adicionar_button.clicked.connect(self.adicionar_contato)
        self.listar_button.clicked.connect(self.listar_contatos)
        self.pesquisar_button.clicked.connect(self.pesquisar_contato)
        self.remover_button.clicked.connect(self.remover_contato)
        self.deletar_button.clicked.connect(self.deletar_agenda)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.nome_input)
        layout.addWidget(self.sobrenome_input)
        layout.addWidget(self.telefone_input)
        layout.addWidget(self.empresa_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.adicionar_button)
        layout.addWidget(self.listar_button)
        layout.addWidget(self.pesquisar_button)
        layout.addWidget(self.remover_button)
        layout.addWidget(self.deletar_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def adicionar_contato(self):
        
        nome = self.nome_input.text()
        sobrenome = self.sobrenome_input.text()
        telefone = self.telefone_input.text()
        empresa = self.empresa_input.text()
        email = self.email_input.text()

        # Verificar se campos obrigatórios estão preenchidos
        if not nome or not sobrenome or not telefone:
            QMessageBox.warning(self, "Aviso", "Por Favor, Preencha Nome, Sobrenome e Telefone. Esses Campos São Obrigatórios!")
            return
        
        if not empresa:
            empresa = "None"

        if not email:
            email = "None"

        self.gerenciador.add_contato(nome, sobrenome, telefone, empresa, email)
        
        # Limpar os campos após adicionar o contato
        self.nome_input.clear()
        self.sobrenome_input.clear()
        self.telefone_input.clear()
        self.empresa_input.clear()
        self.email_input.clear()
        self.result_text.clear()

        self.result_text.append("Contato Adicionado com Sucesso!")

    def listar_contatos(self):
        pass

    def pesquisar_contato(self):

        config = Config()

        nome = self.nome_input.text()
        sobrenome = self.sobrenome_input.text()

        if not nome or not sobrenome:
            QMessageBox.warning(self, "Aviso", "Por Favor, Preencha Nome e Sobrenome para Pesquisar um Contato Específico.")
            return
        
        contato = self.gerenciador.search_contato(nome, sobrenome)

        self.nome_input.clear()
        self.sobrenome_input.clear()
        self.result_text.clear()

        if contato:
            self.result_text.append("------- CONTATO ENCONTRADO -------")
            self.result_text.append("")
            self.result_text.append(config.formatar_contato(contato))
        else:
            self.result_text.append("Contato Não Encontrado na Agenda!")

    def remover_contato(self):

        nome = self.nome_input.text()
        sobrenome = self.sobrenome_input.text()

        if not nome or not sobrenome:
            QMessageBox.warning(self, "Aviso", "Por Favor, Preencha Nome e Sobrenome para Remover um Contato Específico.")
            return
        
        contato = self.gerenciador.remove_contato(nome, sobrenome)

        self.nome_input.clear()
        self.sobrenome_input.clear()
        self.result_text.clear()

        if contato:
            self.result_text.append("------- CONTATO REMOVIDO -------")
        else:
            self.result_text.append("Não Há Nenhum Contato com essas Informações!")

    def deletar_agenda(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AgendaApp()
    window.show()
    sys.exit(app.exec_())