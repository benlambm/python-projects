"""
Created on Sept 24, 2021

Author:  Ben Lamb
Program:  client_benlamb
Description: A client script to make RPC calls upon a localhost server

"""
from socket import *
from codecs import decode
from sys import argv

HOST = argv[1]
PORT = int(argv[2])
num1 = argv[3]
num2 = argv[4]
request_message = num1 + num2
BUFF_SIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "ascii"

server = socket(AF_INET, SOCK_STREAM)
server.connect(ADDRESS)

welcome = decode(server.recv(BUFF_SIZE), "ascii")
print(welcome)

while True:
    server.send(bytes(request_message, CODE))
    reply = decode(server.recv(BUFF_SIZE), CODE)
    print(reply)
    quit()