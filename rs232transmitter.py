#RS232 transmitter

#pyserial module
import serial
import os
import time
from colorama import init
init()
from colorama import Fore, Back, Style
from random import randint

clear = lambda: os.system('cls')
clear()

DefaultPort = "COM1"
DefaultBaud = 1200
timeout = 1

ser = serial.Serial(DefaultPort, DefaultBaud, timeout=1)

def Init():
	print('RS232 transmitter by Adrian Schwizgebel\n_______________________________________\n\n')
	PortSel()
	BaudSel()
	ser.close()
	Standby()

def Standby():
	print('Enter command or use ' + Fore.GREEN + '<help>' + Style.RESET_ALL + ': ')
	KeyboardInput = input()
	
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
		Standby()
	elif KeyboardInput == 'close':
		if ser.isOpen():
			ser.close()
			print(Fore.YELLOW + 'Closed serial communication!' + Style.RESET_ALL)
		else:
			print('There was no connection.')
		Standby()
	elif KeyboardInput == 'send':
		clear()
		ByteWrite()
	elif KeyboardInput == 'random':
		Random()
		Standby()
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
	else:
		Standby()
	
def OpenHelp():
	clear()
	print('This program is designed to write single bytes to a RS232 port.\n')
	print('Type ' + Fore.GREEN + '<open>' + Style.RESET_ALL + ' to open a serial connection.')
	print('Type ' + Fore.GREEN + '<close>' + Style.RESET_ALL + ' to close a serial connection.')
	print('Type ' + Fore.GREEN + '<send>' + Style.RESET_ALL + ' to send byte.')
	print('Type ' + Fore.GREEN + '<random>' + Style.RESET_ALL + ' to send random byte.')
	print('Type ' + Fore.GREEN + '<port>' + Style.RESET_ALL + ' to change serial port.')
	print('Type ' + Fore.GREEN + '<baud>' + Style.RESET_ALL + ' to change baudrate.')
	print('Type ' + Fore.GREEN + '<exit>' + Style.RESET_ALL + ' to close program.')
	input('\nQuit help with any key.\n\n')
	Standby()
	
def PortSel():
	temp = input('Please enter serial port. Leave blank for default port COM1: ')
	if temp == '':
		ser.port = DefaultPort
		print('Set to default port ' + Fore.GREEN + 'COM1 ' + Style.RESET_ALL + '.\n')
	else:
		ser.port = temp
		print('Set port to ' + Fore.GREEN + ser.port + Style.RESET_ALL + '.')
		
def BaudSel():
	temp = input('Please enter baudrate. Leave blank for default baudrate of 1200: ')
	if temp == '':
		ser.baudrate = DefaultBaud
		print('Set to default baudrate of ' + Fore.GREEN + '1200 ' + Style.RESET_ALL + '.\n')
	else:
		ser.baudrate = int(temp)
		print('Set Baudrate to ' + Fore.GREEN + str(ser.baudrate) + Style.RESET_ALL + '.')
		
def ByteWrite():
	val = input('Please enter value to send: ')
	if val == 'menu' or val == 'back' or val == 'close' or val == 'exit':
		clear()
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
			Standby()
			
def Random():
	temp = randint(0,255)
	valBytearray2 = ([temp])
	if ser.isOpen():
		ser.write(valBytearray2)
		Standby()
	else:
		print(Fore.RED + 'There is no open connection!' + Style.RESET_ALL)
		Standby()
	
Init()