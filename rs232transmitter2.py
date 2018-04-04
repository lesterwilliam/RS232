#RS232 transmitter

#pyserial module
import serial
import os
from colorama import init
init()
from colorama import Fore, Back, Style

defaultport = "COM1"
defaultbaud = 1200
timeout = 1
inputMSG = "Please enter value to send: "

# clear cmd console
clear = lambda: os.system('cls')
clear()

# define port
definedport = input('Please enter serial port. Leave blank for default port COM1.')
if definedport == "":
	definedport = defaultport
	
# define baud rate
definedbaud = input('Please enter baud rate. Leave blank for default rate 1200.')
if definedbaud == "":
	definedbaud = defaultbaud

# create serial object from class
ser = serial.Serial(definedport, definedbaud, timeout=1)

# open the serial port
if ser.isOpen():
	print(Fore.GREEN + ser.name + ' is open!\n' + Style.RESET_ALL)
else:
	print('\nCould not open serial port ' + str(ser.name) + '!\n')
	exit()

# endless loop, listens to command line and writes to serial port
while True:
	# read input and save it as unicode into val
	val = input(inputMSG)
	
	# exit condition
	if val == "exit":
		ser.close()
		print(Fore.YELLOW + '\nClosed serial communication!' + Style.RESET_ALL)
		clear()
		exit()
	# close connection
	elif val == "close":
		clear()
		ser.close()
		print(Fore.YELLOW + 'Closed serial communication!' + Style.RESET_ALL)
	# open help
	elif val == "help":
		clear()
		print('Insert decimal value between 0 and 255 and press enter.\n')
		print('Type <baud> to change baud rate.\n')
		print('Type <exit> to close program.\n')
		input('Quit help with any key.')
		clear()
	# change baud
	elif val == "baud":
		clear()
		ser.close()
		print(Fore.RED + 'Closed serial communication!' + Style.RESET_ALL)
		definedbaud = input('Please enter new baud rate: ')
		ser = serial.Serial(definedport, definedbaud, timeout=1)
		# open the serial port
		if ser.isOpen():
			print(Fore.GREEN + ser.name + ' is open!\n' + Style.RESET_ALL)
		else:
			print('\nCould not open serial port ' + str(ser.name) + '!\n')
			exit()
	# wrong input contition
	elif not val.isdigit():
		print(Fore.RED + '\nPlease only input integer between 0 and 255 or <exit> command.\n' + Style.RESET_ALL)
	elif int(val) < 0 or int(val) > 255:
		print(Fore.RED + '\nPlease only input integer between 0 and 255 or <exit> command.\n' + Style.RESET_ALL)
	else:
		# put val into a bytearray, integer-cast
		valBytearray = ([int(val)])
		
		# write complete array to serial port
		ser.write(valBytearray)
		print(Fore.GREEN + 'Sent "' + str(val) + '" to ' + str(ser.name) + '.\n' + Style.RESET_ALL)