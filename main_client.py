import socket
import time


print(""" Welcome to this TXT file transfer script. 
          We hope you will enjoy your stay.""")
print()

str_ip = input("Please input the IP address of the server.")
str_port = input("PLease input the port number of the server.\n")
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

    received = c.recv(1024).decode()
    print(received)
    try:    
        file = open(name, "r")
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
    if run == "Y" or "":
        pass
    else: 
        print("Terminating connection.")
        break

c.close()
