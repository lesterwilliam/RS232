#RS232 transmitter

#pyserial module
import serial
 
port = "COM1"
baud = 1200
timeout = 1
inputMSG = "Please enter value to send: "

# create serial object from class
ser = serial.Serial(port, baud, timeout=1)
	
# open the serial port
if ser.isOpen():
	print(ser.name + ' is open!')
else:
	print('Could not open serial port ' + str(ser.name) + '!')
	exit()

# endless loop, listens to command line and writes to serial port
while True:
	# read input and save it as unicode into val
	val = input(inputMSG)
	
	# exit condition
	if val == "exit":
		ser.close()
		print('Closed serial communication!')
		exit()
	
	# put val into a bytearray, integer-cast
	valBytearray = ([int(val)])
	
	# write complete array to serial port
	ser.write(valBytearray)
	print('Sent "' + str(val) + '" to ' + str(ser.name))