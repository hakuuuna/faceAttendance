import tkinter as tk
import csv
import sys
import re
import os.path
from tkinter import messagebox
from PIL import Image,ImageTk
from Calendar import Calendar
import subprocess
#from CalendarView import CalendarView


root = tk.Tk()
root.title("sheet date")
#Tikinter Vars

name = tk.StringVar()
hours = tk.IntVar()
minutes = tk.IntVar()
#Functions




def setup():
	#Used to make the two textfiles if they don't already exist

	file_exists = os.path.isfile("dates.txt")
	if file_exists:
		pass
	else:
		file = open("dates.txt", "w+")
		file.close()


	
def makeAppointment():
	#Format date
	day = str(datePickercalendar.day_selected)
	month = str(datePickercalendar.month_selected)
	
	
	
	if datePickercalendar.day_selected < 10:
	    day = "0"+str(datePickercalendar.day_selected)
	    
	if datePickercalendar.month_selected < 10:
	    month = "0"+str(datePickercalendar.month_selected)
	    
	
	    
	    
	    
	date = day+"/"+month+"/"+str(datePickercalendar.year_selected)
	#Format time
	if hours.get() < 10:
	    hour = "0"+str(hours.get())
	    print(date +" "+hour+":00")
	else:
	    hour = str(hours.get())
	    print(date +" "+str(hours.get())+":00")
	
   
	with open("dates.txt") as f:
		for line in f:
			if line.startswith(date +" "+hour+":00"):
				print(line.split("'")[1:])
				present = line.split("'")[1:]
				#print(re.findall("['(.*?)']", str(present)))
				print(present)
		subprocess.call(["python3","showSheet.py"] + present)
		print(date,hour,present)
					
					
			
	
	

	
	

	
					
#Call setup
setup()

#Define Frame

bookAppointment = tk.Frame(root)


#Configure all (main) Frames

bookAppointment.grid(row=0,column=0, sticky='news')
bookAppointment.configure(bg='black')





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
