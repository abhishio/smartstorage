#!/usr/bin/python3.4
import os
from tkinter import *
from tkinter.messagebox import showinfo
from threading import Thread

top=Tk()
top.title('Vapour Smart Disk')
top.geometry('300x500')

label=Label(top, text='Welcome\nTo\nVapour Smart Disk', font='Helvetica -24 bold')
label.pack(fill=Y, expand=1)

def CONNECT():
	os.system('python3.4 connect.py')
def SHOWDISK():
	os.system('./showdisk.sh')	
def OPEN():
	os.system('python3.4 mount.py')
def FORMAT():
	os.system('python3.4 format.py')
def DISCONNECT():
	os.system('python3.4 disconnect.py')
		
Connect=Button(top, text='Connect', command=CONNECT, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Connect.pack(fill=X, expand=1)

Showdisk=Button(top, text='Show Disk Status', command=SHOWDISK, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Showdisk.pack(fill=X, expand=1)

Open=Button(top, text='Open Cloud Disk', command=OPEN, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Open.pack(fill=X, expand=1)

Format=Button(top, text='Format', command=FORMAT, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Format.pack(fill=X, expand=1)

Disconnect=Button(top, text='Disconnect', command=DISCONNECT, bg='goldenrod1', fg='blue', activeforeground='white', activebackground='grey')
Disconnect.pack(fill=X, expand=1)

quit=Button(top, text='Exit', command=top.quit, bg='red', fg='blue', activeforeground='white', activebackground='green')
quit.pack(fill=X, expand=1)


mainloop()
