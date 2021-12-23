from tkinter import *
from CalculateChild import WindowChild
from CalculateChild2 import WindowChild2
from CalculateChild3 import WindowChild3
from tkinter import messagebox as msg
from datetime import datetime

class Window:
    def __init__(self):
        self.root = Tk()
        self.root.title("Online calculator")
        self.root.geometry("450x500+500+200")
        self.root.iconbitmap("calculator.ico")
        self.root.resizable(True,False)
        self.root.configure(background ="#E0FFFF")
        self.Login_inv= StringVar()
        self.Password_inv = StringVar()
        self.login_reg = StringVar()
        self.password_reg = StringVar()
        self.root.grid_columnconfigure(0, minsize=60)
        self.root.grid_rowconfigure(0, minsize=60)
        """Button for authorize/registration """
        self.button0 = Button(text='Enter', command=self.create_child)
        self.button0.grid(row=8, column=0)
        self.button1 = Button(text='Without Registration', command=self.enter_child2)
        self.button1.grid(row=9, column=0,pady=10)
        self.button2 = Button(text=' History operation ', command=self.enter_child3)
        self.button2.grid(row=10, column=0,pady=3)
        self.data_log=self.data_operday()
        my_file = open("dataoutput2.txt", "a")
        my_file.close()
        my_file2 = open("database.txt", "a")
        my_file2.close()

    def data_operday(self):
        current_microsecond = datetime.now().microsecond
        current_datetime = datetime.now().date()
        all_time = f'{current_datetime} .{current_microsecond}'
        return all_time
    """Registration check"""
    def check_registr(self):
        Lable_ref = Label(self.root, text='After Registration click Enter', justify=CENTER, font="Console 10", bg="#E0FFFF")
        Lable_ref.grid(row=24, column=0, pady=10)
        entryLogin = Entry(self.root, textvariable=str(self.Login_inv))
        entryLogin.grid(row=16, column=0)
        entryPassword = Entry(self.root, textvariable=str(self.Password_inv))
        entryPassword.grid(row=19, column=0,pady=2)
        answer = msg.askyesno(
            title="Registration Yes or no",
            message="Registration now?")
        if answer:
            with open("dataoutput2.txt", mode='r', encoding='utf-8') as f:
                user_list = [self.Login_inv.get(), self.Password_inv.get()]
                for index, i in enumerate(user_list[:-1]):
                    item_user = i + user_list[index + 1]
                if item_user not in f.read():
                     Button_reg = Button(text='Enter/Registration', command=self.writetofileforreg)#writetofile
                     Button_reg.grid(row=20, column=0)

    """Creation of simple calculator for  authorized users"""

    def enter_child(self):
        WindowChild(self.root)
    """Creation of simple calculator for not authorized users with out registrate and history"""
    def enter_child2(self):
        WindowChild2(self.root)

    def enter_child3(self):
        WindowChild3(self.root)

    """Launch the interface"""
    def ranning(self):

            self.drow_widjet()
            self.root.mainloop()

    """Creation of an advanced calculator for authorized users with registrate"""
    def create_child(self):

        with open("dataoutput2.txt", mode='r', encoding='utf-8') as f:
            user_list = [self.Login_inv.get(), self.Password_inv.get()]
            for index, i in enumerate(user_list[:-1]):
                item_user=i+user_list[index+1]
            if  item_user in f.read():
                WindowChild(self.root)
                self.writetofile()
            elif item_user not in f.read():
                self.check_registr()
            else:
                self.enter_child2()
    """Creating widgets Label/Entry"""
    def drow_widjet(self):

        Lable_auth = Label(self.root, text='Authorization', justify=CENTER, font="Console 20", bg="#E0FFFF")
        Lable_auth.grid(row=0, column=0,
                        sticky=W,
                        pady=0, padx=135)
        inputVarLogin = Entry(self.root, textvariable=str(self.Login_inv),width=30)
        self.Login_inv.set(str("Enter existing login or create new"))
        inputVarLogin.grid(row=1, column=0,
                        sticky=W,
                        pady=10, padx=128)

        inputVarPassword = Entry(self.root, textvariable=str(self.Password_inv),width=40)
        self.Password_inv.set(str("Enter existing password or create new"))
        inputVarPassword.grid(row=2, column=0,
                        sticky=W,
                        pady=1, padx=100)
    """Writing login and password to file"""
    def writetofile(self):

        content_list = [self.Login_inv.get(),self.Password_inv.get()]
        with open("dataoutput2.txt", "a") as f:
            for index, i in enumerate(content_list[:-1]):
                item=i+content_list[index+1]
                f.write(f"{self.data_operday()}:{item}")
                f.close()
    def writetofileforreg(self):

        content_list = [self.Login_inv.get(),self.Password_inv.get()]
        with open("dataoutput2.txt", "a") as f:
            for index, i in enumerate(content_list[:-1]):
                item=i+content_list[index+1]
                f.write(f"\n{self.data_operday()}:{item} -User registration successful\n ")
                f.close()

    def forwriteLogin_inv_r(self):
        Login_inv_r=self.Login_inv.get()
        return print(Login_inv_r)

"""Start the class"""
window = Window()
window.ranning()
