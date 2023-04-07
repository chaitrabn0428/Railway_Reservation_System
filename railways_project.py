from tkinter import *
from PIL import ImageTk,Image

def open_window():
    top = Toplevel()
    top.title("Railways Reservation System")
    top.geometry("891x600")

    def details():
        down = Toplevel()
        down.title("Railways Reservation System")
        down.geometry("891x600")
        l1=Label(down,text=("Enter passenger Details"),font=("italic",30),fg="red",bg="white")
        l2=Label(down,text=("Mobile Number"),font=("italic",20),fg="black",bg="white")
        en2=Entry(down)
        l3=Label(down,text=("UPI ID"),font=("italic",20),fg="black",bg="white")
        en3=Entry(down)
        l4=Label(down,text=("Full Name"),font=("italic",20),fg="black",bg="white")
        en4=Entry(down)
        l5=Label(down,text=("Age"),font=("italic",20),fg="black",bg="white")
        en5=Entry(down)
        l6=Label(down,text=("Gender"),font=("italic",20),fg="black",bg="white")
        en6=Entry(down)
       
        def congrats():
            up = Toplevel()
            up.title("Railways Reservation System")
            up.geometry("891x600")

            def print_ticket():
                pt = Toplevel()
                pt.title("Railways Reservation System")
                pt.geometry("891x600")
                From=from_entry.get()
                To=to_entry.get()
                Date=date_entry.get()
                Name=en4.get()
                Age=en5.get()
                Gender=en6.get()
                
                l1=Label(pt,text=("INDIAN RAILWAYS"),font=("italic",30),fg="red",bg="white")
                l2=Label(pt,text=("TICKET DETAILS"),font=("italic",30),fg="red",bg="white")
                
                l3=Label(pt,text=("From:"),font=("italic",30),fg="red",bg="white")
                l4=Label(pt,text=From,font=("italic",30),fg="red",bg="white")

                l5=Label(pt,text=("To:"),font=("italic",30),fg="red",bg="white")
                l6=Label(pt,text=To,font=("italic",30),fg="red",bg="white")
                
                l7=Label(pt,text=("Date:"),font=("italic",30),fg="red",bg="white")
                l8=Label(pt,text=Date,font=("italic",30),fg="red",bg="white")
                
                l9=Label(pt,text=("Name:"),font=("italic",30),fg="red",bg="white")
                l10=Label(pt,text=Name,font=("italic",30),fg="red",bg="white")

                l11=Label(pt,text=("Age:"),font=("italic",30),fg="red",bg="white")
                l12=Label(pt,text=Age,font=("italic",30),fg="red",bg="white")

                l13=Label(pt,text=("Gender:"),font=("italic",30),fg="red",bg="white")
                l14=Label(pt,text=Gender,font=("italic",30),fg="red",bg="white")
                
                l15=Label(pt,text=("THANK YOU!"),font=("italic",30),fg="blue",bg="white")


                pt.configure(bg='white')
                
                l1.grid(row=0,column=1)
                l2.grid(row=6,column=0)
                l3.grid(row=7,column=0)
                l4.grid(row=7,column=1)
                l5.grid(row=8,column=0)
                l6.grid(row=8,column=1)
                
                l7.grid(row=9,column=0)
                l8.grid(row=9,column=1)
                l9.grid(row=10,column=0)
                l10.grid(row=10,column=1)
                l11.grid(row=11,column=0)
                l12.grid(row=11,column=1)
                l13.grid(row=12,column=0)
                l14.grid(row=12,column=1)
                
                l15.grid(row=14,column=1)



            up.configure(bg='white')

            l2=Label(up,text="Congratulations!!!",font=("italic",30),fg="black",bg="white")
            l3=Label(up,text="your seat is reserved",font=("italic",30),fg="black",bg="white")
            b1=Button(up,text="print ticket",font=("italic",15),fg="red",bg="white",borderwidth = 3,width=10, relief="sunken",command=print_ticket)
            l2.grid(row=2,column=3)
            l3.grid(row=3,column=3)
            b1.grid(row=5,column=3)
        

        down.configure(bg='white')
        b2=Button(down,text="Confirm",font=("italic",15),fg="red",bg="white",borderwidth = 3,width=10, relief="sunken",command=congrats)
        b3=Label(down,text="Once you enter your UPI ID ",font=("italic",15),fg="black",bg="white")
        b4=Label(down,text="go to the app and pay to confirm your ticket",font=("italic",15),fg="black",bg="white")


        l1.grid(row=0,column=1)
        l2.grid(row=6,column=0)
        en2.grid(row=6,column=1)
        l3.grid(row=7,column=0)
        en3.grid(row=7,column=1)
        l4.grid(row=3,column=0)
        en4.grid(row=3,column=1)
        l5.grid(row=4,column=0)
        en5.grid(row=4,column=1)
        l6.grid(row=5,column=0)
        en6.grid(row=5,column=1)       

        b2.grid(row=10,column=0)
        b3.grid(row=11,column=0)
        b4.grid(row=12,column=0)

    top.configure(bg='white')
    From=from_entry.get()
    To=to_entry.get()
    Date=date_entry.get()


    l1=Label(top,text="Available Trains",font=("Calibri",30),fg="red",bg="white")
    l2=Label(top,text="PANCHA GANGA EXPRESS",font=("Algerian",20),fg="black",bg="white")
    l3=Label(top,text="Train Number:101102",font=("Algerian",10),fg="black",bg="white")
    l4=Label(top,text="From: "+From+" To: "+To,font=("Algerian",10),fg="black",bg="white")
    l5=Label(top,text="Amount:2000/person",font=("Algerian",10),fg="black",bg="white")
    l6=Label(top,text=Date,font=("Algerian",10),fg="black",bg="white")
    b1=Button(top,text="Book now",font=("Algerian",15),fg="red",bg="white",borderwidth = 3,width=10, relief="sunken",command=details)

    l7=Label(top,text="SHATABDI EXPRESS",font=("Algerian",20),fg="black",bg="white")
    l8=Label(top,text="Train Number:101103",font=("Algerian",10),fg="black",bg="white")
    l9=Label(top,text="From: "+From+" To: "+To,font=("Algerian",10),fg="black",bg="white")
    l10=Label(top,text="Amount:1500/person",font=("Algerian",10),fg="black",bg="white")
    l11=Label(top,text=Date,font=("Algerian",10),fg="black",bg="white")
    b2=Button(top,text="Book now",font=("Algerian",15),fg="red",bg="white",borderwidth = 3,width=10, relief="sunken",command=details)

    l12=Label(top,text="VANDE MAATHRAM EXPRESS",font=("Algerian",20),fg="black",bg="white")
    l13=Label(top,text="Train Number:192928",font=("Algerian",10),fg="black",bg="white")
    l14=Label(top,text="From: "+From+" To: "+To,font=("Algerian",10),fg="black",bg="white")
    l15=Label(top,text="Amount:1500/person",font=("Algerian",10),fg="black",bg="white")
    l16=Label(top,text=Date,font=("Algerian",10),fg="black",bg="white")
    b3=Button(top,text="Book now",font=("Algerian",15),fg="red",bg="white",borderwidth = 3,width=10, relief="sunken",command=details)

    l17=Label(top,text="RAAJADHANI EXPRESS",font=("Algerian",20),fg="black",bg="white")
    l18=Label(top,text="Train Number:291904",font=("Algerian",10),fg="black",bg="white")
    l19=Label(top,text="From: "+From+" To: "+To,font=("Algerian",10),fg="black",bg="white")
    l20=Label(top,text="Amount:1500/person",font=("Algerian",10),fg="black",bg="white")
    l21=Label(top,text=Date,font=("Algerian",10),fg="black",bg="white")
    b4=Button(top,text="Book now",font=("Algerian",15),fg="red",bg="white",borderwidth = 3,width=10, relief="sunken",command=details)


    l1.grid(row=0,column=0)
    l2.grid(row=3,column=0)
    l3.grid(row=4,column=0)
    l4.grid(row=5,column=0)
    l5.grid(row=6,column=0)
    l6.grid(row=7,column=0)
    b1.grid(row=8,column=0)

    l7.grid(row=12,column=0)
    l8.grid(row=13,column=0)
    l9.grid(row=14,column=0)
    l10.grid(row=15,column=0)
    l11.grid(row=16,column=0)
    b2.grid(row=17,column=0)

    l12.grid(row=3,column=3)
    l13.grid(row=4,column=3)
    l14.grid(row=5,column=3)
    l15.grid(row=6,column=3)
    l16.grid(row=7,column=3)
    b3.grid(row=8,column=3)

    l17.grid(row=12,column=3)
    l18.grid(row=13,column=3)
    l19.grid(row=14,column=3)
    l20.grid(row=15,column=3)
    l21.grid(row=16,column=3)
    b4.grid(row=17,column=3)

