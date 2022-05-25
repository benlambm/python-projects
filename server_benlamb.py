"""
Created on Sept 24, 2021

Author:  Ben Lamb
Program:  server_benlamb
Description: A server script to receive RPC calls for some basic calculations

"""
from codecs import decode
from socket import *
from time import ctime

HOST = "localhost"
PORT = 8000
ADDRESS = (HOST, PORT)
BUFF_SIZE = 1024
CODE = "ascii"

while True:
    server = socket(AF_INET, SOCK_STREAM)
    server.bind(ADDRESS)
    server.listen(10)
    print("Waiting for connection...")
    (client, server) = server.accept()
    print("...Connected from: ", client.getsockname())
    client.send(bytes("Welcome to my server!", CODE))
    while True:
        request = decode(client.recv(BUFF_SIZE), CODE)
        x = int(request[0])
        y = int(request[1])
        response = f"""
        {x} * {y} is {x * y}
        {x} / {y} is {x / y}
        {x} + {y} is {x + y}
        {x} - {y} is {x - y}
        {x} / 0 is Infinity
        Servertime is {ctime()}
        Have a nice day!
        """
        client.send(bytes(response, CODE))
        break
    print("...Response sent...closing connection.")
    client.close()
    break
