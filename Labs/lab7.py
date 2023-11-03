#Lab7 Nazli Zamanian Gustavsson

import socket
import select #so we can manage more than one ios and run the same.

# port = 60003
# sockL =socket.socket(socket.AF_INET,socket_STREAM)
# sockL.bind(("", port))
# sockL.listen(1)

# listOfSockets = [sockL]

# print("Listening on port {}".format(port))

# while True:
#     tup = select.socket(listOfSockets, [],[])
#     sock = tup [0] [0]
    
#     if sock ==sockL: 
#         pass
#     # TODO: A new clients connects.
#         # call (sockClient, addr) = sockL.accept() and take care of the new client
#         # add the new socket to listOfSockets
#         # notify all other clients about the new client
        
        
#     else:
#         data = sock.recv(2048)
#        pass
#     # : A client disconnects
#     # close the socket object and remove from listOfSockets
#     # notify all other clients about the disconnected client
# else:
# pass # : A client sends a message
# # data is a message from a client
# # send the data to all client
            

####################

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT =1234

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SQL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list =[server_socket]

clients ={}


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGHT)
        if not len(message_header): # we didnt get a thing
            return False
        
        message_lenght = int (message_header.decode('utf-8').strip())
        return {"header": message_header, "data":client.socket.recv(message_lenght) }
    
    except: #only will be hit if the script is broken
        return False


while True:
    read_sockets, _, exception_sockets = select.select(socket_list, [], sockets_list)
    
    for notified_sockets in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            
            user = receive_message(client_Socket)
            if user is False:
                continue 
           
                sockets_list.append(client_socket)
            
                clients[client_socket] = user
            
                print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username: {user['data'].decode('utf-8')}")
            
            else: 
                message = receive_message(notified_socket)
                
                if message is False:
                    print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                    sockets_list.remove(notified_socket)
                    del clients[notified_socket]
                    continue 
                user = clients[notfied_socket]
                
                print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")
                
                for client_socket in clients:
                    if client_socket != notified_socket:
                        client_socket.send(user['header']+ user['data']+ message['header'] + message['data'])
                        
        for notified_socket in exception_sockets:
            sockets_list.remove(notified_socket)
            del clients[notified_socket]
            
            
            