#Lab7 Nazli Zamanian Gustavsson
#Server sided 
import socket
import select

IP = "0.0.0.0"  # Listen on all available network interfaces
PORT = 60003
HEADER_LENGTH = 10

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IP, PORT))
server_socket.listen()  

list_of_sockets = [server_socket]
clients = {}

def send_message(client_socket, message):
    try:
        client_socket.send(message)
    except Exception as e:
        print(f"Error sending message: {str(e)}")

def broadcast_message(sender_socket, message):
    for client_socket in clients:
        if client_socket != sender_socket:
            send_message(client_socket, message)

print(f"Listening on {IP}:{PORT}")

while True:
    read_sockets, _, _ = select.select(list_of_sockets, [], [])

    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            # A new client is trying to connect
            client_socket, client_address = server_socket.accept()
            list_of_sockets.append(client_socket)

            # Notify existing clients about the new connection
            for client in clients:
                if client != server_socket:
                    connection_message = f"[{client_address[0]}:{client_address[1]}] (connected)\n".encode('utf-8')
                    send_message(client, connection_message)

            clients[client_socket] = client_address
            print(f"Accepted new connection from {client_address[0]}:{client_address[1]}")

        else:
            # An existing client sent a message
            client_socket = notified_socket
            data = client_socket.recv(2048)

            if not data:
                # Client disconnected
                client_address = clients[client_socket]
                del clients[client_socket]
                list_of_sockets.remove(client_socket)
                disconnect_message = f"[{client_address[0]}:{client_address[1]}] (disconnected)\n".encode('utf-8')
                broadcast_message(client_socket, disconnect_message)
                print(f"Connection from {client_address[0]}:{client_address[1]} closed")
            else:
                # Broadcast the message to all connected clients
                client_address = clients[client_socket]
                message = f"[{client_address[0]}:{client_address[1]}] {data.decode('utf-8')}".encode('utf-8')
                broadcast_message(client_socket, message)
                print(f"Received message from {client_address[0]}:{client_address[1]}: {data.decode('utf-8')}")
