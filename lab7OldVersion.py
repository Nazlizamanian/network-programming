

# host = ''
# port = 55555

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind((host, port))
# server.listen()

# clients = []
# nicknames = []

# def broadcast(message ): #broadcasting a message
#     for client in clients:
#         client.send(message)
        
# def handle(client):
#     while True:
#         try:
#             message = client.recv(1024)
#             broadcast(message)
#         except:
#             index = clients.index(client)
#             clients.remove(client)
#             client.close()
#             nickname = nicknames[index]
#             broadcast(f'{nickname} left the chat!'.encode('ascii'))
#             nicknames.remove(nickname)
#             break
            
            
# def receive():
#     while True: 
#         client, address = server.accept()
#         print(f"Connected with {str(address)}")
        
#         ip, port = address 
        
#         client.send('NICK'.encode('ascii'))
#         nickname = client.recv(1024).decode('ascii')
#         nicknames.append(nickname)
#         clients.append(client)
        
#         print(f'Nickname of the client is {nickname}!')
        
#         message = f"[{ip}:{port}] (connected)"
#         broadcast(message.encode('ascii'), client)
        
#         broadcast(f'{nickname} joined the chat!.'.encode('ascii'))
#         client.send('Connected to the server!'.encode('ascii'))
        
#         thread = threading.Thread(target=handle, args=(client,))
#         thread.start()

# print("Server is listening...")
# receive()


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

sockets_list = [server_socket]

clients = {}

def broadcast_message(message, sender_socket=None):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                pass

def send_message_to_all_clients(message, exclude_client=None):
    for client_socket in clients:
        if client_socket != exclude_client:
            try:
                client_socket.send(message)
            except:
                pass


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            return False

        message_length = int(message_header.decode('utf-8').strip())
        return {"header": message_header, "data": client_socket.recv(message_length)}

    except:  # This will only be hit if the script is broken
        return False

while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()

            user = receive_message(client_socket)
            if user is False:
                continue

            sockets_list.append(client_socket)
            clients[client_socket] = user

            connected_message = f"[{client_address[0]}:{client_address[1]}] (connected)\n".encode('utf-8')
            
            send_message_to_all_clients(connected_message, exclude_client=client_socket)
            
            sockets_list.append(client_socket)
            clients[client_socket] = user

            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username: {user['data'].decode('utf-8')}")

        else:
            message = receive_message(notified_socket)

            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}")
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
            else:
                user = clients[notified_socket]

                print(f"Received message from {user['data'].decode('utf-8')}: {message['data'].decode('utf-8')}")

                
    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]

###################################################################################### CLient 
# nickname = input("Choose a nickname: ")
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('127.0.0.1', 55555))
# client.send(nickname.encode('ascii'))

# def receive():
#     while True:
#         try:
#             message = client.recv(1024).decode('ascii')
#             if message == 'NICK':
#                 client.send(nickname.encode('ascii'))
#                 pass 
#             else:
#                 print(message)
#         except:
#             print('Error occured!')
#             client.close()
#             break

# def write():
#     while True:
#         message = f'{nickname}: {input("")}'    
#         client.send(message.encode('ascii'))
        
# receive_thread= threading.Thread(target= receive)
# receive_thread.start()

# write_thread = threading.Thread(target=write)
# write_thread.start()


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8")
client_socket.send(username_header + username)

while True:
    message = input(f"{my_username} > ")

    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
        client_socket.send(message_header + message)

    try:
        while True:
            # receive things
            username_header = client_socket.recv(HEADER_LENGTH)
            if not len(username_header):
                print("Connection closed by the server")
                sys.exit()
            username_length = int(username_header.decode("utf-8").strip())
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('General error', str(e))
        sys.exit()
        
        
        
        