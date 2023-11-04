import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
con=mysql.connector.connect(host="localhost",user="root",password="admin")
cur=con.cursor(buffered=True)
try:
    cur.execute("use mini_project")  #DB name
except:
    cur.execute("create database mini_project")
    cur.execute("use mini_project")
try:
    cur.execute("describe year2016") #table
except:

    cur.execute("create table year2016(drug_code int,country_code varchar(30),unit varchar(30),typical_rate int)") #creating table
def GetValue(event):
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    row_id = listBox.selection()[0]
    select = listBox.set(row_id)
    e1.insert(0,select['drug_code'])
    e2.insert(0,select['country_code'])
    e3.insert(0,select['unit'])
    e4.insert(0,select['typical_rate'])
 
 
def Add():
    drug_code = e1.get()
    country_code = e2.get()
    unit = e3.get()
    typical_rate = e4.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="admin",database="mini_project")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "INSERT INTO  year2016 (drug_code,country_code,unit,typical_rate) VALUES (%s, %s, %s, %s)"
       val = (drug_code,country_code,unit,typical_rate)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Information", "Entry inserted successfully...")
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
    except Exception as e:
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
 
def update():
    drug_code = e1.get()
    country_code = e2.get()
    unit = e3.get()
    typical_rate = e4.get()
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="admin",database="mini_project")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "Update  year2016 set country_code= %s,unit= %s,typical_rate= %s where drug_code= %s"
       val = (country_code,unit,typical_rate,drug_code)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Information", "Record Updateddddd successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)

       e4.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def delete():
    drug_code = e1.get()
 
    mysqldb=mysql.connector.connect(host="localhost",user="root",password="admin",database="mini_project")
    mycursor=mysqldb.cursor()
 
    try:
       sql = "delete from year2016 where drug_code = %s"
       val = (drug_code,)
       mycursor.execute(sql, val)
       mysqldb.commit()
       lastid = mycursor.lastrowid
       messagebox.showinfo("Information", "Record Deleteeeee successfully...")
 
       e1.delete(0, END)
       e2.delete(0, END)
       e3.delete(0, END)
       e4.delete(0, END)
       e1.focus_set()
 
    except Exception as e:
 
       print(e)
       mysqldb.rollback()
       mysqldb.close()
 
def show():

        mysqldb = mysql.connector.connect(host="localhost", user="root", password="admin",database="mini_project")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT drug_code,country_code,unit,typical_rate FROM year2016")
        records = mycursor.fetchall()
        print(records)
 
        for i, (drug_code, country_code, unit, typical_rate) in enumerate(records, start=1):
            listBox.insert("", "end", values=(drug_code, country_code, unit, typical_rate))
            mysqldb.close()
 
root = Tk()
root.geometry("800x500")
global e1
global e2
global e3
global e4
 
tk.Label(root, text="Walter White and Co.", fg="red", font=(None, 30)).place(x=300, y=5)
 
tk.Label(root, text="Drug Code").place(x=10, y=10)
Label(root, text="Country Code").place(x=10, y=40)
Label(root, text="Unit").place(x=10, y=70)
Label(root, text="Typical Rate").place(x=10, y=100)
 
e1 = Entry(root)
e1.place(x=140, y=10)
 
e2 = Entry(root)
e2.place(x=140, y=40)
 
e3 = Entry(root)
e3.place(x=140, y=70)
 
e4 = Entry(root)
e4.place(x=140, y=100)
 
Button(root, text="Add",command = Add,height=3, width= 13).place(x=30, y=130)
Button(root, text="update",command = update,height=3, width= 13).place(x=140, y=130)
Button(root, text="Delete",command = delete,height=3, width= 13).place(x=250, y=130)
 
cols = ('drug_code', 'country_code', 'unit','typical_rate')
listBox = ttk.Treeview(root, columns=cols, show='headings' )
 
for col in cols:
    listBox.heading(col, text=col)
    listBox.grid(row=1, column=0, columnspan=2)
    listBox.place(x=10, y=200)
 
show()
listBox.bind('<Double-Button-1>',GetValue)
 
root.mainloop()