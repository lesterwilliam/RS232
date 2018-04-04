#RS232 transmitter

#pyserial module
import serial
import os
from colorama import init
init()
from colorama import Fore, Back, Style

clear = lambda: os.system('cls')
clear()

port = "COM1"
baud = 1200
timeout = 1

ser = serial.Serial(port, baud, timeout=1)

def Init():
	PortSel(port)
	BaudSel(baud)
	Standby()
	
#def Loop():
	#while True:

def Standby():
	clear()
	KeyboardInput = input('Enter command or use <help>')
	
	if KeyboardInput == 'help':
		OpenHelp()
	elif KeyboardInput == 'open':
		if ser.isOpen():
			print(Fore.GREEN + ser.name + ' is open!\n' + Style.RESET_ALL)
		else:
			print('\nCould not open serial port ' + str(ser.name) + '!\n')
		input()
		Standby()
	elif KeyboardInput == 'close':
		clear()
		if ser.isOpen():
			ser.close()
			print(Fore.YELLOW + 'Closed serial communication!' + Style.RESET_ALL)
		else:
			print('There was no connection.')
		input()
		Standby()
	elif KeyboardInput == 'send':
		ByteWrite()
	
def OpenHelp():
	clear()
	print('Insert decimal value between 0 and 255 and press enter.\n')
	print('Type <baud> to change baud rate.\n')
	print('Type <exit> to close program.\n')
	input('Quit help with any key.')
	Standby()
	
def BaudSel(baud):
	baud = input('Please enter baud rate. Leave blank for default rate 1200.')
	if not baud.isdigit() or baud == "":
		baud = 1200
	
def PortSel(port):
	port = input('Please enter serial port. Leave blank for default port COM1.')
	if port != 'COM1':
		port = 'COM1'
		
def ByteWrite():
	clear()
	val = input('Please enter value to send!')
	if not val.isdigit():
		print(Fore.RED + '\nPlease only input integer between 0 and 255 or command.\n' + Style.RESET_ALL)
	elif int(val) < 0 or int(val) > 255:
		print(Fore.RED + '\nPlease only input integer between 0 and 255 or command.\n' + Style.RESET_ALL)
	else:
		# put val into a bytearray, integer-cast
		valBytearray = ([int(val)])
		
		# write complete array to serial port
		ser.write(valBytearray)
		print(Fore.GREEN + 'Sent "' + str(val) + '" to ' + str(ser.name) + '.\n' + Style.RESET_ALL)
	input()
	Standby()
Init()