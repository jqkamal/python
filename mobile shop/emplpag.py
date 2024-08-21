import tkinter as tk
import sqlite3
from tkinter import messagebox
parent=tk.Tk()
def validate():
    parent.destroy()
    import addmobile
parent.title("Welcome emplyee page")
login_button=tk.Button(parent,text="Add mobiles",command=validate)
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
    import emplpag
login_button=tk.Button(parent,text="logout",command=log)
login_button.pack()

parent.mainloop()
