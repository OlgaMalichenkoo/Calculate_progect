from tkinter import *
from tkinter import messagebox
class WindowChild2:
    def __init__(self,parent1):
        self.root =Toplevel(parent1)
        self.root.title("Online calculator")
        self.root.geometry("670x700+20+20")
        self.root.iconbitmap("calculator.ico")
        self.root.resizable(True,False)
        self.root.configure(background ="#E0FFFF")
        self.ranning()


    """Creating and working buttons"""
    def make_button_number(self,digit):
        return Button(self.root, text=digit, bd='5',font=('Arial',15),command=lambda : self.add_number(digit))

    def make_button_operation(self,action):
        return Button(self.root, text=action, bd='5',font=('Arial',15),fg='blue',command=lambda : self.add_operfornumber(action))

    def make_button_clear(self, action):
        return Button(self.root, text=action, bd='5', font=('Arial', 15), fg='blue'
                      , command=self.Equals_clearing)
    def make_button_calc(self, action):
        return Button(self.root, text=action, bd='5', font=('Arial', 15), fg='blue'
                      , command=self.Equals_equation)

    """Creating interface tools"""
    def drow_widjet(self):
        self.inputVarName3 = Entry(self.root,justify=RIGHT,font=('Arial',20),width=40)
        self.inputVarName3.insert(0,'0')
        self.inputVarName3.grid(row=0,column=0,columnspan=6,stick='wens',padx=20)
        self.make_button_number('1').grid(row=1,column=0, stick="wens", pady=10,padx=10)
        self.make_button_number('2').grid(row=1, column=1, stick="wens",pady=10,padx=10)
        self.make_button_number('3').grid(row=1, column=2, stick="wens",pady=10,padx=10)
        self.make_button_number('4').grid(row=1, column=3, stick="wens",pady=10,padx=10)
        self.make_button_number('5').grid(row=1, column=4, stick="wens",pady=10,padx=10)
        self.make_button_number('6').grid(row=1, column=5, stick="wens",pady=10,padx=10)
        self.make_button_number('7').grid(row=2, column=0, stick="wens",pady=10,padx=10)
        self.make_button_number('8').grid(row=2, column=1, stick="wens",pady=10,padx=10)
        self.make_button_number('9').grid(row=2, column=2, stick="wens",pady=10,padx=10)
        self.make_button_number('0').grid(row=2, column=3, stick="wens",pady=10,padx=10)
        self.make_button_number('(').grid(row=2, column=4, stick="wens", pady=10, padx=10)
        self.make_button_number(')').grid(row=2, column=5, stick="wens", pady=10, padx=10)
        self.make_button_operation('+').grid(row=3, column=0, stick="wens",padx=10,pady=10)
        self.make_button_operation('-').grid(row=3, column=1, stick="wens",padx=10,pady=10)
        self.make_button_operation('/').grid(row=3, column=2, stick="wens",padx=10,pady=10)
        self.make_button_operation('*').grid(row=3, column=3, stick="wens",padx=10,pady=10)
        self.make_button_clear('C').grid(row=3, column=4, stick="wens", padx=10, pady=10)
        self.make_button_calc('=').grid(row=3, column=5, stick="wens", padx=10, pady=10)
        self.root.grid_columnconfigure(1, minsize=60)
        self.root.grid_columnconfigure(2, minsize=60)
        self.root.grid_rowconfigure(1, minsize=60)
        self.root.grid_rowconfigure(2, minsize=60)
        self.root.grid_rowconfigure(3, minsize=60)
        self.root.grid_rowconfigure(4, minsize=60)

    """Expression Calculation Functions"""
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

    def check_key(self, event):
        print(repr(event.char))
        if event.char.isdigit():
            self.add_number(event.char)
        elif event.char in '+-/*':
            self.add_operfornumber(event.char)
        elif event.char == '\r':
            self.Equals_equation()

    def Equals_clearing(self):
        self.inputVarName3.delete(0, END)
        self.inputVarName3.insert(0, 0)

        """Begin window launch"""
    def ranning(self):
            self.drow_widjet()

