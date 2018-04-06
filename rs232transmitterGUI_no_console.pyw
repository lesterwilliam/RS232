# This is my first try to create a python program with a GUI

import serial
import os
import time
from random import randint
from tkinter import *
from tkinter import messagebox

connectionFlag = 0

DefaultPort = "COM1"
DefaultBaud = 1200
timeout = 1

nextByteToSend = 0

ser = serial.Serial(DefaultPort, DefaultBaud, timeout=1)

def helloCallBack():
	msg = messagebox.showinfo( "Hello Python", "Hello World")

def OpenConnection():
	if ser.isOpen():
		connectionFlag = 1
	else:
		ser.open()
		if ser.isOpen():
			connectionFlag = 1
		else:
			connectionFlag = 0
			# Error pop-up message that connection couldn't be opened
	
def CloseConnection():
	if not ser.isOpen():
		connectionFlag = 0
	else:
		ser.close()
		connectionFlag = 0
	if ser.isOpen():
		# Error pop-up message that connection couldn't be closed
		connectionFlag = 1
	
def SerialUpdate():
	nextByteToSend = CheckVar0.get() + CheckVar1.get() + CheckVar2.get() + CheckVar3.get() + CheckVar4.get() + CheckVar5.get() + CheckVar6.get() + CheckVar7.get()
	ser.write([int(nextByteToSend)])
	
def SendRandom():
	ser.write(([randint(0,255)]))
	
def UpdatePort():
	ser.close()
	ser.port = 'COM' + str((int(str(Lb1.curselection())[1:2])+1))
	PortSel.set(ser.port)
	ser.open()
	print('Active port: ' + str(ser.port))
	
# GUI stuff
top = Tk()
top.title("RS232 transmitter")
top.geometry("220x400")
top.wm_iconbitmap("Icon.ico")

# Checkboxes
CheckVar0 = IntVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()

C0 = Checkbutton(top, text = "Bit0", variable = CheckVar0, onvalue=1, offvalue=0, height=0, width=20, command = SerialUpdate)
C1 = Checkbutton(top, text = "Bit1", variable = CheckVar1, onvalue=2, offvalue=0, height=0, width=20, command = SerialUpdate)
C2 = Checkbutton(top, text = "Bit2", variable = CheckVar2, onvalue=4, offvalue=0, height=0, width=20, command = SerialUpdate)
C3 = Checkbutton(top, text = "Bit3", variable = CheckVar3, onvalue=8, offvalue=0, height=0, width=20, command = SerialUpdate)
C4 = Checkbutton(top, text = "Bit4", variable = CheckVar4, onvalue=16, offvalue=0, height=0, width=20, command = SerialUpdate)
C5 = Checkbutton(top, text = "Bit5", variable = CheckVar5, onvalue=32, offvalue=0, height=0, width=20, command = SerialUpdate)
C6 = Checkbutton(top, text = "Bit6", variable = CheckVar6, onvalue=64, offvalue=0, height=0, width=20, command = SerialUpdate)
C7 = Checkbutton(top, text = "Bit7", variable = CheckVar7, onvalue=128, offvalue=0, height=0, width=20, command = SerialUpdate)

C0.place(x=-30,y=0)
C1.place(x=-30,y=20)
C2.place(x=-30,y=40)
C3.place(x=-30,y=60)
C4.place(x=80,y=0)
C5.place(x=80,y=20)
C6.place(x=80,y=40)
C7.place(x=80,y=60)

# Listbox
Lb1 = Listbox(top, height=11, width = 25)
Lb1.insert(1, "COM1")
Lb1.insert(2, "COM2")
Lb1.insert(3, "COM3")
Lb1.insert(4, "COM4")
Lb1.insert(5, "COM5")
Lb1.insert(6, "COM6")
Lb1.insert(7, "COM7")
Lb1.insert(8, "COM8")
Lb1.insert(9, "COM9")

Lb1.place(x=30,y=140)

# Labels
PortSel = StringVar()
PortSelLabel = Label(top, textvariable = PortSel, relief = RAISED, width = 19)
PortSelLabel.place(x=35, y=115)

# Buttons
SendRandom = Button(top, text = "Random", command = SendRandom)
SendRandom.place(x=75, y=85)

Apply = Button(top, text = "Apply", command = UpdatePort)
Apply.place(x=85, y=325)

top.mainloop()