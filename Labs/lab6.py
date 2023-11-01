#Lab6 Nazli Zamanian Gustavsson
import socket

def main():
    server_ip = '0.0.0.0'  # Listen on all available network interfaces
    server_port = 8080  

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)  # Listen for up to 5 client connections

    print(f"Server is listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Handle the client connection here
        handle_client(client_socket)
           
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

#     client_socket.close()  # Close the client socket

if __name__ == "__main__":
    main()
