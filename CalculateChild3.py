from tkinter import *
from datetime import datetime
from tkinter import messagebox
class WindowChild3:
    def __init__(self,parent2):
        self.root =Toplevel(parent2)
        self.root.title("History operation of calculator")
        self.root.geometry("550x500+500+200")
        self.root.iconbitmap("calculator.ico")
        self.root.resizable(True,False)
        self.root.configure(background ="#E0FFFF")
        self.Login_inv_histor = StringVar()
        self.Password_inv_histor = StringVar()
        self.entryDates = StringVar()
        self.entryDatepo = StringVar()
        self.entrylog= StringVar()
        self.historyall= StringVar()
        self.ranning()

    """Creating interface tools"""
    def drow_widjet(self):
            Lable_auth = Label(self.root, text='History of operation', justify=CENTER, font="Console 20", bg="#E0FFFF")
            Lable_auth.grid(row=0, column=0,
                            sticky=W,
                            pady=0, padx=135)
            inputVarLoginh = Entry(self.root, textvariable=str(self.Login_inv_histor), width=30)
            self.Login_inv_histor.set(str("Enter existing login"))
            inputVarLoginh.grid(row=1, column=0,
                              sticky=W,
                              pady=10, padx=128)

            inputVarPasswordh = Entry(self.root, textvariable=str(self.Password_inv_histor), width=40)
            self.Password_inv_histor.set(str("Enter existing password"))
            inputVarPasswordh.grid(row=2, column=0,
                               sticky=W,
                               pady=1, padx=100)
            inputVarDates = Entry(self.root, textvariable=str(self.entryDates), width=20)
            self.entryDates.set(str("1900-01-01"))
            inputVarDates.grid(row=6, column=0,
                               sticky=W,
                               pady=10, padx=100)

            inputVarDatepo = Entry(self.root, textvariable=str(self.entryDatepo), width=20)
            self.entryDatepo.set(str("3500-01-01"))
            inputVarDatepo.grid(row=8, column=0,
                               sticky=W,
                               pady=10, padx=100)

            self.make_button_history('Show history').grid(row=6, column=0)

    def make_button_history(self,digit):
        return Button(self.root, text=digit, bd='5',font=('Arial',8),command=self.my_dict_for_history_fin)

    """Functions for displaying the formation of the history of actions"""

    def my_dict_for_history(self):
            myDict = {}
            with open("dataoutput2.txt") as file:
                item_user =self.print_history()
                for line in file:
                    if item_user in line:
                        for line1 in line:
                            key_value = line.rstrip('\n').split(":")
                            if len(key_value) == 2:
                                myDict[key_value[0]] = key_value[1]

            return myDict

    def my_dict_for_history_write(self):
        with open("database.txt", "a") as f:
            f.truncate(0)
        dict = self.my_dict_for_history()
        dates = datetime.strptime(str(self.entryDates.get()), "%Y-%m-%d").date()#self.entryDates.get()
        datepo = datetime.strptime(str(self.entryDatepo.get()), "%Y-%m-%d").date()#self.entryDatepo.get()
        for key in dict:
            key2 = datetime.strptime(str(key)[:10], "%Y-%m-%d").date()
            if key2 >= dates and key2 <= datepo:
                key2 = key
                for name, age in dict.items():
                    if name == key2:
                        log_user = name + ':' + age + ';'
                        with open("database.txt", "a") as f:
                            for i in log_user:
                                f.write(f"{i}")

    def my_dict_for_history_fin(self):
        self.my_dict_for_history_write()
        with open("database.txt", "r") as f:
            file_r = f.read()
            f.close()
        return messagebox.showinfo("Your operation",file_r.replace(';','\n'))

    def print_history(self):
        user_list = [self.Login_inv_histor.get(), self.Password_inv_histor.get()]
        for index, i in enumerate(user_list[:-1]):
            item_user = i + user_list[index + 1]
            return item_user

    """Begin window launch"""
    def ranning(self):
        self.drow_widjet()
