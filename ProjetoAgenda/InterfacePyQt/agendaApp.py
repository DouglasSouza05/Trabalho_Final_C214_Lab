import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel

class AgendaApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('APLICATIVO AGENDA DE CONTATOS')
        self.setGeometry(200, 200, 800, 600)

        add_Button = QPushButton("ADICIONAR CONTATO", self)
        add_Button.clicked.connect(self.say_hello)

        vbox = QVBoxLayout()
        vbox.addWidget(add_Button)

        self.setLayout(vbox)

    def say_hello(self):
        print('Olá!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AgendaApp()
    window.show()
    sys.exit(app.exec_())