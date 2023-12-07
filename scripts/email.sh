#!/bin/bash

# Recupera o endereço de e-mail da variável de ambiente
to_email="$YOUR_EMAIL_VARIABLE"

subject="Pipeline terminou"
body="Pipeline do projeto de C214 terminou"

# Use o comando mail para enviar o e-mail
echo "$body" | mail -s "$subject" "$to_email"