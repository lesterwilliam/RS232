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
	PortSel()
	BaudSel()
	ser.close()
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
			print(Fore.YELLOW + ser.name + ' is already open!\n' + Style.RESET_ALL)
		else:
			ser.open()
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
	elif KeyboardInput == 'port':
		PortSel()
		Standby()
	elif KeyboardInput == 'baud':
		BaudSel()
		Standby()
	elif KeyboardInput == 'exit':
		clear()
		ser.close()
		exit()
	elif KeyboardInput == '':
		Standby()
	
def OpenHelp():
	clear()
	print('This program is designed to write single bytes to a RS232 port.\n')
	print('Type ' + Fore.GREEN + '<open>' + Style.RESET_ALL + ' to open a serial connection.')
	print('Type ' + Fore.GREEN + '<close>' + Style.RESET_ALL + ' to close a serial connection.')
	print('Type ' + Fore.GREEN + '<send>' + Style.RESET_ALL + ' to send data.')
	print('Type ' + Fore.GREEN + '<port>' + Style.RESET_ALL + ' to change serial port.')
	print('Type ' + Fore.GREEN + '<baud>' + Style.RESET_ALL + ' to change baudrate.')
	print('Type ' + Fore.GREEN + '<exit>' + Style.RESET_ALL + ' to close program.')
	input('\nQuit help with any key.')
	Standby()
	
def PortSel():
	ser.port = input('Please enter serial port. Leave blank for default port COM1.\n')
		
def BaudSel():
	ser.baudrate = int(input('Please enter baud rate. Leave blank for default rate 1200.\n'))
		
def ByteWrite():
	clear()
	val = input('Please enter value to send!')
	if val == 'menu' or val == 'back' or val == 'close' or val == 'exit':
		Standby()
	elif not val.isdigit():
		print(Fore.RED + '\nPlease only input integer between 0 and 255 or command.\n' + Style.RESET_ALL)
		ByteWrite()
	elif int(val) < 0 or int(val) > 255:
		print(Fore.RED + '\nPlease only input integer between 0 and 255 or command.\n' + Style.RESET_ALL)
		ByteWrite()
	else:
		valBytearray = ([int(val)])
		if ser.isOpen():
			ser.write(valBytearray)
			print(Fore.GREEN + 'Sent "' + str(val) + '" to ' + str(ser.name) + '.\n' + Style.RESET_ALL)
			ByteWrite()
		else:
			print(Fore.RED + 'There is no open connection!' + Style.RESET_ALL)
			input()
			Standby()
Init()