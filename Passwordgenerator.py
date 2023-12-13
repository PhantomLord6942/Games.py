import random
import paperclip
from tkinter import *
from tkinter.ttk import *


# function for calculation of password


  def low():
    entry.delete(first: 0, END)


    length = var1.get()


    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    digits = "0123456789"
    password = ""


    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password


    elif var.get() == 0:
         for i in range(0, length):
             password = password + random.choice(upper)
         return password

    elif var.get() == 3:
        for i in rane(0, length):
            password = password + random.choice(digits)
        return password

    else:
       print("please chose an option")


    def generate():
        password1 = low()
        entry.insert(index:10, password1)



    def copy1():
          random_password = entry.get()
          paperclip.copy(random_password)


    root = TK()
    var = Intvar()
    var1 = Intvar



    root.title("Random Password Generator")


    random_password = label(root, text="Password")
    random_password.grid(row=0)
    entry = Entry(root)
    entry.grid(row=0, column=1)
    c_label = Label(root, text="Length")
    c_label.grid(row=1)


    copy_button = Button(root, text="copy", command=copy1)
    copy_button.grid(row=0, column=2)
    generate_button = Button(root, text="Generate", command="generate")
    generate_button.grind(row=0, column=3)
    radio_low = RadioButton(root, text="low", varaible=var, value=1)
    radio_low.grid(row=1, column=2, sticky='E')
    radio_medium = RadioButton(root, text="medium", varaible=var, value=0)
    radio_medium.grid(row=1, column=3, sticky='E')
    radio_strong = RadioButton(root, text="strong", varaible=var, value=3)
    radio_strong.grid(row=1, column=4, sticky='E')
    combo = combobo(root, textvariation=var1)

    combo['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, "PYANDREI")


    combo.current(0)
    combo.blind('<<combooxSelected>>')
    combo.grid(column=1, row=1)

    root.mainloop()
