# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES 
# AUTOR: JHONAT HEBERSON AVELINO DE SOUZA
#
# SCRIPT: Cliente de sockets TCP modificado para enviar dados de um arquivo
#

# importacao das bibliotecas
from socket import *

# definicao das variaveis
serverName = 'localhost' # ip do servidor
serverPort = 64000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

sentence = input('Digite o nome do arquivo para você ler o conteudo, "obter arquivo.txt": ')
clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
modifiedSentence = clientSocket.recv(1024) # recebe do servidor a resposta
print ('O servidor (\'%s\', %d) respondeu com: %s' % (serverName, serverPort, modifiedSentence.decode('utf-8')))
clientSocket.close() # encerramento o socket do cliente
