#!/usr/bin/python
import sys
import socket

if len(sys.argv) != 4:
    sys.stderr.write('Args should be: <host> <port> <message>\n')
    sys.exit(1)

host, port, message = sys.argv[1:4]

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto( message, (host, int(port)) )
except:
    sys.stderr.write('There was something funky about your host or port\n')
    sys.exit(2)
