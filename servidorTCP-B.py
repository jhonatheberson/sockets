# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES 
# AUTOR: JHONAT HEBERSON AVELINO DE SOUZA
#
# SCRIPT: Servidor de sockets TCP modificado para enviar dados de um arquivo

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 64000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  if sentence == 'obter arquivo.txt':
      file = open('arquivo.txt')
      data = file.read()
      print ('Cliente %s enviou: %s, E Enviando: %s' % (addr, sentence, data))
      connectionSocket.send(data.encode('utf-8')) # envia para o cliente o texto transformado
      connectionSocket.close() # encerra o socket com o cliente
      file.close()
  else:
      print ('Cliente %s enviou: %s, comando não aceito' % (addr, sentence))
      error = 'Comando não aceito, por favor degite "data"'
      serverSocket.sendto(error.encode('utf-8'), addr)     

  
serverSocket.close() # encerra o socket do servidor