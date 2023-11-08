#Lab 7 Nazli Zamanian Gustavsson
#Client 
import socket

IP = 'localhost'
PORT = 60003

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT ))

while True: 
    message = input('Enter a message to send: ')
    client_socket.send(message.encode('utf-8'))
    data = client_socket.recv(2048)
    print('Recevied message from server: ', data.decode('utf-8'))
    
client_socket.close()