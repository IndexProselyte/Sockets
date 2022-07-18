import socket
import time
import os

print("Welcome to my Text File transfer script.")
print("You can transfer any type of file that consists of text. (code,text,csv)")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

str_ip = input("Please input the IP address of the server: ")
str_port = input("PLease input the port number of the server: ")
port = int(str_port)

try: 
    c = socket.socket()
    c.connect((str_ip, port))
    print(f"Connected to server. IP:{str_ip}, PORT:{port}\n")
except:
    print("Wrong ip address or port. Please run the script again.")
    time.sleep(1)
    c.close()

while True:
    name = input("Enter the file name: ")
    c.send(bytes(name, "utf-8"))

    #! i dont like paths :(
    # This makes it so i can have a sepparate folder for files.   
    script_dir = os.path.dirname(__file__) 
    rel_path = f"Files/{name}"
    abs_path = os.path.join(script_dir, rel_path)

    received = c.recv(1024).decode()
    print(received)
    try:    
        file = open(abs_path, "r")
        data = file.read()
        time.sleep(1)
        c.send(bytes(data, "utf-8"))
        print("Data sent.")
    except:
        print("Cannot find the specified file. Or the file isnt in text form.")


    received = c.recv(1024).decode()
    print(received)
    time.sleep(3)
    
    run = input("Do you want to continue transfering files? (Y/n)")
    if run == "Y" or "y":
        pass
    else: 
        print("Terminating connection.")
        break

c.close()
