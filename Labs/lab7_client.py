#Lab 7 Nazli Zamanian Client
import socket
import threading

host = '127.0.0.1'
port = 60003

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(2048)
            if not data:
                print(f"[{host}:{port}] Disconnected from the server.")
                break
            else:
                print(data.decode())
        except socket.error as e:
            # An error occurred or the server closed the connection
            print(f"Error receiving data: {e}")
            break

def run_client():
    sock = socket.socket()
    sock.connect((host, port))
    
    print(f"[{host}:{port}] Connected to the server.")
    
    # Start a thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    receive_thread.start()
    
    try:
        while True:
            message = input()
            sock.send(message.encode())
    except KeyboardInterrupt:
        print(f"Disconnected from the server. [{host}:{port}]")
    finally:
        sock.close()

if __name__ == "__main__":
    run_client()
