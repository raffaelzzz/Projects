                                                
 # -*- coding: utf-8 -*-

##################################################
#               AUTOR: RAFFAEL BRUNNO            #
#               DATA: 24.12.2020                 #
#               PROGAMA: FAZ REQUISIÇÕES HTTP    #
#                                                #
##################################################


import socket #// Importando o SOCKET

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #// CRIANDO O SOCKET COM ESTRUTURA IPV4 e TCP/IP

client.settimeout(15) #//O TEMPO QUE O CLIENTE VAI SE CONECTAR COM O SERVIDOR (15segundos) SE PASSAR DISSO ELE CANCELA

try: #//Então
    
     client.connect(('hackerdepressivo.com.br', 80))# // CONECTANDO-SE AO SITE NA PORTA 80
      
     print client.send("GET / HTTP/1.1\nHost: hackerdepressivo.com.br\n\n\n")#// MENSAGEM ENVIADA PARA O SERVIDOR

     print client.recv(1024)# // RESPOSTA, 1024 BUFFEROVERFLOW

except:# // SENÃO
    print "A conexão falhou"






