#!/usr/bin/env python
#Mrunmayi Churi
#Client

import sys
from scapy.all import *

def receive(packet):
    flag=packet['TCP'].flags
    if flag == 0x40:
	char = chr(packet['TCP'].dport)
        sys.stdout.write(char)

def main():
    print "\nStart sending covert data:\n"
    sniff(filter="tcp", prn=receive)
    

if __name__=="__main__":
    main()

