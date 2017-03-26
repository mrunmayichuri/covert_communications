#!/usr/bin/env python
#Mrunmayi Churi
#Server

import sys
from scapy import *

pkt = None

#Ensuring proper command line input
def CommandLineInput():
	if len(sys.argv) != 2:
		print "Error! Use the format:\n", sys.argv[0], "<Host_IP>"
		sys.exit()

#Creating the packet to be sent to the client
def CreatePacket(character):
	global pkt
	global destination
	destination = str(sys.argv[1])
	char = ord(character) 	# converting covert character to decimal value
	pkt = IP(dst=destination)/TCP(sport=RandNum(0,65535), dport=char,flags="E")
	pkt.show2()
	return pkt


#Obtaining user input and sending the message
def SendMessage():
	while True:
		message = raw_input('Enter your message:')
		message += "\n"
		print "Sending covert data..."
		for char in message:
			covert_packet = CreatePacket(char)
			send(covert_packet)

#Main program
def main():
	CommandLineInput()
	SendMessage() 

if __name__=="__main__":
	main()
