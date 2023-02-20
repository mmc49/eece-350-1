# used code from the example posted on moodle
# socket programming with TCP -> safer and more reliable

from socket import * #importing socket library
import requests
import datetime, time
import re, uuid  # to get MAC address 1st way
from uuid import getnode as get_mac #2nd way

# input website IP to access
ip = input('enter IP of website you wish to access>> ')

# identifier for process/server 
serverPort = 8080

serverName = 'servername'

server = (serverName, serverPort) # has to be a tuple to input as arg in connect function

# creating client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# send request to connect client to server
clientSocket.connect(server)
# print msg of request details and exact time sent
#print("Request details: ")
print("Request sent at: ", time.time())
  
# send the datagram
clientSocket.sendto(ip.encode())
send_time_ms = time.time() # time message was sent
print("Request details: ", ip, "\nsent at: ", send_time_ms)

# receive answer from server
serverReply = clientSocket.recv(1024)
recv_time_ms = time.time(); # time response was received from the server
# print details and exact time received
print("Response was received from the server at: ", recv_time_ms)

print('From server: ', serverReply.decode())

clientSocket.close()

# print total RTT, code fromhttps://www.quora.com/What-is-the-Python-code-to-calculate-Round-trip-time-between-server-and-client
rtt_ms = round(recv_time_ms - send_time_ms, 3)
print("Total round-trip time: ", rtt_ms)

# print physical MAC addres
#1st way
# code from stack overflow https://stackoverflow.com/questions/159137/getting-mac-address
mac = get_mac()
print("The MAC adress is: ", mac)
# 2nd way
# code from geeksforgeeks
#print ("The MAC address is : ", end="")
#print (':'.join(re.findall('..', '%012x' % uuid.getnode())))