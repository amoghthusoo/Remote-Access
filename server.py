import winsound as ws
import socket as s

server_socket = s.socket()
print()
print('Socket Created')
server_socket.bind(('localhost', 9999))
server_socket.listen(1)
print('Waiting for connections')

while True:
    client_socket, address = server_socket.accept()
    print('Connected with', address)
    client_socket.send(bytes('Welcome to Xpert Server', 'utf-8'))
    break


while True:

    flow = client_socket.recv(1024).decode()

    if flow == 'True':
        ws.PlaySound('<example>.wav', ws.SND_ASYNC)   # Edit this line.
        
        
    elif flow == 'False':
        ws.PlaySound(None, ws.SND_PURGE)
        
