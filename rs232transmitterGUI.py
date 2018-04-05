# This is my first try to create a python program with a GUI

import serial
import os
import time
from colorama import init
from colorama import Fore, Back, Style
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
	print(nextByteToSend)
	
def SendFF():
	ser.write(([255]))
	
def Send00():
	ser.write(([0]))

# GUI stuff
top = Tk()
top.geometry("300x500")

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

C0.pack()
C1.pack()
C2.pack()
C3.pack()
C4.pack()
C5.pack()
C6.pack()
C7.pack()

# Labels
L1 = Label(top, text = "User Name")
L1.pack( side = LEFT)

E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

# Buttons
Open = Button(top, text = "Open", command = OpenConnection)
Open.place(x = 10, y = 10)

Close = Button(top, text = "Close", command = CloseConnection)
Close.place(x = 90, y = 10)

SendFF = Button(top, text = "Send 0xFF", command = SendFF)
SendFF.place(x = 10, y = 40)

Send00 = Button(top, text = "Send 0x00", command = Send00)
Send00.place(x = 90, y = 40)

top.mainloop()