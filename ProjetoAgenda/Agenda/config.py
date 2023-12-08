class Config: 
    def formatar_contato(self, contato):
        if contato is not None and all(hasattr(contato, attr) for attr in ["nome", "sobrenome", "telefone", "empresa", "email"]):
            return (f"Nome: {' '.join(str(contato.nome).strip().split())} / "
                    f"Sobrenome: {' '.join(str(contato.sobrenome).strip().split())} / "
                    f"Telefone: {' '.join(str(contato.telefone).strip().split())} / "
                    f"Empresa: {' '.join(str(contato.empresa).strip().split())} / "
                    f"Email: {' '.join(str(contato.email).strip().split())}")
        else:
            return ""

    def formatar_json(self, contato):
        if contato is not None and all(hasattr(contato, attr) for attr in ["nome", "sobrenome", "telefone", "empresa", "email"]):
            nome = ' '.join(str(contato.nome).strip().split())
            sobrenome = ' '.join(str(contato.sobrenome).strip().split())
            telefone = ' '.join(str(contato.telefone).strip().split())
            empresa = ' '.join(str(contato.empresa).strip().split())
            email = ' '.join(str(contato.email).strip().split())

            contato_formatado = {
                "nome": nome,
                "sobrenome": sobrenome,
                "telefone": telefone,
                "empresa": empresa,
                "email": email
            }

            return contato_formatado
        else:
            return {}
