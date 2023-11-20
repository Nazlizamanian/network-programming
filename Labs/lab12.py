#12 Nazli Zamanian Gustavsson

import firebase_admin 
from firebase_admin import  credentials, initialize_app, db 
import tkinter as tk
from tkinter import scrolledtext

# Firebase initialization
json_file_path = "C:\\Users\\nazli\\OneDrive\\Dokument\\University\\yearTwo\\NetworkProgramming\\Labs\\lab12-9e351-firebase-adminsdk-aqemq-dc3cfed443.json"

cred = credentials.Certificate(json_file_path)
firebase_admin.initialize_app(cred, {'databaseURL': 'https://lab12-9e351-default-rtdb.firebaseio.com/'})
ref = db.reference('/messages')


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #-------------------------------------------------------------------
        # row 1: connection stuff (and a clear-messages button)
        #-------------------------------------------------------------------
        self.groupCon = tk.LabelFrame(bd=0)
        self.groupCon.pack(side="top")
        #
        self.connectButton = tk.Button(self.groupCon, text='connect',
                                       command=self.connectButtonClick, width=10)
        self.connectButton.pack(side="left")
        #
        padder = tk.Label(self.groupCon, padx=1)
        padder.pack(side="left")
        #
        self.clearButton = tk.Button(self.groupCon, text='clr msg',
                                     command=self.clearButtonClick)
        self.clearButton.pack(side="left")

        #-------------------------------------------------------------------
        # row 2: the message field (chat messages + status messages)
        #-------------------------------------------------------------------
        self.msgText = scrolledtext.ScrolledText(height=15, width=42,
                                                 state=tk.DISABLED)
        self.msgText.pack(side="top")

        #-------------------------------------------------------------------
        # row 3: sending messages
        #-------------------------------------------------------------------
        self.groupSend = tk.LabelFrame(bd=0)
        self.groupSend.pack(side="top")
        #
        self.textIn = tk.Entry(self.groupSend, width=38)
        # if the focus is on this text field and you hit 'Enter',
        # it should (try to) send
        self.textIn.bind('<Return>', self.sendButtonClick)
        self.textIn.pack(side="left")
        #
        padder = tk.Label(self.groupSend, padx=5)
        padder.pack(side="left")
        #
        self.sendButton = tk.Button(self.groupSend, text='send',
                                    command=self.sendButtonClick)
        self.sendButton.pack(side="left")

    def clearButtonClick(self):
        self.msgText.configure(state=tk.NORMAL)
        self.msgText.delete(1.0, tk.END)
        self.msgText.see(tk.END)
        self.msgText.configure(state=tk.DISABLED)

    def connectButtonClick(self):
        # Subscribe to Firebase updates
        self.message_stream = ref.listen(self.stream_handler)
        self.printToMessages("Connected to Firebase")

    def disconnect(self):
        # Unsubscribe from Firebase updates
        self.message_stream.close()
        self.printToMessages("Disconnected")

    def tryToConnect(self):
        pass

    def sendMessage(self, _):
        message = self.textIn.get()
        new_message = {'name': 'Your Name', 'text': message}
        ref.push(new_message)
        self.printToMessages(f"Sent: {message}")

    def stream_handler(self, incoming_data):
        if incoming_data.event_type == 'put':
            if incoming_data.path == '/':
                if incoming_data.data is not None:
                    for key in incoming_data.data:
                        message = incoming_data.data[key]
                        self.handle_message(message)
            else:
                message = incoming_data.data
                self.handle_message(message)

    def handle_message(self, message):
        name = message.get('name', 'Unknown')
        text = message.get('text', '')
        formatted_message = f"{name}: {text}"
        self.printToMessages(formatted_message)

    def printToMessages(self, message):
        self.msgText.configure(state=tk.NORMAL)
        self.msgText.insert(tk.END, message + '\n')
        self.msgText.see(tk.END)
        self.msgText.configure(state=tk.DISABLED)

if __name__ == "__main__":
    g_root = tk.Tk()
    g_app = Application(master=g_root)
    g_app.mainloop()
