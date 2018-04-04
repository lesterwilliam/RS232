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
	val = input(inputMSG)
	if val == "exit":
		ser.close()
		print('Closed serial communication!')
		exit()
	val = int(val.encode('utf-8'))
	#ser.write(val.encode('utf-8'))
	ser.write(val)
	print('Sent "' + str(val) + '" to ' + str(ser.name))
	
	
	
	
# endless loop, listens to command line and writes to serial port
while True:
	val = input(inputMSG)
	if val == "exit":
		ser.close()
		print('Closed serial communication!')
		exit()
	val = chr(int(val))
	ser.write(val.encode('utf-8'))
	print('Sent "' + str(val) + '" to ' + str(ser.name))