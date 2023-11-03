# #Lab6 Nazli Zamanian Gustavsson

import socket

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')

    if request:
        # Prepare the response headers
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type: text/html\r\n\r\n"
        
        # Create an HTML response with the client's request
        response += "<html><pre>"
        response += "<h1 style='font-family: Times New Roman'> Your browser sent the following request: </h1>"
        response += request 
        response += "</pre></html>"

        # Send the response to the client
        client_socket.send(response.encode('utf-8'))
    
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 8080))
    server.listen(3)  

    print("Listening on http://localhost:8080/blub/blib.html.")

    while True:
        client_socket, client_address = server.accept()
        print(f"Accepted connection from {client_address}")
        handle_client(client_socket)

if __name__ == "__main__":
    main()


