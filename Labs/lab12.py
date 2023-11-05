#12 Nazli Zamanian Gustavsson

import firebase_admin 
from firebase_admin import  credentials, db 

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://lab12-9e351-default-rtdb.europe-west1.firebasedatabase.app/'})  

# Create a refer
# ence to the root of your database
ref = db.reference('/')

def stream_handler(message):
    if message['event_type'] == 'put':
        if message['path'] == '/message':
            for key, value in message['data'].items():
                handle_message(value)
                
def handle_message(message):
    name = message['name']
    text = message['text']
    print(f'{name}: {text}')
    
message_stream = ref.child('messages').listen(stream_handler)

new_message = {'name': 'Jojo', 'text': 'hello, Firebase!'}
ref.child('messages').push(new_message)
            