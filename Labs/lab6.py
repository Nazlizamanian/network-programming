# #Lab6 Nazli Zamanian Gustavsson
import socket
#http://localhost:8080/blub/blib.html. 
#http://localhost:8080/

def create_response_html(request):
    response = """
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {}

<html>
<head>
    <title>Request Description</title>
</head>
<body>
    <h1>Your browser made the following request: </h1>
    <pre>{}</pre>
</body>
</html>
""".format(len(request), request)

    return response

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connection from {client_address}")

                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break

                # Extract the request from the client's data
                request = data.split('\n\n', 1)[-1]

                response = create_response_html(request)

                client_socket.sendall(response.encode('utf-8'))

if __name__ == '__main__':
    host = '127.0.0.1' 
    port = 8080 

    start_server(host, port)


########################################################################
# def handle_client(client_socket):
#     request = client_socket.recv(1024).decode('utf-8')

#     if request:
#         # Prepare the response headers
#         response = "HTTP/1.1 200 OK\r\n"
#         response += "Content-Type: text/html\r\n\r\n"
        
#         # Create an HTML response with the client's request
#         response += "<html><pre>"
#         response += "<h1 style='font-family: Times New Roman'> Your browser sent the following request: </h1>"
#         response += request 
#         response += "</pre></html>"

#         # Send the response to the client
#         client_socket.send(response.encode('utf-8'))
    
#     client_socket.close()

# def main():
#     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server.bind(('localhost', 8080))
#     server.listen(3)  

#     print("Listening on http://localhost:8080/blub/blib.html.")

#     while True:
#         client_socket, client_address = server.accept()
#         print(f"Accepted connection from {client_address}")
#         handle_client(client_socket)

# if __name__ == "__main__":
#     main()


