class Contato:
    def __init__(self, nome, sobrenome, telefone, empresa=None, email=None):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone
        self.empresa = empresa
        self.email = email

    # Getters
    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.sobrenome

    def get_telefone(self):
        return self.telefone

    def get_empresa(self):
        return self.empresa

    def get_email(self):
        return self.email

    # Setters
    def set_nome(self, nome):
        self.nome = nome

    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def set_telefone(self, telefone):
        self.telefone = telefone

    def set_empresa(self, empresa):
        self.empresa = empresa

    def set_email(self, email):
        self.email = email