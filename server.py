# timeout error code from https://www.internalpointers.com/post/making-http-requests-sockets-python

from socket import *
import requests
import datetime, time


serverPort = 8182
SERVER = socket.gethostbyname(socket.gethostname())

addr = (SERVER, serverPort) # has to be a tuple to input as arg in bind function

# creating server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind((addr))

# server begins listening for requests
serverSocket.listen(1);
print('The server is ready to receive and listening on port{serverPort}')

while True:
    connectionSocket, addr = serverSocket.accept()
    print('connection from {addr} received')

    connectionSocket.settimeout(10)

    msg = connectionSocket.recv(1024).decode() # recieves the ip address from client
    #address = socket.gethostbyaddr(msg) # parse request to get destination server from ip
    # print that response was received with the exact time
    print("Received message: {msg} from {addr} at:  {msg.time()}")
    # get ip from request
    address = msg.split()[1].split('/')[2]

    try:
        while True:
            reponse = reponse + connectionSocket.recv(1024);
    except socket.timeout as e:
        print("Time Out!") # catches error if takes more time than requested

    serverSocket.connect((address, 80)) # send the client's request to the destination server
    serverSocket.send(msg.encode()) #https://www.internalpointers.com/post/making-http-requests-sockets-python
    # receive response from destination server
    index = serverSocket.recv(4096)
    print("Response was received from destination server at: ", time.time())
    
    connectionSocket.send(index.encode())
    finalResponseTime = time.time()
    # print that response was sent with exact time
    print("Response to client was sent at: ", finalResponseTime)
    connectionSocket.close()