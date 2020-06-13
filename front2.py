#!/usr/bin/python3

from tkinter import*
import tkinter.messagebox as ms

from tkinter import filedialog as fd

import PIL # Install Using PIP
#from tkinter.ttk import *
from PIL import ImageTk, Image

import os
import subprocess
import stdDatabase_BackEnd


class Student:

    def __init__(self, root):
        self.root = root
        self.root.title("Students Managment System")
        self.root.geometry("900x800+0+0")
        self.root.config(bg="black")

        StdID = StringVar()
        FirstName = StringVar()
        LastName = StringVar()
        DoB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Adress = StringVar()
        Mobile = StringVar()
        ImgPath = StringVar()

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++FUNCTIONS

        def iExit():
            root.destroy()
            return

        def clearData():
            self.txtStdID.delete(0, END)
            self.txtfna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAdr.delete(0, END)
            self.txtMobile.delete(0, END)
            self.txtImgPath['text'] = ""
            self.canvas.delete(ALL)
            
            
            
        def addData():
            if (len(StdID.get())!=0):
                #add into DB
                stdDatabase_BackEnd.addStdRec(StdID.get(), FirstName.get(), LastName.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get(),self.txtImgPath['text'])
                studentlist.delete(0,END)
                studentlist.insert(END,(StdID.get(), FirstName.get(), LastName.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get(),self.txtImgPath['text']))
                
                
                
                subprocess.call(["python3","addLines.py",FirstName.get() ,StdID.get()])
                
                            
     
        def DisplayData():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.viewData():
                studentlist.insert(END,row,str(""))
                
        def StudentRec(event):
            global sd 
            searchStd = studentlist.curselection()[0]  #current selection 
            sd = studentlist.get(searchStd)
            
            self.txtStdID.delete(0, END)
            self.txtStdID.insert(END,sd[1])
            self.txtfna.delete(0, END)
            self.txtfna.insert(END,sd[2])
            self.txtSna.delete(0, END)
            self.txtSna.insert(END,sd[3])
            self.txtDoB.delete(0, END)
            self.txtDoB.insert(END,sd[4])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END,sd[5])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END,sd[6])
            self.txtAdr.delete(0, END)
            self.txtAdr.insert(END,sd[7])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END,sd[8])
            self.txtImgPath['text'] = ""
            self.txtImgPath['text'] = sd[9]
            self.pilImage = Image.open(sd[9])
            re = self.pilImage.resize((300,300),Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(re)
            self.canvas.delete(ALL)
            self.canvas.create_image(150,100,anchor=CENTER,image=self.img)
       
            
                
        def deleteData():
            if (len(StdID.get())!=0):
                stdDatabase_BackEnd.deleteRec(sd[0])
                clearData()
                DisplayData()
                
        def searchDatabase():
            studentlist.delete(0,END)
            for row in stdDatabase_BackEnd.searchData(StdID.get(), FirstName.get(), LastName.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get(), ImgPath.get()):
                
                studentlist.insert(END,row,str(""))
                
        def update():
            if (len(StdID.get())!=0):
                stdDatabase_BackEnd.deleteRec(sd[0])
            if (len(StdID.get())!=0):
                stdDatabase_BackEnd.addStdRec(StdID.get(), FirstName.get(), LastName.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get(), self.txtImgPath['text'])
                studentlist.delete(0,END)
                
                studentlist.insert(END,(StdID.get(), FirstName.get(), LastName.get(), DoB.get(), Age.get(), Gender.get(), Adress.get(), Mobile.get(),self.txtImgPath['text']))

        


        def make_image():
            try:
                global ImgPath
                ImgPath = fd.askopenfilename()
                self.pilImage = Image.open(ImgPath)
                re = self.pilImage.resize((300,300),Image.ANTIALIAS)
                self.img = ImageTk.PhotoImage(re)
                self.canvas.delete(ALL)
                self.canvas.create_image(150,100,anchor=CENTER,image=self.img)
                self.txtImgPath['text']=ImgPath       #status modified with txtImgPath 
                print(ImgPath)
                ImgPath = str(ImgPath) 
            except:
                ms.showerror('Error!','FILE type is unsupported.')
                
        def take_image():
            subprocess.Popen(['python3', 'photo_booth.py', '-o' , 'images', '-n' , '{}'.format(FirstName.get()) ])
            
        
                 
       
                
            

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++FRAMES

        MainFrame = Frame(self.root, bg="black")
        MainFrame.grid()

        TitFrame = Frame(MainFrame, bd=2, padx=15, pady=4,bg="grey", relief=RIDGE)
        TitFrame.pack(side=TOP)

        self.lblTit = Label(TitFrame, font=('arial', 20, 'bold'),text="Student Management System", bd=2, bg="grey")
        self.lblTit.grid()
        
        
        

        

        DataFrame = Frame(MainFrame, bd=1, width=500, height=170,padx=10, pady=3, relief=RIDGE, bg="black")
        DataFrame.pack(side=BOTTOM)
        
        
       
        

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, font=('arial', 15, 'bold'), text="Student Info \n", width=250, height=150, padx=10,pady=15, bg="black", relief=RIDGE)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, font=('arial', 15, 'bold'), text="Image Browser \n",width=200, height=130, padx=20, pady=3, bg="black", relief=RIDGE)
        DataFrameRIGHT.pack(side=RIGHT)

        BottomFrame = Frame(self.root, bg="black", pady = 10)
        BottomFrame.grid()

        ButtonFrame = Frame(BottomFrame, bd=1, width=300, height=15,padx=10, pady=5, relief=RIDGE, bg="black")
        ButtonFrame.pack(side=TOP)

        DataFrameBOTTOM = LabelFrame(BottomFrame, bd=3,font=('arial', 15, 'bold'),text ="Student Details", width=200, height=60,padx=5, pady=5, relief=RIDGE, bg="black")
        DataFrameBOTTOM.pack(side=BOTTOM)

        

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++LABELS AND ENTRY WIDGETS

        self.lblStdID = Label(DataFrameLEFT, font=(
            'arial', 15, 'bold'), text="Stuent ID ",fg= "grey", padx=2, pady=2, bg="black")
        self.lblStdID.grid(row=0, column=0, sticky=W)

        self.txtStdID = Entry(DataFrameLEFT, font=(
            'arial', 15, 'bold'), textvariable=StdID,fg= "grey", width=25, bg="black")
        self.txtStdID.grid(row=0, column=1)

        self.lblfna = Label(DataFrameLEFT, font=(
            'arial', 15, 'bold'), text="First Name",fg= "grey", padx=2, pady=2, bg="black")
        self.lblfna.grid(row=1, column=0, sticky=W)

        self.txtfna = Entry(DataFrameLEFT, font=(
            'arial', 15, 'bold'), textvariable=FirstName,fg= "grey", width=25, bg="black")
        self.txtfna.grid(row=1, column=1)

        self.lblSna = Label(DataFrameLEFT, font=(
            'arial', 15, 'bold'), text="Last Name",fg= "grey", padx=2, pady=2, bg="black")
        self.lblSna.grid(row=2, column=0, sticky=W)

        self.txtSna = Entry(DataFrameLEFT, font=(
            'arial', 15, 'bold'), textvariable=LastName,fg= "grey", width=25, bg="black")
        self.txtSna.grid(row=2, column=1)

        self.lblDoB = Label(DataFrameLEFT, font=(
            'arial', 15, 'bold'), text="Date Of Birth ",fg= "grey", padx=2, pady=2, bg="black")
        self.lblDoB.grid(row=3, column=0, sticky=W)

        self.txtDoB = Entry(DataFrameLEFT, font=(
            'arial', 15, 'bold'), textvariable=DoB,fg= "grey", width=25, bg="black")
        self.txtDoB.grid(row=3, column=1)

        self.lblAge = Label(DataFrameLEFT, font=(
            'arial', 15, 'bold'), text="Age ",fg= "grey", padx=2, pady=2, bg="black")
        self.lblAge.grid(row=4, column=0, sticky=W)

        self.txtAge = Entry(DataFrameLEFT, font=(
            'arial', 15, 'bold'), textvariable=Age,fg= "grey", width=25, bg="black")
        self.txtAge.grid(row=4, column=1)

        self.lblGender = Label(DataFrameLEFT, font=(
            'arial', 15, 'bold'), text="Gender ",fg= "grey", padx=2, pady=2, bg="black")
        self.lblGender.grid(row=5, column=0, sticky=W)

        self.txtGender = Entry(DataFrameLEFT,fg= "grey", font=(
            'arial', 15, 'bold'), textvariable=Gender, width=25, bg="black")
        self.txtGender.grid(row=5, column=1)

        self.lblAdr = Label(DataFrameLEFT,fg= "grey", font=('arial', 15, 'bold'), text="Address ", padx=2, pady=2, bg="black")
        self.lblAdr.grid(row=6, column=0, sticky=W)

        self.txtAdr = Entry(DataFrameLEFT, font=(
            'arial', 15, 'bold'), textvariable=Adress,fg= "grey", width=25, bg="black")
        self.txtAdr.grid(row=6, column=1)

        self.lblMobile = Label(DataFrameLEFT, font=(
            'arial', 15, 'bold'), text="Mobile ",fg= "grey", padx=2, pady=2, bg="black")
        self.lblMobile.grid(row=7, column=0, sticky=W)

        self.txtMobile = Entry(DataFrameLEFT,fg= "grey", font=(
            'arial', 15, 'bold'), textvariable=Mobile, width=25, bg="black")
        self.txtMobile.grid(row=7, column=1)

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++Image Browser 

        self.canvas = Canvas(DataFrameRIGHT,height=200,width=300,
            bg='black',bd=1,relief='ridge')
        self.canvas.pack()

        txt = '''
                 
            No Image
        '''

        self.wt = self.canvas.create_text(50,50,text=txt,font=('',30),fill='grey')
        f = Frame(DataFrameRIGHT,bg='black',padx=10,pady=10)
        Button(f,text='Open New Image',bd=1,fg='white',bg='black',font=('',10),command= make_image).pack(side=LEFT)
        Button(f,text='Take An Image',bd=1,fg='white',bg='black',font=('',10),command= take_image).pack(side=RIGHT)
        f.pack()
        self.txtImgPath=Label(DataFrameRIGHT,text = 'Current Image: None',bg='gray',font=('Ubuntu',10),bd=1,fg='black',width= 50,relief='sunken',anchor=W)
        self.txtImgPath.pack(side=BOTTOM)
