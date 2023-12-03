#Lab 12 Nazli Zamanian
import tkinter as tk
import tkinter.scrolledtext as tksctxt
import firebase_admin
from firebase_admin import db

#Firebase Initialization
cred = firebase_admin.credentials.Certificate('lab12network-key.json')
url = "https://lab12network-23d3e-default-rtdb.europe-west1.firebasedatabase.app/"
firebase_admin.initialize_app(cred, {'databaseURL': url})
ref = firebase_admin.db.reference('/messages')  # Reference to the 'messages' node in the database

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        self.create_widgets()

    def create_widgets(self): #GUI 
        self.groupCon = tk.LabelFrame(bd=0)
        self.groupCon.pack(side="top")

        self.ipPortLbl = tk.Label(self.groupCon, text='Name', padx=10)
        self.ipPortLbl.pack(side="left")

        self.ipPort = tk.Entry(self.groupCon, width=40)
        self.ipPort.insert(tk.END, url)
        self.ipPort.pack(side="left")

        padder = tk.Label(self.groupCon, padx=5)
        padder.pack(side="left")

        padder = tk.Label(self.groupCon, padx=1)
        padder.pack(side="left")

        self.clearButton = tk.Button(self.groupCon, text='Clear', command=self.clearButtonClick)
        self.clearButton.pack(side="left")

        self.msgText = tksctxt.ScrolledText(height=15, width=42, state=tk.DISABLED)
        self.msgText.pack(side="top")

        self.groupSend = tk.LabelFrame(bd=0)
        self.groupSend.pack(side="top")

        self.textInLbl = tk.Label(self.groupSend, text='Message', padx=10)
        self.textInLbl.pack(side="left")

        self.textIn = tk.Entry(self.groupSend, width=38)
        self.textIn.bind('<Return>', self.sendMessage)
        self.textIn.pack(side="left")

        padder = tk.Label(self.groupSend, padx=5)
        padder.pack(side="left")

        self.sendButton = tk.Button(self.groupSend, text='Send', command=self.sendButtonClick)
        self.sendButton.pack(side="left")

        self.ipPort.focus_set()

        # Start listening to changes in the Firebase 'messages' node
        self.messages_stream = ref.listen(self.streamHandler)

#Event handeling methods 
    def clearButtonClick(self):
        ref.delete()  #deletes all messages in firebase database, by removing the enitre content of /messages node 
        self.msgText.configure(state=tk.NORMAL) #update our states.
        self.msgText.delete(1.0, tk.END)
        self.msgText.configure(state=tk.DISABLED)
        
    def connectButtonClick(self):
        new_url = self.ipPort.get()
        ref.change_database(new_url)
        self.clearButtonClick()  # Clear messages when connecting to a new Firebase database

    def sendButtonClick(self):
        new_message = {'name': 'Nazlis', 'text': self.textIn.get()} #creates a dicitionary with keys name and text, 
        ref.push(new_message) #push message to database under the /message node
        self.handleMessage(new_message) #update our GUI

    def sendMessage(self, event): #if the user presses the Enter keyboard it also sends a message.
        self.sendButtonClick()

    def streamHandler(self, incomingData):
        if incomingData.event_type == 'put': #handles incoming events from the firebase, checks for incoming put event, this occurs when data is added our updated,
            if incomingData.path == '/': # checks that the event is related to the root node /,
                if incomingData.data is not None: #checks that there is actual data coming in.
                    for key in incomingData.data: #iterate through the keys 
                        message = incomingData.data[key]
                        self.handleMessage(message)
        else:
            message = incomingData.data
            self.handleMessage(message)

    def handleMessage(self, message):
        name = message.get('name', 'Unknown')
        text = message.get('text', '')
        display_text = f"{name}: {text}\n"
        self.msgText.configure(state=tk.NORMAL)
        self.msgText.insert(tk.END, display_text)
        self.msgText.see(tk.END)
        self.msgText.configure(state=tk.DISABLED)


def on_closing():
    # Stop listening to changes in the Firebase 'messages' node
    g_app.messages_stream.close()
    g_root.destroy()


g_root = tk.Tk()
g_app = Application(master=g_root)
g_root.protocol("WM_DELETE_WINDOW", on_closing)
g_app.mainloop()