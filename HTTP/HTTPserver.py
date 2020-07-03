# AUTOR: JHONAT HEBERSON AVELINO DE SOUZA
#
# SCRIPT: servidor com metodo GET (python 3)
#

# importacao das bibliotecas
import socket

# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8081 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    # o metodo .recv recebe os dados enviados por um cliente atraves do socket
    request = client_connection.recv(1024)
    # imprime na tela o que o cliente enviou ao servidor
    request = request.decode('utf-8')
    request = request.split(" ")
    print(request)
    if(request[0] == 'GET'):
        file = request[1].split(" ")
        print(file[0][1:])
        if(file[0] == "/"):
            index = open('index.html')
            contend = index.read()
            http_response = """HTTP/1.1 200 OK\r\n\r\n""" + str(contend)
            index.close()
        else: 
            try:
                response = open(file[0][1:])
                contend = response.read()
                http_response = """HTTP/1.1 200 OK\r\n\r\n""" + str(contend)
                response.close()
            except:
                not_found = open("not_found.html")
                contend = not_found.read()
                http_response = """HTTP/1.1 404 Not Found\r\n\r\n""" + contend
                not_found.close()
    else:
        bad_request = open('bad_request.html')
        contend = bad_request.read()
        http_response = """HTTP/1.1 400 Bad Request\r\n\r\n""" + str(contend)
        bad_request.close()
    
    
    # declaracao da resposta do servidor
 
    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
    client_connection.send(http_response.encode('utf-8'))
    # encerra a conexao
    client_connection.close()

# encerra o socket do servidor
listen_socket.close()