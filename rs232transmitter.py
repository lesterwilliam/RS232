#RS232 transmitter

#pyserial module
import serial
import os
from colorama import init
init()
from colorama import Fore, Back, Style

clear = lambda: os.system('cls')
clear()

DefaultPort = "COM1"
DefaultBaud = 1200
timeout = 1

ser = serial.Serial(DefaultPort, DefaultBaud, timeout=1)

def Init():
	PortSel()
	BaudSel()
	ser.close()
	Standby()

def Standby():
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
	temp = input('Please enter serial port. Leave blank for default port COM1.')
	if temp == '':
		ser.port = DefaultPort
		print('Default port ' + Fore.GREEN + 'COM1 ' + Style.RESET_ALL + 'chosen.\n')
	else:
		ser.port = temp
		print('Port ' + Fore.GREEN + ser.port + Style.RESET_ALL + ' chosen.')
		
def BaudSel():
	temp = input('Please enter baudrate. Leave blank for default baudrate of 1200.')
	if temp == '':
		ser.baudrate = DefaultBaud
		print('Default baudrate of ' + Fore.GREEN + '1200 ' + Style.RESET_ALL + 'chosen.\n')
	else:
		ser.baudrate = int(temp)
		print('Baudrate ' + Fore.GREEN + str(ser.baudrate) + Style.RESET_ALL + ' chosen.')
		
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