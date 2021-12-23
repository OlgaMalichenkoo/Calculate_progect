from tkinter import *
import math
from tkinter import messagebox
class WindowChild:
    def __init__(self,parent):
        self.root =Toplevel(parent)
        self.root.title("Online calculator")
        self.root.geometry("670x700+20+20")
        self.root.iconbitmap("calculator.ico")
        self.root.resizable(True,False)
        self.root.configure(background ="#E0FFFF")
        self.message = StringVar()
        self.ranning()

    """Calling functions to record user actions"""

    def call_all_funcsforwrite(self):
        self.writetofile()
        self.Equals_equation()
        self.writetofile2()

    def call_all_trigonometrsin(self):
        self.trigonometry_func_sin()
        self.writetofile2()

    def call_all_trigonometrcos(self):
        self.trigonometry_func_cos()
        self.writetofile2()

    def call_all_trigonometrtang(self):
        self.trigonometry_func_tang()
        self.writetofile2()

    def call_all_trigonometrcotang(self):
        self.trigonometry_func_cotang()
        self.writetofile2()

    def writetofile(self):
        content_list = [self.message.get()]
        with open("dataoutput2.txt", "a") as f:
            for i in content_list:
                item = i
                f.write(f" operation=>{item}")
                f.close()

    def writetofile2(self):
        content_list = [self.message.get()]
        with open("dataoutput2.txt", "a") as f:
            for i in content_list:
                item = i
                f.write(f"={item};")
                f.close()

    def writetofileend(self):
        with open("dataoutput2.txt", "a") as f:
            f.write(f"\n")
            f.close()
    """Creating and working buttons"""
    def make_button_number(self,digit):
        return Button(self.root, text=digit, bd='5',font=('Arial',15),command=lambda : self.add_number(digit))

    def make_button_close(self,digit):
        return Button(self.root, text=digit, bd='5',font=('Arial',15),command=self.close_window())

    def make_button_operation(self,action):
        return Button(self.root, text=action, bd='5',font=('Arial',15),fg='blue',command=lambda : self.add_operfornumber(action))

    def make_button_clear(self, action):
        return Button(self.root, text=action, bd='5', font=('Arial', 15), fg='blue'
                      , command=self.Equals_clearing)
    def make_button_calc(self, action):
        return Button(self.root, text=action, bd='5', font=('Arial', 15), fg='blue'
                      , command=self.call_all_funcsforwrite) #"""Equals_equation"""
    def trigonometry_func_calc_sin(self, action):
        return Button(self.root, text=action, bd='5', font=('Arial', 15), fg='blue'
                      , command=self.call_all_trigonometrsin)
    def trigonometry_func_calc_cos(self, action):
        return Button(self.root, text=action, bd='5', font=('Arial', 15), fg='blue'
                      , command=self.call_all_trigonometrcos)
    def trigonometry_func_calc_tang(self, action):
        return Button(self.root, text=action, bd='5', font=('Arial', 15), fg='blue'
                      , command=self.call_all_trigonometrtang)
    def trigonometry_func_calc_cotang(self, action):
        return Button(self.root, text=action, bd='5', font=('Arial', 15), fg='blue'
                      , command=self.call_all_trigonometrcotang)
    """Creating interface tools"""
    def drow_widjet(self):
        self.inputVarName3 = Entry(self.root,justify=RIGHT,font=('Arial',20),width=40,textvariable=str(self.message))
        self.inputVarName3.insert(0,'0')
        self.inputVarName3.grid(row=0,column=0,columnspan=7,stick='wens',padx=20)
        self.make_button_number('1').grid(row=1,column=0, stick="wens", pady=10,padx=10)
        self.make_button_number('2').grid(row=1, column=1, stick="wens",pady=10,padx=10)
        self.make_button_number('3').grid(row=1, column=2, stick="wens",pady=10,padx=10)
        self.make_button_number('4').grid(row=1, column=3, stick="wens",pady=10,padx=10)
        self.make_button_number('5').grid(row=1, column=4, stick="wens",pady=10,padx=10)
        self.make_button_number('6').grid(row=1, column=5, stick="wens",pady=10,padx=10)
        self.make_button_number('7').grid(row=1, column=6, stick="wens",pady=10,padx=10)
        self.make_button_number('8').grid(row=2, column=0, stick="wens",pady=10,padx=10)
        self.make_button_number('9').grid(row=2, column=1, stick="wens",pady=10,padx=10)
        self.make_button_number('0').grid(row=2, column=2, stick="wens",pady=10,padx=10)
        self.make_button_number('(').grid(row=2, column=3, stick="wens", pady=10, padx=10)
        self.make_button_number(')').grid(row=2, column=4, stick="wens", pady=10, padx=10)
        self.make_button_operation('+').grid(row=2, column=5, stick="wens",padx=10,pady=10)
        self.make_button_operation('-').grid(row=2, column=6, stick="wens",padx=10,pady=10)
        self.make_button_operation('/').grid(row=3, column=0, stick="wens",padx=10,pady=10)
        self.make_button_operation('*').grid(row=3, column=1, stick="wens",padx=10,pady=10)
        self.make_button_clear('C').grid(row=3, column=2, stick="wens", padx=10, pady=10)
        self.trigonometry_func_calc_sin('sin').grid(row=3, column=3, stick="wens", padx=10, pady=10)
        self.trigonometry_func_calc_cos('cos').grid(row=3, column=4, stick="wens", padx=10, pady=10)
        self.trigonometry_func_calc_tang('tang').grid(row=3, column=5, stick="wens", padx=10, pady=10)
        self.trigonometry_func_calc_cotang('cotang').grid(row=3, column=6, stick="wens", padx=10, pady=10)
        self.make_button_calc('=').grid(row=4, column=0, stick="wens", padx=10, pady=10,columnspan=7)
        self.make_button_close('Click and Quit for save history').grid(row=6, column=0, stick="wens", padx=10, pady=10, columnspan=7)
        self.root.grid_columnconfigure(1, minsize=60)
        self.root.grid_columnconfigure(2, minsize=60)
        self.root.grid_rowconfigure(1, minsize=60)
        self.root.grid_rowconfigure(2, minsize=60)
        self.root.grid_rowconfigure(3, minsize=60)
        self.root.grid_rowconfigure(4, minsize=60)

    """Expression Calculation Functions"""
    def check_key(self,event):
        print(repr(event.char))
        if event.char.isdigit():
            self.add_number(event.char)
        elif event.char in '+-/*':
            self.add_operfornumber(event.char)
        elif event.char == '\r':
            self.Equals_equation()

    def add_number(self,digit):
        number_side=self.inputVarName3.get()
        if number_side[0]=='0' and len(number_side) == 1:
            number_side=number_side[1:]
        self.inputVarName3.delete(0,END)
        self.inputVarName3.insert(0,number_side+digit)

    def add_operfornumber(self, operation):
        number_side = self.inputVarName3.get()
        if number_side[-1] in '+-/*':
            number_side=number_side[:-1]
        self.inputVarName3.delete(0, END)
        self.inputVarName3.insert(0, number_side+operation)

    def Equals_equation(self):
        number_side = self.inputVarName3.get()
        if number_side[-1] in '+/-*':
            number_side=number_side+number_side[:-1]
        self.inputVarName3.delete(0, END)
        try:
           self.inputVarName3.insert(0, eval(number_side))
        except (NameError, SyntaxError):
            messagebox.showinfo('Errow','Only numbers can be entered')
            self.inputVarName3.insert(0, 0)
        except ZeroDivisionError:
            messagebox.showinfo('Errow', 'Division by 0 is not allowed')
            self.inputVarName3.insert(0, 0)

    def Equals_clearing(self):
        self.inputVarName3.delete(0, END)
        self.inputVarName3.insert(0, 0)

    def trigonometry_func_sin(self):
        number_side = self.inputVarName3.get()
        self.inputVarName3.delete(0, END)
        self.inputVarName3.insert(END, f'{number_side}sin={str(math.sin(int(number_side)))}')
    def trigonometry_func_cos(self):
        number_side = self.inputVarName3.get()
        self.inputVarName3.delete(0, END)
        self.inputVarName3.insert(END, f'{number_side}cos={str(math.cos(int(number_side)))}')
    def trigonometry_func_tang(self):
        number_side = self.inputVarName3.get()
        self.inputVarName3.delete(0, END)
        self.inputVarName3.insert(END, f'{number_side}tang={str(math.tan(int(number_side)))}')
    def trigonometry_func_cotang(self):
        number_side = self.inputVarName3.get()
        self.inputVarName3.delete(0, END)
        self.inputVarName3.insert(END, f'{number_side}cotang={str(math.cos(int(number_side))/math.sin(int(number_side)))}')

    def ranning(self):
            self.drow_widjet()

    def close_window(self):
        self.writetofileend()
        return  self.root.destroy




