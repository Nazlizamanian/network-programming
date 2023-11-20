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
    <title>Request </title>
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
                if not data: #if no data is sent we break.
                    break

                request = data.split('\n\n', 1)[-1]# Extract the request from the client's data, split up lines.
                response = create_response_html(request) #calls fun, to generate HTML response based on the request.
                client_socket.sendall(response.encode('utf-8')) #sends the response back to the client.

if __name__ == '__main__':
    host = '127.0.0.1' 
    port = 8080
    start_server(host, port)

