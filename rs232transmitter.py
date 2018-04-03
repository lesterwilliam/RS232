#RS232 transmitter

import serial
 
port = "COM1"
baud = 1200
timeout = 1
 
ser = serial.Serial(port, baud, timeout=1)

# open the serial port
if ser.isOpen():
	print(ser.name + ' is open...')
	val = 0b1
	ser.write(b'2')
	ser.close()
	print('Sent ' + str(val) + ' to ' + str(ser.name))
	exit()