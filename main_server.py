import socket
import time
import tkinter as tk

#Bind it to a static ip and the open port
s = socket.socket()
print("Socket Created")
s.bind(("192.168.0.103", 80))

s.listen(3)
print("Waiting for connections")

c, addr =  s.accept()
print(f"{addr} connected")

while True:
    name = c.recv(1024).decode()
    c.send(bytes(f"Filename received: {name}    Awaiting data...", "utf-8"))
    
    print("Client Disconnected.")

    print("Recieving data...")
    data = c.recv(1024).decode()
    
    file = open(name,  "w")
    print("Writing to file...")
    file.write(data)
    time.sleep(2)
    file.close()    
    
    c.send(bytes("File transfered.", "utf-8"))
    print("File Transfered.")
    

    