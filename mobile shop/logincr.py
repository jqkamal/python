import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox
parent=tk.Tk()
def validate_login():
    userid=username_entry.get()
    password=password_entry.get()
    conn=sqlite3.connect('ss.db')
    cursor=conn.cursor()
    cursor.execute(f"SELECT*from employee where ids='(userid)'and pas='(password)'")
    
    if userid=="admin" and password=="admin":
        messagebox.showinfo("Login Successful","Welcome Admin !")
        parent.destroy()
        import adminpag
    elif not cursor.fetchone():
        messagebox.showerror("login Failed","Invalid username or password")
    else:
        messagebox.showinfo("login successful","welcome !")
        

parent.title("login form")
username_label=tk.Label(parent,text="Userid:")
username_label.pack()
username_entry=tk.Entry(parent)
username_entry.pack()
password_label=tk.Label(parent,text="password:")
password_label.pack()
password_entry=tk.Entry(parent,show="*")
password_entry.pack()
login_button=tk.Button(parent,text="Login",command=validate_login)
login_button.pack()
parent.mainloop()
        
