from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
from datetime import timedelta
import tkinter.messagebox

class Library:

    def __init__(self,root):
        self.root = root
        self.root.title("stark library")
        self.root.geometry("1980x1080+0+0")
        self.root.configure(background='Cadet blue')

        MType=StringVar()
        Ref =StringVar()
        Title =StringVar()
        Firstname=StringVar()
        Surname=StringVar()
        Address1=StringVar()
        Address2=StringVar()
        PostCode=StringVar()
        MobileNo=StringVar()
        BookID=StringVar()
        BookTitle=StringVar()
        BookType=StringVar()
        Author=StringVar()
        DateBorrowed=StringVar()
        DateDue=StringVar()
        SellingPrice=StringVar()
        lateReturnFine=StringVar()
        DateOverDue=StringVar()
        DaysOnLoan=StringVar()
        Prescription=StringVar()
        def iReset():
            MType.set("")
            Ref.set ("")
            Title.set ("")
            Firstname.set("")
            Surname.set("")
            Address1.set("")
            Address2.set("")
            PostCode.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            BookType.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            SellingPrice.set("")
            lateReturnFine.set("")
            DateOverDue.set("")
            DaysOnLoan.set("")
            self.txtFrameDetail.delete("1.0",END)
            
        def iDelete():
            iReset()
            self.txtDisplayR.delete("1.0",END)
        
        def iExit():
            iExit =tkinter.messagebox.askyesno ("stark Library","Confirm if you want to exit")
            if iExit>0:
                root.destroy()
                return

        def iDisplayData():

            self.txtFrameDetail.insert(END,"\t"+MType.set()+"\t\t"+Ref.get()+"\t"+Title.get()+"\t"+
            Firstname.get() +"\t"+ Surname.get()+ "\t\t"+Address1.get() +"\t\t"+ Address2.get()+ "\t\t"+
            PostCode.get() +"\t\t"+BookTitle.get() +"\t\t"+ DateBorrowed.get() +"\t\t" + DaysOnLoan.get()+"\n")

        def iReciept():
            self.txtDisplayR.insert(END,"Member Type: \t\t" + MType.set() + "\n")
            self.txtDisplayR.insert(END,"Ref No: \t\t" + Ref.get() +"\n")
            self.txtDisplayR.insert(END,"Title: \t\t" + Title.get() +"\n") 
            self.txtDisplayR.insert(END,"Firstname: \t\t" + Firstname.get() + "\n")
            self.txtDisplayR.insert(END,"Surname: \t\t" + Surname.get() + "\n")
            self.txtDisplayR.insert(END,"Address1: \t\t" + Address1.get() + "\n")
            self.txtDisplayR.insert(END,"Address2: \t\t" + Address2.get() + "\n")
            self.txtDisplayR.insert(END,"Post Code: \t\t" + PostCode.get() + "\n")
            self.txtDisplayR.insert(END,"Mobile No: \t\t" + MobileNo.get() + "\n")
            self.txtDisplayR.insert(END,"Book ID: \t\t" + BookID.get() + "\n")
            self.txtDisplayR.insert(END,"Book Title: \t\t" + BookTitle.get() + "\n")
            self.txtDisplayR.insert(END,"Author: \t\t" + Author.get() + "\n")
            self.txtDisplayR.insert(END,"Date Borrowed: \t\t" + DateBorrowed.get() + "\n")


        #========================================================Frame==============================================================

        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, width=1350, padx=20, bd=20, relief=RIDGE)
        TitleFrame.pack(side=TOP)
        self.lblTitle =Label(TitleFrame,width=39,font=('arial',40,'bold'),text="\tstark library\t",padx=12)
        self.lblTitle.grid()

        ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail =Frame(MainFrame, bd=20, width=1350, height=100, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame =Frame(MainFrame, bd=20, width=1300, height=400, padx=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT =LabelFrame(DataFrame, bd=10, width=820, height=300, padx=20, relief=RIDGE
                                  , font=('arial', 12,'bold'), text="stark library Info:",)
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=10, width=350, height=300, padx=20, relief=RIDGE
                                  , font=('arial', 12,'bold'), text="Book Details:",)
        DataFrameRIGHT.pack(side=RIGHT)

        #===============================================Widget=============================================================================
        self.lblMemberType = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Member Type:", padx=2, pady=2 )
        self.lblMemberType .grid(row=0, column=0 ,sticky=W)

        self.cboMemberType = ttk.Combobox(DataFrameLEFT, font=('arial', 12, 'bold'),state='readonly', textvariable =MType, width =23 )
        self.cboMemberType['value']=('','student','lecturer','Admin Staff')
        self.cboMemberType.current(0)
        self.cboMemberType .grid(row=0, column=1)

        self.lblBookID = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Book ID:", padx=2, pady=2 )
        self.lblBookID .grid(row=0, column=2 ,sticky=W)
        self.txtBookID = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable =BookID, width =25)
        self.txtBookID .grid(row=0, column=3)

        self.lblRef = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Reference No:", padx=2, pady=2 )
        self.lblRef .grid(row=1, column=0 ,sticky=W)
        self.txtRef = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = Ref, width =25)
        self.txtRef .grid(row=1, column=1)

        self.lblBookTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Book Title:", padx=2, pady=2 )
        self.lblBookTitle .grid(row=1, column=2 ,sticky=W)
        self.txtBookTitle= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = BookTitle, width =25)
        self.txtBookTitle .grid(row=1, column=3)

        self.lblTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Title:", padx=2, pady=2 )
        self.lblTitle .grid(row=2, column=0 ,sticky=W)

        self.cboTitle=ttk.Combobox(DataFrameLEFT,textvariable=Title, state='readonly',
                                   font=('arial', 12, 'bold'), width=23)
        self.cboTitle['value']=('','Mr.','Miss.','Dr.','Capt.','Ms.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=2, column=1)

        self.lblAuthor = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Author:", padx=2, pady=2 )
        self.lblAuthor .grid(row=2, column=2 ,sticky=W)
        self.txtAuthor= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = Author, width =25)
        self.txtAuthor .grid(row=2, column=3)

        self.lblFirstname = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Firstname:", padx=2, pady=2 )
        self.lblFirstname .grid(row=3, column=0 ,sticky=W)
        self.txtFirstname= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = Firstname, width =25)
        self.txtFirstname .grid(row=3, column=1)

        self.lblDateBorrowed = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="DateBorrowed:", padx=2, pady=2 )
        self.lblDateBorrowed .grid(row=3, column=2 ,sticky=W)
        self.txtDateBorrowed= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = DateBorrowed, width =25)
        self.txtDateBorrowed .grid(row=3, column=3)

        self.lblSurname = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Surname:", padx=2, pady=2 )
        self.lblSurname .grid(row=4, column=0 ,sticky=W)
        self.txtSurname= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable=Surname, width =25)
        self.txtSurname .grid(row=4, column=1)

        self.lblDateDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="DateDue:", padx=2, pady=2 )
        self.lblDateDue .grid(row=4, column=2 ,sticky=W)
        self.txtDateDue= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable = DateDue, width =25)
        self.txtDateDue .grid(row=4, column=3)

        self.lblAddress1 = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Address1:", padx=2, pady=2 )
        self.lblAddress1 .grid(row=5, column=0 ,sticky=W)
        self.txtAddress1= Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable= Address1 ,width =25)
        self.txtAddress1 .grid(row=5, column=1)

        self.lblDaysOnLoan = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="DaysOnLoan:", padx=2, pady=2 )
        self.lblDaysOnLoan .grid(row=5, column=2 ,sticky=W)
        self.txtDaysOnLoan= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable= DaysOnLoan, width =25)
        self.txtDaysOnLoan .grid(row=5, column=3)

        self.lblAddress2 = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="Address2:", padx=2, pady=2 )
        self.lblAddress2 .grid(row=6, column=0 ,sticky=W)
        self.txtAddress2= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable=Address2, width =25)
        self.txtAddress2 .grid(row=6, column=1)

        self.lbllateReturnFine = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="lateReturnFine:", padx=2, pady=2 )
        self.lbllateReturnFine .grid(row=6, column=2 ,sticky=W)
        self.txtlateReturnFine= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable= lateReturnFine ,width =25)
        self.txtlateReturnFine .grid(row=6, column=3)

        self.lblPostCode = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="PostCode:", padx=2, pady=2 )
        self.lblPostCode .grid(row=7, column=0 ,sticky=W)
        self.txtPostCode= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable=PostCode, width =25)
        self.txtPostCode .grid(row=7, column=1)

        self.lblDateOverDue = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="DateOverDue:", padx=2, pady=2 )
        self.lblDateOverDue .grid(row=7, column=2 ,sticky=W)
        self.txtDateOverDue= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable=DateOverDue, width =25)
        self.txtDateOverDue .grid(row=7, column=3)

        self.lblMobileNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="MobileNo:", padx=2, pady=2 )
        self.lblMobileNo .grid(row=8, column=0 ,sticky=W)
        self.txtMobileNo= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable=MobileNo, width =25)
        self.txtMobileNo .grid(row=8, column=1)

        self.lblSellingPrice = Label(DataFrameLEFT, font=('arial', 12, 'bold'),text="SellingPrice:", padx=2, pady=2 )
        self.lblSellingPrice .grid(row=8, column=2 ,sticky=W)
        self.txtSellingPrice= Entry(DataFrameLEFT, font=('arial', 12, 'bold'),textvariable=SellingPrice, width =25)
        self.txtSellingPrice .grid(row=8, column=3)
        #==================================================Widgets==========================================================
        self.txtDisplayR =Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width =32, height=13, padx=8 ,pady=20)
        self.txtDisplayR .grid(row=0, column=2)
        #==================================================ListBooks=========================================================
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1,sticky='ns')

        
        ListOfBooks =['Ironman','Captain America','Thor','Justice league','Sherlock Holmes','Spiderman','Aquaman','Adventures of Wonder women',
                      'Shazam','Stranger Things','Dr.Strange','Arrow','The flash','The Vampire Diaries','Artificial Intelligence']

        def SelectedBooks(evt):
            value =str(booklist.get(booklist.curselection()))
            print(value)
            v=value
            
            if (v == "Ironman"):
                BookID.set("ISBN 748256565")
                BookTitle.set("story of Stark")
                Author.set("stan Lee")

                LateReturnFine.set("150 ruppees")
                SellingPrice.set("500 ruppess")
                DaysOnLoan.set(14)
                iReciept()

                import datetime

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateBorrowed.set(d1)
                DateDue.set(d3)
                DataOverDue.set("no")


                
        
        booklist = Listbox(DataFrameRIGHT, width=20, height=12,font=('arial', 12, 'bold'))
        booklist.bind('<<Listboxselect>>',SelectedBooks)
        booklist.grid(row=0, column=0,padx=8)
        scrollbar.config(command=booklist.yview)

        for items in ListOfBooks:
            booklist.insert(END,items)
        #====================================================================================================================
        self.lblLabel =Label(FrameDetail,font=('arial', 10,'bold'),pady=8,
        text="Member Type\tRefrence NO.\t Firstname\t Surname\t Address 1\t Address 2\
        \tPost Code\tBook Title\tDate Borrowed\t Days On Loan",)
        self.lblLabel.grid(row=0, column=0)

        self.txtisplayR =Text(FrameDetail, font=('arial', 12, 'bold'), width =121, height=3, padx=2 ,pady=4)
        self.txtisplayR .grid(row=1, column=0)
        
                                 
        
        #===================================================bUTTONS========================================================
        self.btnDisplayData=Button(ButtonFrame, text='Display Data',font=('arial', 12, 'bold'), width=30, bd=4, command=iDisplayData)
        self.btnDisplayData.grid(row=0,column=0)

        self.btnDelete=Button(ButtonFrame, text='Delete',font=('arial', 12, 'bold'), width=30, bd=4, command=iDelete)
        self.btnDelete.grid(row=0,column=1)

        self.btnReset=Button(ButtonFrame, text='Reset',font=('arial', 12, 'bold'), width=30, bd=4, command=iReset)
        self.btnReset.grid(row=0,column=2)

        self.btnExit=Button(ButtonFrame, text='Exit',font=('arial', 12, 'bold'), width=30, bd=4, command=iExit)
        self.btnExit.grid(row=0,column=3)


if __name__=='__main__':
    root =Tk()
    appliation = Library(root)
    root.mainloop()
