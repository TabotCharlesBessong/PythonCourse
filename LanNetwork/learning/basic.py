print('Hello world')
import socket
connexion_principal = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# lets set up our port 
connexion_principal.bind(('',12800))
# now we need to listen to different events