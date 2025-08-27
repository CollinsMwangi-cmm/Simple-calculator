from tkinter import *

root = Tk()
root.title( "Simple Calculator")


f_num = None
math = None
history = []

e = Entry(root, width=60, borderwidth=10)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


#history Display
history_box = Text(root, width=40, height=8, state=DISABLED)
history_box.grid(row=6,column=0, columnspan=4, padx=10, pady=10)

def update_history(entry):
    history.append(entry)
    history_box.config(state=NORMAL)
    history_box.insert(END, entry + "\n")
    history_box.config(state=DISABLED)

def button_click(number):
    current = e.get()
    if str(number) == '.' and '.' in current:
        return
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

        


def button_add():
    f_number = e.get()
    global f_num, math
    math = "addition"
    f_num =float(f_number)
    e.delete(0, END)
    


def button_minus():
    f_number = e.get()
    global f_num, math
    math = "subtraction"
    f_num =float(f_number)
    e.delete(0, END)
    
    
def button_multiply():
    f_number = e.get()
    global f_num, math
    math = "multiplication"
    f_num =float(f_number)
    e.delete(0, END)

def button_divide():
    f_number = e.get()
    global f_num, math
    math = "division"
    f_num =float(f_number)
    e.delete(0, END)

def button_percent():
    f_number = e.get()
    global f_num, math
    f_num= float(e.get())/100
    math = "percent"
    f_num = float(f_number) / 100
    e.delete(0, END)
    e.insert(0, f_num)
    


def button_equal():
    global f_num, math
    second_number = e.get()
    try:
        s_number = float(second_number)
    except:
        s_number = 0
    e.delete(0, END)
    
    result = None
    expression =""
    
    
    if math == "addition":
        result = f_num + s_number
        expression = f"{f_num} + {s_number} = {result}"
        
    elif math == "percent":
        result = f_num
        expression = f"{s_number}%={result}"
    
    elif math == "subtraction":
        result =  f_num - s_number
        expression = f"{f_num} - {s_number} = {result}"
    
    elif math == "multiplication":
        result =  f_num * s_number
        expression= f"{f_num} * {s_number} = {result}"
    
    
    elif math == "division":
        if s_number != 0:
            result =  f_num / s_number
            expression = f"{f_num} / {s_number} = {result}"
        else:
            e.insert(0, "Error: Div by 0") 
            return
    else:
        e.insert(0, "Error: Invalid Operation")
        return
    
    if result is not None:
        if result.is_integer():
            result = int(result)
        e.insert(0, result)
        update_history(expression)
        
        
def button_delete():
    current = e.get()
    current[:-1]
    e.delete(0, END )
    e.insert(0, current[:-1])
    
    
    
    


button1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_equal = Button(root, text='=', padx=40, pady=20, command=button_equal)
button_dot = Button(root, text='.', padx=41, pady=20, command=lambda: button_click('.'))
button_add = Button(root, text="+", padx=45, pady=20, command=button_add)
button_minus =  Button(root, text="-", padx=45, pady=20, command= button_minus)
button_multiply =  Button(root, text="*", padx=45, pady=20, command= button_multiply)
button_divide =  Button(root, text="/", padx=45,pady=20, command=button_divide)
button_del =Button(root, text='⌫', padx=39, pady=20, command= button_delete)
button_clear = Button(root, text='C', padx=40, pady=20, command=button_clear)
button_percent= Button(root, text='%', padx=86, pady=20, command=button_percent)

button_del.grid(row=1, column=3)
button_clear.grid(row=1, column=2)
button_percent.grid(row=1, column=0,  columnspan=2)

button9.grid(row=2, column=2)
button8.grid(row=2, column=1)
button7.grid(row=2, column=0)

button6.grid(row=3, column=2)
button5.grid(row=3, column=1)
button4.grid(row=3, column=0)

button3.grid(row=4, column=2)
button2.grid(row=4, column=1)
button1.grid(row=4, column=0)

button0.grid(row=5, column=0)
button_dot.grid(row=5, column=1)
button_equal.grid(row=5, column=2)


button_multiply.grid(row=2, column=3)
button_minus.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_add.grid(row=5, column=3)


root.mainloop()
