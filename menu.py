

import numpy
#from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox

import subprocess



main=Tk()
main.geometry('460x500')

frame = Frame(main, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)

main.title('Students Attendance')
frame.config(background='gray')

label = Label(frame, text="Students Attendance",bg='grey',font=('Times 35 bold'))
label.pack(side=TOP)

filename = PhotoImage(file="./images/demo.png")

background_label = Label(frame,image=filename)
background_label.pack(side=TOP)



def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contributors","\n1.Nasreddin Elhafi\n2. Jihane Al Amrani \n")


def anotherWin():
   tkinter.messagebox.showinfo("About",'Students Attendance version v1.0\n Made Using\n-OpenCV\n-facial-recognition\n-Tkinter\n In Python3')
                                    
   

menu = Menu(main)
main.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Students Attendance",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)





  



#added

def start():
   #exec(open('{}'.format(name)).read())
   subprocess.call(["python3","faceRecFrame1.py"])

def front():
   #exec(open('{}'.format(name)).read())
   subprocess.call(["python3","front2.py"])
   
def db():
   #exec(open('{}'.format(name)).read())
   subprocess.call(["python3","data.py"])

   
def sheetDate():
   #exec(open('{}'.format(name)).read())
   subprocess.call(["python3","sheetDate.py"])

   
def iExit():
   main.destroy()
   return

   
but1=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,text='Start',font=('helvetica 15 bold'), command = start)
but1.place(x=5,y=104)

but2=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,text='Students Management',font=('helvetica 15 bold'), command = front)
but2.place(x=5,y=176)

but3=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,text='DataBase',font=('helvetica 15 bold'), command = db)
but3.place(x=5,y=250)

but4=Button(frame,padx=5,pady=5,width=39,bg='white',fg='black',relief=GROOVE,text='Attendance Sheets',font=('helvetica 15 bold'), command = sheetDate)
but4.place(x=5,y=322)


but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='black',relief=GROOVE,text='EXIT',font=('helvetica 15 bold'), command= iExit)
but5.place(x=190,y=448)


main.mainloop()

