# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES 
# AUTOR: JHONAT HEBERSON AVELINO DE SOUZA
#
# SCRIPT: Servidor de sockets UDP modificado para palavra data e receber a data e hora local do servidor
#

# importacao das bibliotecas
from socket import * # sockets
from datetime import datetime

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    message = message.decode('utf-8')
    if message == 'data':
        data = str(datetime.today()) #pegando a hora e data local
        print(data)
        print ('Cliente %s enviou: %s, enviando para cliente: %s' % (clientAddress, message, data))
        serverSocket.sendto(data.encode('utf-8'), clientAddress) 
        # envia a resposta para o cliente
    else:
        print ('Cliente %s enviou: %s, comando não aceito' % (clientAddress, message))
        error = 'Comando não aceito, por favor degite "data"'
        serverSocket.sendto(error.encode('utf-8'), clientAddress) 
serverSocket.close() # encerra o socket do servidor