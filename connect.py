#!/usr/bin/python3.4
import os
import tkinter
top = tkinter.Tk()
top.title('Connected')
top.geometry('400x50')

active=os.system('iscsiadm -m session &> /dev/null')
if active !=0:
	os.system("iscsiadm --mode node --targetname iqn.2003-01.org.linux-iscsi.cloud.x8664:server --portal 192.168.100.4:3260 --login &> /dev/null")
	label = tkinter.Label(top, text='Connected to Vapour Cloud Disk ', font='Helvetica -20 bold')
	label.pack()
	quit = tkinter.Button(top, text='Exit',command=top.quit)
	quit.pack()
else :
	label = tkinter.Label(top, text='Already Connected',font='Helvetica -20 bold')
	label.pack()
	quit = tkinter.Button(top, text='Exit',command=top.quit)
	quit.pack()
tkinter.mainloop()
