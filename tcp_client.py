#!/usr/bin/env python3

import socket

# The client must have the same server specifications
host = '192.168.196.135'
port = 12345
BUFFER_SIZE = 1024

MESSAGE = 'Hello world, this is my first message' 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host, port))
    # We convert str to bytes
    socket_tcp.send(MESSAGE.encode('utf-8'))
    data = socket_tcp.recv(BUFFER_SIZE)
    print('[*] Data received: {}'.format(data.decode('utf-8')))
    print('[*] Data received in bytes: {}'.format(":".join("{:02x}".format(ord(c)) for c in data.decode('utf-8')))) 