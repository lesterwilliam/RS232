#RS232 transmitter

import serial
 
port = "COM1"
baud = 1200
 
ser = serial.Serial(port, baud, timeout=1)
    # open the serial port
if ser.isOpen():
     print(ser.name + ' is open...')
 
while True:
    cmd = input("Enter command or 'exit':")
    if cmd == 'exit':
        ser.close()
        exit()
    else:
        ser.write(cmd.encode('ascii')+'\r\n')
        out = ser.read()
        print('Receiving...'+out)