from tkinter import*
from tkinter import ttk
import random
import tkinter.messagebox
from datetime import datetime

class Hotel:

    def __init__(self,root):
        self.root=root
        self.root.title("stark resort")
        self.root.geometry("1350x750+0+0")
        self.root.config(background="powder blue")

        mainFrame =Frame(self.root)
        mainFrame.grid()

        TopFrame =Frame(mainFrame, bd=14 ,width=1350,height=550,padx=20 ,relief=RIDGE,bg="cadet Blue")
        TopFrame.pack(side=TOP)

        LeftFrame=Frame(TopFrame,bd=5,width=450,height=550,padx=2,relief=RIDGE,bg="powder blue")
        LeftFrame.pack(side=LEFT)

        RightFrame= Frame(TopFrame,bd=10,width=820,height=550,padx=2,relief=RIDGE,bg="cadet Blue")
        RightFrame.pack(side=RIGHT)

        BottomFrame=Frame(TopFrame,bd=10,width=1350,height=150,padx=20,relief=RIDGE,bg="powder blue")
        BottomFrame.pack(side=BOTTOM)

        CustomerRef =StringVar()
        Firstname =StringVar()
        Lastname =StringVar()
        Address=StringVar()
        PostCode=StringVar()
        Mobile=StringVar()
        Email=StringVar()
        Nationality=StringVar()
        DOB=StringVar()
        IDType=StringVar()
        Gender=StringVar()
        CheckInDate=StringVar()
        CheckOutDate=StringVar()
        Meal=StringVar()
        RoomType=StringVar()
        RoomNo=StringVar()
        TotalCost=StringVar()
        SubTotal=StringVar()
        PaidTax=StringVar()
        TotalDays=StringVar()
        """===================================Widgets========================================"""
        self.lblCustomer_Ref =Label(LeftFrame, font=('arial', 12, 'bold'),text="Customer Ref:",padx=2,bg="powder blue")
        self.lblCustomer_Ref.grid(row=0,column=0,sticky =W)
        self.txtCustomer_Ref =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =CustomerRef,width=20)
        self.txtCustomer_Ref.grid(row=0,column=1,pady=3,padx=20)

        self.lblFirstname =Label(LeftFrame, font=('arial', 12, 'bold'),text="Firstname: ",padx=2,bg="powder blue")
        self.lblFirstname.grid(row=1,column=0,sticky =W)
        self.txtFirstname =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =Firstname,width=20)
        self.txtFirstname.grid(row=1,column=1,pady=3,padx=20)

        self.lblLastname =Label(LeftFrame, font=('arial', 12, 'bold'),text="Lastname:",padx=2,bg="powder blue")
        self.lblLastname.grid(row=2,column=0,sticky =W)
        self.txtLastname =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =Lastname,width=20)
        self.txtLastname.grid(row=2,column=1,pady=3,padx=20)

        self.lblAddress =Label(LeftFrame, font=('arial', 12, 'bold'),text="Address:",padx=2,bg="powder blue")
        self.lblAddress.grid(row=3,column=0,sticky =W)
        self.txtAddress =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =Address,width=20)
        self.txtAddress.grid(row=3,column=1,pady=3,padx=20)

        self.lblPostCode =Label(LeftFrame, font=('arial', 12, 'bold'),text="PostCode:",padx=2,bg="powder blue")
        self.lblPostCode.grid(row=4,column=0,sticky =W)
        self.txtPostCode =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =PostCode,width=20)
        self.txtPostCode.grid(row=4,column=1,pady=3,padx=20)

        self.lblMobile =Label(LeftFrame, font=('arial', 12, 'bold'),text="Mobile:",padx=2,bg="powder blue")
        self.lblMobile.grid(row=5,column=0,sticky =W)
        self.txtMobile =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =Mobile,width=20)
        self.txtMobile.grid(row=5,column=1,pady=3,padx=20)

        self.lblEmail =Label(LeftFrame, font=('arial', 12, 'bold'),text="Email:",padx=2,bg="powder blue")
        self.lblEmail.grid(row=6,column=0,sticky =W)
        self.txtEmail=Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =Email,width=20)
        self.txtEmail.grid(row=6,column=1,pady=3,padx=20)

        self.lblNationality =Label(LeftFrame, font=('arial', 12, 'bold'),text="Nationality:",padx=2,pady=2,bg="powder blue")
        self.lblNationality.grid(row=7,column=0,sticky =W)
        self.cboNationality =ttk.Combobox(LeftFrame,textvariable =Nationality,state='readonly',font=('arial', 12, 'bold'),width=18)
        self.cboNationality['value'] =(' ','india','africa','america','UAE','Argentina','Southafrica','Australia')
        self.cboNationality.current(0)
        self.cboNationality.grid(row=7,column=1,pady=3,padx=20)

        self.lblDOB=Label(LeftFrame, font=('arial', 12, 'bold'),text="DOB:",padx=2,bg="powder blue")
        self.lblDOB.grid(row=8,column=0,sticky =W)
        self.txtDOB =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =DOB,width=20)
        self.txtDOB.grid(row=8,column=1,pady=3,padx=20)

        self.lblIDType =Label(LeftFrame, font=('arial', 12, 'bold'),text="IDType:",padx=2,bg="powder blue")
        self.lblIDType.grid(row=9,column=0,sticky =W)
        self.cboIDType =ttk.Combobox(LeftFrame,textvariable =IDType,state='readonly',font=('arial', 12, 'bold'),width=18)
        self.cboIDType['value'] =(' ','Driving License','Voter Card','Pan Card','Green Card','PassPort')
        self.cboIDType.current(0)
        self.cboIDType.grid(row=9,column=1,pady=3,padx=20)

        self.lblGender =Label(LeftFrame, font=('arial', 12, 'bold'),text="Gender:",padx=2,bg="powder blue")
        self.lblGender.grid(row=10,column=0,sticky =W)
        self.cboGender =ttk.Combobox(LeftFrame,textvariable =Gender,state='readonly',font=('arial', 12, 'bold'),width=18)
        self.cboGender['value'] =(' ','Male','Female','Other')
        self.cboGender.current(0)
        self.cboGender.grid(row=10,column=1,pady=3,padx=20)

        self.lblCheckInDate =Label(LeftFrame, font=('arial', 12, 'bold'),text="CheckInDate:",padx=2,bg="powder blue")
        self.lblCheckInDate.grid(row=11,column=0,sticky =W)
        self.txtCheckInDate =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =CheckInDate,width=20)
        self.txtCheckInDate.grid(row=11,column=1,pady=3,padx=20)

        self.lblCheckOutDate =Label(LeftFrame, font=('arial', 12, 'bold'),text="CheckOutDate:",padx=2,bg="powder blue")
        self.lblCheckOutDate.grid(row=12,column=0,sticky =W)
        self.txtCheckOutDate =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =CheckOutDate,width=20)
        self.txtCheckOutDate.grid(row=12,column=1,pady=3,padx=20)

        self.lblMeal =Label(LeftFrame, font=('arial', 12, 'bold'),text="Meal:",padx=2,bg="powder blue")
        self.lblMeal.grid(row=13,column=0,sticky =W)
        self.cboMeal =ttk.Combobox(LeftFrame,textvariable =Meal,state='readonly',font=('arial', 12, 'bold'),width=18)
        self.cboMeal['value'] =(' ','Breakfast','Lunch','Dinner')
        self.cboMeal.current(0)
        self.cboMeal.grid(row=13,column=1,pady=3,padx=20)

        self.lblRoomType =Label(LeftFrame, font=('arial', 12, 'bold'),text="RoomType:",padx=2,bg="powder blue")
        self.lblRoomType.grid(row=14,column=0,sticky =W)
        self.cboRoomType =ttk.Combobox(LeftFrame,textvariable =RoomType,state='readonly',font=('arial', 12, 'bold'),width=18)
        self.cboRoomType['value'] =(' ','Single','Double','Family')
        self.cboRoomType.current(0)
        self.cboRoomType.grid(row=14,column=1,pady=3,padx=20)

        self.lblRoomNo =Label(LeftFrame, font=('arial', 12, 'bold'),text="RoomNo:",padx=2,bg="powder blue")
        self.lblRoomNo.grid(row=15,column=0,sticky =W)
        self.txtRoomNo =Entry(LeftFrame, font=('arial', 12, 'bold'),textvariable =RoomNo,width=20)
        self.txtRoomNo.grid(row=15,column=1,pady=3,padx=20)

        """======================================Reciept====================================================================="""

        self.lblLabel = Label(RightFrame, font=('arial', 10, 'bold'),pady=10,bg="cadet Blue",
        text="Customer Ref\tFirstname\tLastname\tAddress\tPostCode\tMobile\tNationality\tCheckInDate\tCheckOutDate\t")
        self.lblLabel.grid(row =0,column=0,columnspan=17)
        
        self.txtReciept =Text(RightFrame, height=25,width=108,bd=10,font=('arial' ,11, 'bold',))
        self.txtReciept.grid(row=1,column=0,columnspan=2,padx=2,pady=5)
        """=====================================================Reciept======================================================="""
        self.lblDays=Label(RightFrame,font=('arial',14,'bold'), text="No. of Days",bd=7,bg="cadet Blue",fg="black",)
        self.lblDays.grid(row=2,column=0, sticky=W)
        self.txtDays = Entry(RightFrame,font=('arial', 14, 'bold'),textvariable=TotalDays,bd=7,bg="White",width=67,justify=LEFT)
        self.txtDays.grid(row=2,column=1)

        
        
        

if __name__=='__main__':
    root =Tk()
    application = Hotel(root)
    root.mainloop()
