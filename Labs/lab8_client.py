#Lab8 Nazli Zamanian using Lab 7 server code
import tkinter as tk
import tkinter.messagebox as tkmsgbox
import tkinter.scrolledtext as tksctxt
import socket

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
        self.ipPortLbl = tk.Label(self.groupCon, text='IP:port', padx=10)
        self.ipPortLbl.pack(side="left")
        #
        self.ipPort = tk.Entry(self.groupCon, width=20)
        self.ipPort.insert(tk.END, 'localhost:60003')
        # if the focus is on this text field and you hit 'Enter',
        # it should (try to) connect
        self.ipPort.bind('<Return>', connectHandler)
        self.ipPort.pack(side="left")
        #
        padder = tk.Label(self.groupCon, padx=5)
        padder.pack(side="left")
        #
        self.connectButton = tk.Button(self.groupCon,
            command = connectButtonClick, width=10)
        self.connectButton.pack(side="left")
        padder = tk.Label(self.groupCon, padx=1)
        padder.pack(side="left")
        self.clearButton = tk.Button(self.groupCon, text='clr msg',
            command = clearButtonClick)
        self.clearButton.pack(side="left")
        
        #-------------------------------------------------------------------
        # row 2: the message field (chat messages + status messages)
        #-------------------------------------------------------------------
        self.msgText = tksctxt.ScrolledText(height=15, width=42,
            state=tk.DISABLED)
        self.msgText.pack(side="top")

        #-------------------------------------------------------------------
        # row 3: sending messages
        #-------------------------------------------------------------------
        self.groupSend = tk.LabelFrame(bd=0)
        self.groupSend.pack(side="top")
        self.textInLbl = tk.Label(self.groupSend, text='message', padx=10)
        self.textInLbl.pack(side="left")
        self.textIn = tk.Entry(self.groupSend, width=38)
        # if the focus is on this text field and you hit 'Enter',
        # it should (try to) send
        self.textIn.bind('<Return>', sendMessage)
        self.textIn.pack(side="left")
        #
        padder = tk.Label(self.groupSend, padx=5)
        padder.pack(side="left")
        #
        self.sendButton = tk.Button(self.groupSend, text = 'send',
            command = sendButtonClick)
        self.sendButton.pack(side="left")
        
        # set the focus on the IP and Port text field
        self.ipPort.focus_set()

def clearButtonClick():
    g_app.msgText.configure(state=tk.NORMAL)
    g_app.msgText.delete(1.0, tk.END)
    g_app.msgText.see(tk.END)
    g_app.msgText.configure(state=tk.DISABLED)

def connectButtonClick():
    connectHandler(g_app)  # forward to the connect handler

def sendButtonClick():
    sendMessage(g_app)  # forward to the sendMessage method

# the connectHandler toggles the status between connected/disconnected
def connectHandler(master):
    if g_bConnected:
        disconnect()
    else:
        tryToConnect()

# a utility method to print to the message field        
def printToMessages(message):
    g_app.msgText.configure(state=tk.NORMAL)
    g_app.msgText.insert(tk.END, message + '\n')
    # scroll to the end, so the new message is visible at the bottom
    g_app.msgText.see(tk.END)
    g_app.msgText.configure(state=tk.DISABLED)

def on_closing(): # if attempt to close the window, it is handled here
    if g_bConnected:
        if tkmsgbox.askokcancel("Quit",
            "You are still connected. If you quit you will be"
            + " disconnected."):
            myQuit()
    else:
        myQuit()

def myQuit():
    disconnect()
    g_root.destroy()

def myAddrFormat(addr): # utility address formatting
    return '{}:{}'.format(addr[0], addr[1])


# disconnect from server (if connected) and
def disconnect():
    global g_bConnected
    global g_sock
    
    if g_sock: #check if connected 
        g_sock.close()
        g_sock = None #no active socket connection
        g_bConnected = False 
    g_app.connectButton['text'] = 'connect' #updated GUI

    
# when a user clicks on the button connect   
def tryToConnect():
    global g_bConnected
    global g_sock
    # try to connect to the IP address and port number
    # as indicated by the text field g_app.ipPort
    # a call to g_app.ipPort.get() delivers the text field's content
    # if connection successful, set the program's state to 'connected'
    try:
        # Get IP address and port number from the text field
        ip, port_str = g_app.ipPort.get().split(':')
        port = int(port_str)

        # Create and connect the socket
        g_sock = socket.create_connection((ip, port))

        # Update connection state and GUI
        g_bConnected = True
        g_sock.setblocking(False)
        g_app.connectButton['text'] = 'Disconnect'

    except (socket.error, ValueError) as e:
        print(f"Connection failed: {e}")
        raise RuntimeError('Connection failed')

# attempt to send the message (in the text field g_app.textIn) to the server
def sendMessage(master):
    # a call to g_app.textIn.get() delivers the text field's content
    # if a socket.error occurrs, you may want to disconnect, in order
    # to put the program into a defined state
    try:
        g_sock.sendall(g_app.textIn.get().encode('utf-8')) #reesives the message from text input field & sends message using sendall.

    except socket.error as e:
        print(f"Error sending message:{e}")
        disconnect()   
        
def pollMessages():
    g_root.after(g_pollFreq, pollMessages) # schedule the next execution of this function.
    try:
        message = g_sock.recv(2048) #try to revice x amount of data from socket,
        if message:
            print(message)  #we will print out and decode message.
            printToMessages(message.decode('utf-8'))
    except:
        pass

g_bConnected = False # by default we are not connected
g_sock = None

g_pollFreq = 200 # in milliseconds, dealy between 2 consecutive calls to pollMessages

g_root = tk.Tk() # launch the gui
g_app = Application(master=g_root)

disconnect()

# schedule the next call to pollMessages
g_root.after(g_pollFreq, pollMessages)

g_root.protocol("WM_DELETE_WINDOW", on_closing)

g_app.mainloop() 