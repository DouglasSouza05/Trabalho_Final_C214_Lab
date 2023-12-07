class Config:

    def formatar_contato(self, contato):

        return (f"Nome: {' '.join(contato.nome.strip().split())} / "
                f"Sobrenome: {' '.join(contato.sobrenome.strip().split())} / "
                f"Telefone: {' '.join(contato.telefone.strip().split())} / "
                f"Empresa: {' '.join(contato.empresa.strip().split())} / "
                f"Email: {' '.join(contato.email.strip().split())}")
    
    def formatar_json(self, contato):

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

        return contato