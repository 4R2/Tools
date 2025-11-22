#!/usr/bin/python

import fileinput
import socket
import sys

if len(sys.argv) !=3:
        print ("uses ./smtp-enum.py <IP> <user>")
        exit(0)
ip=sys.argv[1]
print ("args fulfilled")

s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect= s.connect((ip,25))
banner=s.recv(1024)
print (banner)

for user in fileinput.input(sys.argv[2]):
        verify= 'VRFY ' + user + ' \r\n'
        ver=verify.encode()
        s.send(ver)
        result=s.recv(1024)
        print (result)
s.close()
