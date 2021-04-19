import mysql.connector
import tkinter as tk
from tkinter import *

class View:
    def __init__(self):
        root = tk.Tk()
        root.title("NMIMS's View Database")
        root.geometry("1366x768+0+0")
        my_connect = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="inventory_system"
        )
        my_conn = my_connect.cursor()

        my_conn.execute("SELECT * FROM inventory")
        i = 1
        e = Entry(root, width=10, fg='blue')
        e.grid(row=0, column=0)
        e.insert(END, "Product ID")
        e = Entry(root, width=20, fg='blue',
                  font=('Arial', 16, 'bold'))

        e = Entry(root, width=10, fg='blue')
        e.grid(row=0, column=1)
        e.insert(END, "Product Name")
        e = Entry(root, width=20, fg='blue',
                  font=('Arial', 16, 'bold'))

        e = Entry(root, width=10, fg='blue')
        e.grid(row=0, column=2)
        e.insert(END, "Product Stock")
        e = Entry(root, width=20, fg='blue',
                  font=('Arial', 16, 'bold'))

        e = Entry(root, width=10, fg='blue')
        e.grid(row=0, column=3)
        e.insert(END, "Product Price")
        e = Entry(root, width=20, fg='blue',
                  font=('Arial', 16, 'bold'))

        for student in my_conn:
            for j in range(len(student)):
                e = Entry(root, width=10, fg='blue')
                e.grid(row=i, column=j)
                e.insert(END, student[j])
                e = Entry(root, width=20, fg='blue',
                          font=('Arial', 16, 'bold'))

            i += 1
        root.mainloop()
