import tkinter as tk
import csv
import sys
import os.path
from tkinter import messagebox
from PIL import Image,ImageTk
from Calendar import Calendar
import subprocess
#from CalendarView import CalendarView


root = tk.Tk()
root.title("Swim School")
#Tikinter Vars
username = tk.StringVar()
password = tk.StringVar()
name = tk.StringVar()
loggedInLabel = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()
#Functions
def setup():
	#Used to make the two textfiles if they don't already exist
	file_exists = os.path.isfile("users.txt")
	if file_exists:
		pass
	else:
		file = open("users.txt", "w+")
		file.close()
	file_exists = os.path.isfile("dates.txt")
	if file_exists:
		pass
	else:
		file = open("dates.txt", "w+")
		file.close()


	
def makeAppointment():
	#Format date
	date = str(datePickercalendar.day_selected)+"/"+"0"+str(datePickercalendar.month_selected)+"/"+str(datePickercalendar.year_selected)
	#Format time
	
	
	time = str(hours.get())+":00"
	presenceList = ["aloha"]
	#with open ("appointments.txt",'w',newline="") as appFile:
	#	writer = csv.writer(appFile)
	#	writeList = [name.get(),date,time,preseceList]
	#	writer.writerow(writeList)
	#	appFile.close()
   
	with open("dates.txt") as f:
		for line in f:
			if line.startswith(date +" "+str(hours.get())+":00" ):
				print(line.split(" ")[2])
				present = line.split(" ")[2]
				print(present)
				subprocess.call(["python3","showSheet.py"] + present)
					
					
				#if word == date:   # create a list of lists
		#for i, x in enumerate(lis):   #print the list items 
		#	print("{}".format(x))
	
	
	print(date,time,present)
	#messagebox.showinfo("Success!","Appointment made!")
	#calendarViewFrame = tk.Frame(userFrame, borderwidth=5, bg="black")
	#calendarViewFrame.grid(row=2, column=1, columnspan=5)
	#viewCalendar = CalendarView(calendarViewFrame, {name.get()})
	
	

	
					
#Call setup
setup()

#Define Frame

bookAppointment = tk.Frame(root)


#Configure all (main) Frames

bookAppointment.grid(row=0,column=0, sticky='news')
bookAppointment.configure(bg='black')
	
with open("users.txt",'r') as userFile:
		reader = csv.reader(userFile)
		for row in reader:
			#removes empty list from loop
			if len(row)>0:
				print(row[0]+" has logged in!")
				#Set welcome message
				loggedInLabel.set("Welcome, "+row[0])
				# Calendar View
				#global calendarViewFrame
				#calendarViewFrame = tk.Frame(userFrame, borderwidth=5, bg="black")
				#calendarViewFrame.grid(row=2, column=1, columnspan=5)
				#viewCalendar = CalendarView(calendarViewFrame, {row[0]})
				name.set(row[0])
				#raiseFrame(userFrame)




tk.Label(bookAppointment,text="Attendace Sheet date",font=("Courier", 30),bg='black').grid(row=1,column=1,columnspan=5)
tk.Label(bookAppointment,text="Select a Date: ",font=("Courier", 22),bg='black').grid(row=2,column=1)
tk.Label(bookAppointment,text="Select Hour: ",font=("Courier", 22),bg='black').grid(row=3,column=1)

#Buttons

tk.Button(bookAppointment,font=("Courier", 22),bg='grey',text="view sheet",command=lambda :makeAppointment()).grid(row=5,column=2)
tk.Button(bookAppointment,font=("Courier", 22),bg='grey',text="Back").grid(row=5,column=1)


#Time Selector
timeSelectFrame = tk.Frame(bookAppointment,borderwidth=5,bg="black")
timeSelectFrame.grid(row=3,column=2)

tk.Spinbox(timeSelectFrame,from_=1, to=24,bg="grey",width=2,textvariable=hours).grid(row=1,column=1)

tk.Label(timeSelectFrame,text=":00",bg="grey").grid(row=1,column=2)


calendarFrame = tk.Frame(bookAppointment, borderwidth=5, bg="black")
calendarFrame.grid(row=2, column=2, columnspan=5)

datePickercalendar = Calendar(calendarFrame, {})
#Raise Initial Frame
bookAppointment.tkraise(bookAppointment)
root.mainloop()
