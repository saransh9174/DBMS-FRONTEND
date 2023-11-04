import tkinter
import mysql.connector

con=mysql.connector.connect(host="localhost",user="root",password="admin")
cur=con.cursor(buffered=True)
try:
    cur.execute("use registration")  #DB name
except:
    cur.execute("create database registration")
    cur.execute("use registration")
try:
    cur.execute("describe test") #table
except:

    cur.execute("create table test(id int,name varchar(20),age int,gender varchar(20),email varchar(320),mobile varchar(10))") #creating table


def Registration():
    cur.execute(f"insert into test(id,name,age,gender,email,mobile) values('{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{e6.get()}')") #attributes
    con.commit()
win=tkinter.Tk()
win.geometry("500x500")
win.title("DBMS Project")
l1=tkinter.Label(win,text="id")
l2=tkinter.Label(win,text="NAME")
l3=tkinter.Label(win,text="AGE")
l4=tkinter.Label(win,text="GENDER")
l5=tkinter.Label(win,text="EMAIL")
l6=tkinter.Label(win,text="MOBILE")

l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
l3.grid(row=3,column=1)
l4.grid(row=4,column=1)
l5.grid(row=5,column=1)
l6.grid(row=6,column=1)

e1=tkinter.Entry(win)
e2=tkinter.Entry(win)
e3=tkinter.Entry(win)
e4=tkinter.Entry(win)
e5=tkinter.Entry(win)
e6=tkinter.Entry(win)


e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
e3.grid(row=3,column=2)
e4.grid(row=4,column=2)
e5.grid(row=5,column=2)
e6.grid(row=6,column=2)



b=tkinter.Button(win,text="Submit Here",command=Registration)
b.grid(row=9,column=1)
win.mainloop()