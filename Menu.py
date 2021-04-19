try:
    import Tkinter as tk
except:
    import tkinter as tk

import update as up
import add_to_db as add_inven
import generate_bill as ge_bill
import view
class Menu():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("NMIMS's Inventory Management System")
        self.root.geometry("1366x768+0+0")
        self.heading = tk.Label(self.root, text="NMIMS's Inventory Management System", font=('arial 40 bold'), fg='steelblue')
        self.heading.place(x=200, y=0)
        exit_button = tk.Button(self.root, text="Quit", width=30, height=2, bg='red', fg='white',
                                  command=self.quit)
        update = tk.Button(self.root, text="Update Inventory", width=30, height=2, bg='orange', command=self.update)
        add_inventory = tk.Button(self.root, text="Add Some Inventory", width=30, height=2, bg='orange', command=self.add_inventory)
        billing = tk.Button(self.root, text="Generate Bill", width=30, height=2, bg='orange',
                                  command=self.generate_bill)
        view = tk.Button(self.root, text="View Inventory", width=30, height=2, bg='orange',
                            command=self.view_in)
        view.place(x = 550, y = 150)
        update.place(x = 550, y = 220)
        add_inventory.place(x = 550, y = 290)
        billing.place(x = 550, y = 360)
        exit_button.place(x=550, y=430)
        self.root.mainloop()

    def view_in(self):
        view.View()

    def update(self):
        rooting = tk.Tk()
        b = up.Database(rooting)
        rooting.geometry("1366x768+0+0")
        rooting.title("NMIMS's Inventory Management System")
        rooting.mainloop()

    def quit(self):
        self.root.destroy()

    def add_inventory(self):
        rooting = tk.Tk()
        b = add_inven.Database(rooting)
        rooting.geometry("1366x768+0+0")
        rooting.title("NMIMS's Inventory Management System")
        rooting.mainloop()

    def generate_bill(self):
        rooting = tk.Tk()
        ge_bill.Application(rooting)
        rooting.geometry("1366x768+0+0")
        rooting.title("NMIMS's Inventory Management System")
        rooting.mainloop()


app = Menu()