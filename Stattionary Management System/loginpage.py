from tkinter import *
from functools import partial
from tkinter.font import BOLD
from tkinter import messagebox
import re
import pymysql

def logout():
    root.destroy()
    import SMS.py
root = Tk()  
root.resizable("false","false")
root.geometry('1200x800')  
root.title('Stationary Management System')
def searching():
    con = pymysql.connect(host="localhost", user="root", password="", database="sufyan" )
    cur = con.cursor()
    cur.execute("select * from items where product=%s",(search.get()))
    row = cur.fetchall()
    print(row)

def usernasmes():
    title = Label(mainframe,foreground="white",bg="red",font=("times new roman",28,BOLD), text="Welcome To Our Shop")
    title.place(x=450,y=20)

    title['text']=(row)




mainframe = Frame(root, width=1200, height=800, bg="red").pack()
search = Entry(mainframe, width=30, highlightcolor="yellow")
search.place(x=750,y=20)
serachbtn = Button(mainframe, text="search", width=50, command=searching)
serachbtn.place(x=800,y=20)

logoutButton = Button(mainframe, text="Logout", font=("arial", 12, BOLD), command=logout)
logoutButton.place(x=1050, y=10 , width=130)


    
root.mainloop()