root = Tk()
root.title('Railways Reservation System')

image=Image.open("C:\\Users\\win10\\Desktop\\sem1\\python_project\\bg.jpeg")
back_end=ImageTk.PhotoImage(image)

label=Label(root,image=back_end)
label.place(x=0,y=0)

l1=Label(root,text="Welcome to Indian Railways",font=("Algerian",30),fg="black",bg="white") 
l2=Label(root,text="Search Train",font=("Algerian",25),fg="red",bg="white")

l1.grid(row=1,column=1, pady=10) 
l2.grid(row=6,column=0,padx=10, pady=10)

from_label = Label(root, text="From:",font=("Algerian",20),bg="white")
from_label.grid(row=7, column=0)
from_entry = Entry(root,text="From")
from_entry.grid(row=7, column=1)

to_label = Label(root, text="To:",font=("Algerian",20),bg="white")
to_label.grid(row=8, column=0)
to_entry = Entry(root,text="To")
to_entry.grid(row=8, column=1)

date_label = Label(root, text="Date:",font=("Algerian",20),bg="white")
date_label.grid(row=9, column=0)
date_entry = Entry(root)
date_entry.grid(row=9, column=1)

search = Button(root, text="Search",font=("Algerian",10),fg="red",bg="white",borderwidth = 3,width=10, relief="sunken", command=open_window)
search.grid(row=13, column=1)

root.geometry("891x600")
root.mainloop()