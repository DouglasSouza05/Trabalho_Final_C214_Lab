<<<<<<< HEAD
# Trabalho_Final_C214_Lab
echo "Trabalho de C214 Lab"
# Recupera o endereço de e-mail da variável de ambiente
notify-send "Notificação em paralelo rodando" &
=======
to_email="$EMAIL_VARIABLE"
>>>>>>> ab2d804f2f97ba3ad7f28a6d4b6a4f9707a4bd7f

# Executa o job
./job.sh

<<<<<<< HEAD
# Fim do trabalho
echo "Testes finalizados"
sudo apt-get install mailutils
echo "Enviando o e-mail do trabalho C214 Lab" | mail -s "Trabalho C214 Lab" ${EMAIL_LIST}
=======
echo "set smtp-use-starttls" >> ~/.mailrc
echo "set ssl-verify=ignore" >> ~/.mailrc
echo "$body" | mail -s "$subject" "$to_email"
>>>>>>> ab2d804f2f97ba3ad7f28a6d4b6a4f9707a4bd7f
