#+----------------------------------+
#| Server                           |
#+----------------------------------+
import socket
#       CONFIGURATION
host = '127.0.0.1'
port = 9879
buffer_size = 1024
#Creo el  objeto socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Invoco  al metodo bind, pasando como parametro una tupla con IP y puerto
mysocket.bind((host, port))
#Invoco  el metodo listen para escuchar conexiones con el numero maximo de  conexiones como parametro
mysocket.listen(5)
#El  metodo accept bloquea la ejecucion a la espera de conexiones accept  devuelve un objeto socket y una tupla Ip y puerto
(client, (ip,puerto)) = mysocket.accept()
print("Recibo conexion de " + str(ip) + ":" + str(puerto))

while True:
    recibido = client.recv(1024).decode('utf8')
    if  recibido == "exit":
        client.send(msg)
        break
    print("Client Request:", recibido)
    #Envio  la respuesta al socket cliente
    msg = ("knock knock knock, I'm the server").encode('utf-8')
    client.send(msg)

print("Adios")

# Cierro sockets client and server
client.close()
mysocket.close()
