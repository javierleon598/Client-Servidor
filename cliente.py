#+----------------------------------+
#| Client                           |
#+----------------------------------+
import socket
#       CONFIGURATION
host = '127.0.0.1'
port = 9879
buffer_size = 1024
#Creo el  objeto socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#invoco  el metodo connect del socket pasando como parametro la tupla IP , puerto
mysocket.connect((host, port))

while  True:
    mensaje = input("Mensaje  a enviar: ").encode('utf-8')
    #invoco  el metodo send pasando como parametro el string ingresado por el  usuario
    mysocket.send(mensaje)
    if  mensaje.decode('utf8') == "exit":
        break
    data = mysocket.recv(buffer_size)
    print("Server Response:", data.decode('utf8'))

print("Adios")

#cierro socket
mysocket.close()
