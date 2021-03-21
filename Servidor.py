# *-* coding: utf-8 *-*

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Servidor TCP

ip = "0.0.0.0" # Para deixar mais organizado, vou inserir o IP dentro de uma variável 
port = 777


try:
    server.bind((ip, port)) # O serve.bind está ouvindo na porta 777 no ip genérico 0,0,0,0

    server.listen(5) # vamos passar de fato pra ele ouvir na porta, o 5 e a quantidade de pessoas que pode conectar, geralmente é 5

    print "Listening in " + ip + " port: " + str(port) #Quando der certo, vamos printar que ele esta escultando na porta

    (client_socket, address) = server.accept() # Vamos aceitar a conexão, quando aceitamos ele mostra 2 resultados
    #(<socket._socketobject object at 0x7f5d3d47dad0>, ('127.0.0.1', 47124))
    # O primeiro seria o Client Socket o segundo a porta
   

    print "Received from: " + str(address[0]) # Quando der certo no Accept ele vai printar quem se conectar na porta mostrando o IP da pessoa 

    while True: # Vamos criar uma estrutura de repetição, para que não feche a conexão após a primeira mensagem

        data = client_socket.recv(1024) # Aqui estamos falando que o client socket vai receber dados, mesgagem no caso
        print (data) # vamos mostrar o que recebeu
        client_socket.send("Enviar: ") # E não vamos apenas receber dado, e sim enviar também


    server.close() #Não vamos deixar identado o close no While se não ele fecha


except Exception as erro: # O except é praticamente o Senão, utilizamos o Exception as erro pra mostrar qual erro esta aparecendo depois printamos esse erro
    print str(erro)
    server.close() #Serve pra fechar a conexão
