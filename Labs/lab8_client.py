#Lab 8 Nazli Zamanian Gustavsson 
#extended on lab7. 
import socket
import select
import errno
import sys
import tkinter as tk


HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT = 1234

class ChatClient:
    def __init__(self, root, my_username):
        self.my_username = my_username
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((IP, PORT))
        self.client_socket.setblocking(False)

        self.root = root
        self.root.title(f"Chat - {my_username}")

        self.message_entry = tk.Entry(self.root)
        self.message_entry.pack()
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()
        self.message_display = tk.Text(self.root)
        self.message_display.pack()

        self.username = my_username.encode("utf-8")
        self.username_header = f"{len(self.username):<{HEADER_LENGTH}}".encode("utf-8")
        self.client_socket.send(self.username_header + self.username)

        self.message_queue = []

        self.root.after(200, self.poll_messages)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            message = message.encode("utf-8")
            message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8")
            self.client_socket.send(message_header + message)
            self.message_entry.delete(0, tk.END)

    def poll_messages(self):
        try:
            while True:
                username_header = self.client_socket.recv(HEADER_LENGTH)
                if not len(username_header):
                    printToMessages("Connection closed by the server")
                    self.root.quit()
                    return

                username_length = int(username_header.decode("utf-8").strip())
                username = self.client_socket.recv(username_length).decode("utf-8")

                message_header = self.client_socket.recv(HEADER_LENGTH)
                message_length = int(message_header.decode("utf-8").strip())
                message = self.client_socket.recv(message_length).decode("utf-8")

                self.message_queue.append(f"{username} > {message}")

        except IOError as e:
            if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                printToMessages('Reading error', str(e))
                self.root.quit()

        except Exception as e:
            printToMessages('General error', str(e))
            self.root.quit()

        if len(self.message_queue) > 0:
            self.print_to_messages(self.message_queue.pop(0))

        self.root.after(200, self.poll_messages)

    def print_to_messages(self, message):
        self.message_display.insert(tk.END, message + '\n')

    def printToMessages(self, message):
        self.root.after(0, self.print_to_messages, message)

root = tk.Tk()
my_username = input("Username: ")
client = ChatClient(root, my_username)
root.mainloop()
