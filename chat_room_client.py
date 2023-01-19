import socket
import threading
from getpass import  getpass
from hashlib import sha256
nickname=input("choose a nickname : ")
host='127.0.0.1' #localhost
port=60254
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((host,port))

def recieve():
    while True : 
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("!!!!an error occured!!!!!")
            client.close()
            break

def write():
    while True :
        message =f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))
def login():
    
    client.send(("LOGIN").encode('ascii'))
    message = client.recv(1024).decode('ascii')
    if message == "NAME":
        name= input("enter your First Name")
        client.send(name.encode('ascii'))
    elif message == "PASS":
        pwd=getpass("enter your Password") 
        client.send((sha256(pwd.encode()).hexdigest()).encode('ascii'))
    elif message =="SUCCESS":
        print("success")
    else : 
        print("error")    


recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()