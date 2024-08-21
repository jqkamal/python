import sqlite3
from tkinter import *
from tkinter import messagebox
parent=Tk()
def employe():
    uid=int(ids.get())
    pasw=pas.get()
    name=na.get()
    age=int(ag.get())
    gend=gen.get()
    add=ad.get()
    cont=int(con.get())
    eml=em.get()
    sly=int(sl.get())
    if (sly >10000 and sly <=25000):
        da=sly*2/100
        hr=sly*3/100
        ta=sly*2/100
        pf=sly*1/100
    elif(sly >25000 and sly <=50000):
         da=sly*3/100
         hr=sly*4/100
         ta=sly*3/100
         pf=sly*2/100
    elif(sly >50000 and sly <=100000):
        da=sly*4/100
        hr=sly*5/100
        ta=sly*4/100
        pf=sly*3/100
    else:
        da=sly*5/100
        hr=sly*6/100
        ta=sly*5/100
        pf=sly*4/100
    netsal=sly+da+hr+ta-pf
    daa.config(text=da)
    hra.config(text=hr)
    taa.config(text=ta)
    pff.config(text=pf)
    netsalary.config(text=netsal)
    conn=sqlite3.connect("ss.db")
    cursor=conn.cursor()
    cursor.execute("insert into employee(ids,na,ag,gen,pas,em,ad,con,sly)values(?,?,?,?,?,?,?,?,?)",(uid,name,age,gend,pasw,add,cont,eml,sly))
    conn.commit()
    print("records inserted....")
    conn.close()
empl=Label(parent,text="employe I'D").grid(row=0,column=0)
ids=Entry(parent)
ids.grid(row=0,column=1)
password=Label(parent,text="password").grid(row=1,column=0)
pas=Entry(parent,show="**")
pas.grid(row=1,column=1)
name=Label(parent,text="employe Name").grid(row=2,column=0)
na=Entry(parent)
na.grid(row=2,column=1)
ages=Label(parent,text="employe age").grid(row=3,column=0)
ag=Entry(parent)
ag.grid(row=3,column=1)
gender=Label(parent,text="employe gender").grid(row=4,column=0)
gen=Entry(parent)
gen.grid(row=4,column=1)
adds=Label(parent,text="employe address").grid(row=5,column=0)
ad=Entry(parent)
ad.grid(row=5,column=1)
conta=Label(parent,text="contacts").grid(row=6,column=0)
con=Entry(parent)
con.grid(row=6,column=1)
emal=Label(parent,text="Email").grid(row=7,column=0)
em=Entry(parent)
em.grid(row=7,column=1)
salary=Label(parent,text="salary").grid(row=8,column=0)
sl=Entry(parent)
sl.grid(row=8,column=1)
daa=Label(parent)
daa.grid(row=9,column=0)
hra=Label(parent)
hra.grid(row=10,column=0)
taa=Label(parent)
taa.grid(row=11,column=0)
pff=Label(parent)
pff.grid(row=12,column=0)
netsalary=Label(parent)
netsalary.grid(row=13,column=0)
b1=Button(parent,text="submit",command=employe).grid(row=14,column=1)
b2=Button(parent,text="cancel").grid(row=14,column=0)
parent.mainloop()
