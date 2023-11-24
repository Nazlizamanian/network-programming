#Lab8 Nazli Zamanian Gustavsson
import socket
import select

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 60003))
server_socket.listen()

clients = [server_socket]

print('Server listening on port 60003...')

while True:
    # Use select to handle multiple connections
    readable, _, _ = select.select(clients, [], [])

    for sock in readable:
        if sock == server_socket:
            # New client connection
            client_socket, client_address = server_socket.accept()
            clients.append(client_socket)
            print(f"New connection from {client_address}")
            
            # Broadcast a welcome message to all clients
            welcome_message = f"Client {client_address} joined the chat"
            for client in clients[1:]:
                client.sendall(welcome_message.encode())
        else:
            # Incoming data from a client
            data = sock.recv(1024)
            if not data:
                # Client disconnected
                print(f"{client_address} Client {sock.getpeername()} disconnected")
                sock.close()
                clients.remove(sock)
                
                # Broadcast a leave message to all clients
                leave_message = f"Client {sock.getpeername()} left the chat"
                for client in clients[1:]:
                    client.sendall(leave_message.encode())
            else:
                # Broadcast the message to all clients
                print(f"Received: {data.decode()}")
                for client in clients[1:]:
                    client.sendall(data)

# Close the server socket
server_socket.close()
