#Lab6 Nazli Zamanian Gustavsson
import socket

def extract_headers(request_data, headers_to_extract):
    extracted_headers = {}
    lines = request_data.split('\n')
    for line in lines:
        for header in headers_to_extract:
            if line.startswith(header):
                extracted_headers[header] = line[len(header):].strip()
    return extracted_headers

def serve_html_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return f"""HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

{content}"""
    except FileNotFoundError:
        return """HTTP/1.1 404 Not Found

<html>
<body>
<h1>404 Not Found</h1>
<p>The requested resource could not be found.</p>
</body>
</html>
"""

def handle_client(client_socket):
    request_data = client_socket.recv(4096).decode('utf-8')
    print(request_data)

    headers_to_extract = [
        'GET',
        'Host:',
        'User-Agent:',
        'Accept:',
        'Accept-Language:',
        'Accept-Encoding:',
        'Connection:',
        'Upgrade-Insecure-Requests:'
    ]

    extracted_headers = extract_headers(request_data, headers_to_extract)

    # Check if the request is for a specific resource (e.g., blib.html)
    if "blib.html" in request_data:
        response = serve_html_file("blib.html")
    else:
        # Create a generic response with extracted headers
        response = """HTTP/1.1 200 OK
Content-Type: text/html; charset=utf-8

<html>
<body>
<h1>Your browser sent the following request: </h1>
<pre>
{}
</pre>
</body>
</html>
""".format("\n".join(["{} {}".format(key, value) for key, value in extracted_headers.items()]))

    client_socket.send(response.encode('utf-8'))
    client_socket.close()

def main():
    server_ip = '0.0.0.0'  # Listen on all available network interfaces
    server_port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(3)

    print(f"Server is listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Handle the client connection here
        handle_client(client_socket)

if __name__ == '__main__':
    main()


#6.1 
# def handle_client(client_socket):
#     headers_to_print = [
#         "Host", "User-Agent", "Accept", "Accept-Language",
#         "Accept-Encoding", "Connection", "Upgrade-Insecure-Requests", "Cache-Control"
#     ]

#     request = client_socket.recv(1024)  # Receive data from the client
#     if request:
#         text = request.decode('utf-8')  # Decode the byte-array to a string

#         # Split the request into lines
#         request_lines = text.split('\r\n')

#         # The first line contains the request method, path, and HTTP version
#         first_line = request_lines[0]
#         print(f"Request Line: {first_line}")

#         # Create a set to keep track of printed headers for each header
#         printed_headers = {header: False for header in headers_to_print}

#         # Loop through the headers in the specified order
#         for line in request_lines:
#             for header in headers_to_print:
#                 if line.startswith(header) and not printed_headers[header]:
#                     print(line)
#                     printed_headers[header] = True

  # client_socket.close()  # Close the client socket

# import socket

# def extract_headers(request_data, headers_to_extract):
#     extracted_headers = {}
#     lines = request_data.split('\n')
#     for line in lines:
#         for header in headers_to_extract:
#             if line.startswith(header):
#                 extracted_headers[header] = line[len(header):].strip()
#     return extracted_headers

# def serve_html_file(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             return f"""HTTP/1.1 200 OK
# Content-Type: text/html; charset=utf-8

# {content}"""
#     except FileNotFoundError:
#         return """HTTP/1.1 404 Not Found

# <html>
# <body>
# <h1>404 Not Found</h1>
# <p>The requested resource could not be found.</p>
# </body>
# </html>
# """

# def handle_client(client_socket):
#     request_data = client_socket.recv(4096).decode('utf-8')
#     print(request_data)

#     headers_to_extract = [
#         'GET',
#         'Host:',
#         'User-Agent:',
#         'Accept:',
#         'Accept-Language:',
#         'Accept-Encoding:',
#         'Connection:',
#         'Upgrade-Insecure-Requests:'
#     ]

#     extracted_headers = extract_headers(request_data, headers_to_extract)

#     # Check if the request is for a specific resource (e.g., blib.html)
#     if "blib.html" in request_data:
#         response = serve_html_file("blib.html")
#     else:
#         # Create a generic response with extracted headers
#         response = """HTTP/1.1 200 OK
# Content-Type: text/html; charset=utf-8

# <html>
# <body>
# <h1>Your browser sent the following request: </h1>
# <pre>
# {}
# </pre>
# </body>
# </html>
# """.format("\n".join(["{} {}".format(key, value) for key, value in extracted_headers.items()]))

#     client_socket.send(response.encode('utf-8'))
#     client_socket.close()

# def main():
#     server_ip = '0.0.0.0'  # Listen on all available network interfaces
#     server_port = 8080

#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     server_socket.bind((server_ip, server_port))
#     server_socket.listen(3)

#     print(f"Server is listening on {server_ip}:{server_port}")

#     while True:
#         client_socket, client_address = server_socket.accept()
#         print(f"Accepted connection from {client_address}")

#         # Handle the client connection here
#         handle_client(client_socket)

# if __name__ == '__main__':
#     main()
