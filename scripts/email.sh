# Trabalho_Final_C214_Lab
echo "Trabalho de C214 Lab"
# Recupera o endereço de e-mail da variável de ambiente
notify-send "Notificação em paralelo rodando" &

# Executa o job
./job.sh

# Fim do trabalho
echo "Testes finalizados"
sudo apt-get install mailutils
echo "Enviando o e-mail do trabalho C214 Lab" | mail -s "Trabalho C214 Lab" ${EMAIL_LIST}
