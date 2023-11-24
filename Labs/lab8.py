#Lab 7 Nazli Zamanian Gustavsson
import socket
import select

port = 60003
sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockL.bind(("", port))
sockL.listen(1)
listOfSockets = [sockL]

print("Listening on port {}".format(port))

while True:
    readable, _, _ = select.select(listOfSockets, [], [])

    for sock in readable: #client wants to connect.
        if sock == sockL:
            sockClient, addr = sockL.accept()
            listOfSockets.append(sockClient)

            # Notify all other clients about the new client
            new_client_msg = "[{}:{}] (connected)\n".format(addr[0], addr[1])
            for client in listOfSockets:
                if client != sockL and client != sockClient:
                    client.send(new_client_msg.encode())

            print("{}:{} connected".format(addr[0], addr[1]))
        else:
            data = sock.recv(2048)
            if not data:
                # A client disconnects
                addr = sock.getpeername()
                sock.close()
                listOfSockets.remove(sock)

                # Notify all other clients about the disconnected client
                disconnected_msg = "[{}:{}] disconnected\n".format(addr[0], addr[1])
                for client in listOfSockets:
                    if client != sockL:
                        client.send(disconnected_msg.encode())

                print("{}:{} disconnected".format(addr[0], addr[1]))
            else:
                # A client sends a message
                addr = sock.getpeername()
                message = "[{}:{}] {}".format(addr[0], addr[1], data.decode())

                # Send the data to all clients except the sender
                for client in listOfSockets:
                    if client != sockL and client != sock:
                        client.send(message.encode())
