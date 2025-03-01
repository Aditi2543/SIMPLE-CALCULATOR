from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Calculator")
root.configure(bg="lightgray") 


text_box = Entry(root, width=35, borderwidth=5)
text_box.grid(row=0, column=0, columnspan=4)


def button_click(number):
    current = text_box.get()
    text_box.delete(0, END)
    text_box.insert(0, str(current) + str(number))

def button_clear():
    text_box.delete(0, END)

def button_add():
    first_number = float(text_box.get())
    global f_num
    global math
    math = "addition"
    f_num = first_number
    text_box.delete(0, END)

def button_equal():
    second_number = float(text_box.get())
    text_box.delete(0, END)

    if math == "addition":
        text_box.insert(0, f_num + second_number)
    elif math == "subtraction":
        text_box.insert(0, f_num - second_number)
    elif math == "multiplication":
        text_box.insert(0, f_num * second_number)
    elif math == "division":
        if second_number != 0:
            text_box.insert(0, f_num / second_number)
        else:
            messagebox.showerror("Error", "Cannot divide by zero")

def button_subtract():
    first_number = float(text_box.get())
    global f_num
    global math
    math = "subtraction"
    f_num = first_number
    text_box.delete(0, END)

def button_multiply():
    first_number = float(text_box.get())
    global f_num
    global math
    math = "multiplication"
    f_num = first_number
    text_box.delete(0, END)

def button_divide():
    first_number = float(text_box.get())
    global f_num
    global math
    math = "division"
    f_num = first_number
    text_box.delete(0, END)


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), bg="white", fg="black")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), bg="white", fg="black")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), bg="white", fg="black")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), bg="white", fg="black")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), bg="white", fg="black")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), bg="white", fg="black")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), bg="white", fg="black")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), bg="white", fg="black")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), bg="white", fg="black")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), bg="white", fg="black")

button_add = Button(root, text="+", padx=39, pady=20, command=button_add, bg="pink", fg="black")
button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract, bg="pink", fg="black")
button_multiply = Button(root, text="*", padx=41, pady=20, command=button_multiply, bg="pink", fg="black")
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide, bg="pink", fg="black")
button_equal = Button(root, text="=", padx=87, pady=20, command=button_equal, bg="purple", fg="black")
button_clear = Button(root, text="Clear", padx=77, pady=20, command=button_clear, bg="purple", fg="black")


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)


root.mainloop()