# This is my first try to create a python program with a GUI

from tkinter import *
from tkinter import messagebox

def helloCallBack():
	msg = messagebox.showinfo( "Hello Python", "Hello World")
	
def CloseConnection():
	var = 1
	
def SerialUpdate():
	var2 = 2
	
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
C1 = Checkbutton(top, text = "Bit1", variable = CheckVar1, onvalue=2, offvalue=0, height=0, width=20)
C2 = Checkbutton(top, text = "Bit2", variable = CheckVar2, onvalue=4, offvalue=0, height=0, width=20)
C3 = Checkbutton(top, text = "Bit3", variable = CheckVar3, onvalue=8, offvalue=0, height=0, width=20)
C4 = Checkbutton(top, text = "Bit4", variable = CheckVar4, onvalue=16, offvalue=0, height=0, width=20)
C5 = Checkbutton(top, text = "Bit5", variable = CheckVar5, onvalue=32, offvalue=0, height=0, width=20)
C6 = Checkbutton(top, text = "Bit6", variable = CheckVar6, onvalue=64, offvalue=0, height=0, width=20)
C7 = Checkbutton(top, text = "Bit7", variable = CheckVar7, onvalue=128, offvalue=0, height=0, width=20)

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
Open = Button(top, text = "Open", command = helloCallBack)
Open.place(x = 10, y = 10)

Close = Button(top, text = "Close", command = CloseConnection)
Close.place(x = 90, y = 10)

top.mainloop()