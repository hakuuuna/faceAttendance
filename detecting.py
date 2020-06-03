#!/usr/bin/python3

from tkinter import*
import tkinter.messagebox as ms

from tkinter import filedialog as fd

import PIL # Install Using PIP

from PIL import ImageTk, Image
from datetime import datetime

import csv
import os
import subprocess
#import stdDatabase_BackEnd

import sqlite3
# import tkFont
from tkinter import ttk
#from faceRecFrame import loop
class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Sheet")
        self.root.geometry("900x400+0+0")
        self.root.config(bg="black")

        StdID = StringVar()
        FirstName = StringVar()
        LastName = StringVar()
        

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++FUNCTIONS

        def iExit():
            
            if iExit > 0:
                root.destroy()
            return

                
            

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++FRAMES

        MainFrame = Frame(self.root, bg="black")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=15, pady=8,bg="grey", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 20, 'bold'),text="Attendance Sheet", bd=2, bg="grey")
        self.lblTit.grid()

        

        DataFrame = Frame(MainFrame, bd=1, width=700, height=750,padx=10, pady=5, relief=RIDGE, bg="black")
        DataFrame.pack(side=BOTTOM)


        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, font=('arial', 15, 'bold'), text="Student attendance Sheet \n",width=150, height=600, padx=20, pady=3, bg="black", relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)

        

      
        

        

        

        

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++BUTTON WIDGETS

        #self.btnAddDate = Button(ButtonFrame, font=('arial', 20, 'bold'), text="Stop", height=1, width=8, bd=4)
        #self.btnAddDate.grid(row=0, column=0)

        

        #self.btnExit = Button(ButtonFrame, font=(   'arial', 20, 'bold'), text="view", height=1, width=5, bd=4, command=iExit)
        #self.btnExit.grid(row=0, column=6)



        

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++TREE
        
        connection = sqlite3.connect('student.db')
        
        TABLE_NAME = "student"


        tree = ttk.Treeview(DataFrameRIGHT)
        tree["columns"] = ("one", "two", "three")
        
        
 
        tree.heading("one", text="Student Name")
        tree.heading("two", text="LastName")
        tree.heading("three", text="p/abs")
     
        
        # for col in tree["columns"]:
            # tree.column(col, width=tkFont.Font().measure(col.title()))
            
        cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
        
        present = sys.argv[1:]
        print(present)
        
     
        
        now = datetime.now()
        #time = now.strftime("%H") + ":00"
	    
        date = now.strftime("%d/%m/%Y %H:00")
        print("{} {}".format(date,present))
        with open ("dates.txt",'a',newline="") as appFile:
            writer=csv.writer(appFile) 
            writeList = ["{} {}".format(date,present)]
            writer.writerow(writeList)
            appFile.close()

	    
        
        for row in cursor:
            if row[2] in present:
                
                tree.insert('', 'end', values=(row[2], row[3], "p"))
            else:
                tree.insert('', 'end', values=(row[2], row[3], "abs" ))
        
        tree.pack()
        

        


        
        
        

        
        
        

        



if __name__ == '__main__':
    root = Tk()
    applicaiton = Student(root)
    root.mainloop()
