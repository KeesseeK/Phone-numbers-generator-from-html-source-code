<<<<<<< HEAD

import re
from tkinter import *
from matplotlib.pyplot import close, text
import sqlite3


#database functions
def connect():
    conn=sqlite3.connect("phone_numbers_database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS phone_numbers (id INTEGER PRIMARY KEY UNIQUE, phone_number VARCHAR(22) UNIQUE)")
    conn.commit()
    conn.close()

def insert(phone_number_input):
    conn=sqlite3.connect("phone_numbers_database.db")
    cur=conn.cursor()
    try:
        for item in phone_number_input:
            cur.execute("INSERT INTO phone_numbers VALUES (NULL,?)",(item,))
    except:
        pass
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("phone_numbers_database.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM phone_numbers")
    rows=cur.fetchall()
    return rows

#Searching for phone numbers
def search_for_hone_numbers(html_user_input):
    content = html_user_input.get()
    

    #digits of length 9
    def filterNumber(n):
        if(len(n)==9):
            return True
        else:
            return False



    #search using regex
    my_list = re.findall('[0-9]+', content)


    #filter the list
    filtered_my_list = [int(s) for s in set(filter(filterNumber, my_list))]

    filtered_my_list_final = [i for i in filtered_my_list if i >= 500000000]

    return filtered_my_list_final



#Generate button funcion
def generate_command():
    connect()
    insert(search_for_hone_numbers(html_user_input))
    for row in view():
        list1.insert(END,row)

    


#Window
window=Tk()

l1=Label(window,text="Html code:")
l1.grid(row=0,column=0)

html_user_input=StringVar()
e1=Entry(window,textvariable=html_user_input)
e1.grid(row=0,column=1)

list1=Listbox(window,height=40,width=50)
list1.grid(row=2,column=0,columnspan=2,rowspan=10)

sb1=Scrollbar(window)
sb1.grid(row=1,column=2,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(text='Generate',width=12,height=30,command=generate_command)
b1.grid(row=2,column=3)




window.mainloop()
=======

import re
from tkinter import *
from matplotlib.pyplot import close, text
import sqlite3


#database functions
def connect():
    conn=sqlite3.connect("phone_numbers_database.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS phone_numbers (id INTEGER PRIMARY KEY UNIQUE, phone_number VARCHAR(22) UNIQUE)")
    conn.commit()
    conn.close()

def insert(phone_number_input):
    conn=sqlite3.connect("phone_numbers_database.db")
    cur=conn.cursor()
    for item in phone_number_input:
        cur.execute("INSERT INTO phone_numbers VALUES (NULL,?)",(item,))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("phone_numbers_database.db")
    cur=conn.cursor()
    cur.execute("SELECT phone_number FROM phone_numbers")
    rows=cur.fetchall()
    return rows

#Searching for phone numbers
def search_for_hone_numbers(html_user_input):
    content = html_user_input.get()
    

    #digits of length 9
    def filterNumber(n):
        if(len(n)==9):
            return True
        else:
            return False



    #search using regex
    my_list = re.findall('[0-9]+', content)


    #filter the list
    filtered_my_list = [int(s) for s in set(filter(filterNumber, my_list))]

    filtered_my_list_final = [i for i in filtered_my_list if i >= 500000000]

    return filtered_my_list_final



#Generate button funcion
def generate_command():
    connect()
    insert(search_for_hone_numbers(html_user_input))
    for row in view():
        list1.insert(END,row)

    


#Window
window=Tk()

l1=Label(window,text="Html code:")
l1.grid(row=0,column=0)

html_user_input=StringVar()
e1=Entry(window,textvariable=html_user_input)
e1.grid(row=0,column=1)

list1=Listbox(window,height=40,width=50)
list1.grid(row=2,column=0,columnspan=2,rowspan=10)

sb1=Scrollbar(window)
sb1.grid(row=1,column=2,rowspan=10)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(text='Generate',width=12,height=30,command=generate_command)
b1.grid(row=2,column=3)




window.mainloop()
>>>>>>> c173ad2df87252901a09a122c121da9cd5d5f6c1
