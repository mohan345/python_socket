#!/usr/bin/env python

import socket
import thread

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("",8888))

c_ip="192.168.122.1"
c_port=9999

def recv():
    while True:
        data=s.recvfrom(100)
        print "from client 1: ",data[0]

def send():
    while True:
        msg=raw_input("type to send : ")
        s.sendto(msg,(c_ip,c_port))

thread.start_new_thread(recv,())
thread.start_new_thread(send,())



while True:
    pass
~                                                                                                                                                     
~                                                                                                                                                     
~                                                                                                                                                     
~ 
