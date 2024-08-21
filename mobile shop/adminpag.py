import tkinter as tk
import sqlite3
from tkinter import messagebox
parent=tk.Tk()

def validate():
    parent.destroy()
    import empldetel
parent.title("welcome Admin")
login_button=tk.Button(parent,text="employee details",command=validate)
login_button.pack()
def add():
    parent.destroy()
    import addmobile
login_button=tk.Button(parent,text="Add mobiles",command=add)
login_button.pack()
def sales():
    parent.destroy()
    import sale
login_button=tk.Button(parent,text="sales",command=sales)
login_button.pack()
def view():
    parent.destroy()
    import viewmobile
login_button=tk.Button(parent,text="View mobiles",command=view)
login_button.pack()
def log():
    parent.destroy()
    import logincr
login_button=tk.Button(parent,text="logout",command=log)
login_button.pack()
parent.mainloop()
