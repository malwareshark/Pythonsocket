#!/bin/python3
#this script utilizes socket to connect one to node to another node.
import socket


HOST = '127.0.0.1'
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
