#!/usr/bin/python
from Tkinter import *
import os
import time
root=Tk()
root.title("Simple XAMPP Manager")
root.geometry("300x200")
root.resizable(0 ,0)
def checkStatusfn():
	showStatus.delete("1.0", END)
	showStatus.insert(END, "Checking")
	statusAgain=os.popen("/opt/lampp/lampp status").read()
	showStatus.delete("1.0", END)
	statusAgain1=statusAgain.split("\n");
	showStatus.insert(END, statusAgain1[1]+"\n"+statusAgain1[2]+"\n"+statusAgain1[3])
def startServerfn():
	starting=os.popen("/opt/lampp/lampp start").read()
	showStatus.delete("1.0", END)
	showStatus.insert(END, starting)
def stopServerfn():
	stopping=os.popen("/opt/lampp/lampp stop").read()
	showStatus.delete("1.0", END)
	showStatus.insert(END, stopping)
status=os.popen("/opt/lampp/lampp status").read()
checkStatus=Button(root, text="Check Status", command=checkStatusfn)
startServer=Button(root, text="Start XAMPP", command=startServerfn)
stopServer=Button(root, text="Stop XAMPP", command=stopServerfn)
stopServer.pack()
startServer.pack()
checkStatus.pack()
showStatus=Text(root)
showStatus.pack(side=LEFT)
showStatus.insert(END, status)
mainloop()