#sttus got modified with txtImgPath

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++BUTTON WIDGETS

        self.btnAddDate = Button(ButtonFrame, font=(
            'arial', 15, 'bold'), text="Add New ", height=1, width=8, bd=4, command = addData)
        self.btnAddDate.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, font=(
            'arial', 15, 'bold'), text="Display ", height=1, width=6, bd=4 , command = DisplayData)
        self.btnDisplayData.grid(row=0, column=1)

        self.btnClearData = Button(ButtonFrame, font=(
            'arial', 15, 'bold'), text="Clear", height=1, width=5, bd=4, command=clearData)
        self.btnClearData.grid(row=0, column=2)

        self.btnDeleteData = Button(ButtonFrame, font=(
            'arial', 15, 'bold'), text="Delete", height=1, width=5, bd=4, command = deleteData)
        self.btnDeleteData.grid(row=0, column=3)

        self.btnSearchData = Button(ButtonFrame, font=(
            'arial', 15, 'bold'), text="Search", height=1, width=6, bd=4, command = searchDatabase)
        self.btnSearchData.grid(row=0, column=4)

        self.btnUpdateData = Button(ButtonFrame, font=(
            'arial', 15, 'bold'), text="Update", height=1, width=6, bd=4, command = update)
        self.btnUpdateData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, font=(
            'arial', 15, 'bold'), text="Exit", height=1, width=5, bd=4, command=iExit)
        self.btnExit.grid(row=0, column=6)



        

        # ++++++++++++++++++++++++++++++++++++++++++++++++++++LISTBOX & SCROLL BAR WIDGET

        scrollbar = Scrollbar(DataFrameBOTTOM)
        scrollbar.grid(row=2, column=1, sticky='ns')

        studentlist = Listbox(DataFrameBOTTOM, font=('arial', 12, 'bold'), height=6, width=90, yscrollcommand=scrollbar.set)
        
        studentlist.bind('<<ListboxSelect>>', StudentRec)   
#we call the student record inside a Side Box 
        
        studentlist.grid(row=2, column=0, padx=8)

        scrollbar.config(command=studentlist.yview)





if __name__ == '__main__':
    root = Tk()
    applicaiton = Student(root)
    root.mainloop()
