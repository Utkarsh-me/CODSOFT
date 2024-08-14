## TASK 3 - PASSWORD GENERATOR
## A password generator is a useful tool that generates strong and random passwords for users. This project aims to create a password generator application using Python, allowing users to specify the length and complexity of the password.
## User Input: Prompt the user to specify the desired length of thepassword.
## Generate Password: Use a combination of random characters to generate a password of the specified length.
## Display the Password: Print the generated password on the screen

import random 
from tkinter import * 
import tkinter as tk
import pyperclip 


def strong():
    pass_entry.delete(0,END)
    length = int(in_option.get())
    low = "abcdefghijklmnopqrstuvwxyz"
    med = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    strn = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$&^._"
    password = ""

    stregnth = var.get()

    if stregnth == "weak":
        chars = low
       

    elif stregnth == "med":
        chars = med
        

    else:
        chars = strn 
        
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate():
    password1 = strong()
    pass_entry.insert(10, password1)
 

def copy():
    random_pass = pass_entry.get()
    pyperclip.copy(random_pass)

root = Tk()
root.config(background="black")
root.title("Passwod Generator")
root.geometry('900x250+500+250')
#pgl = Label(root, text="Password generator",background="black", fg="white", font=('times', (22)))
#pgl.grid(row=0)

#space = Label(root, text="", background="black",fg="white", font=('times', (10))) 
#space.grid(row=0)
num=tk.IntVar()
in_option = StringVar()
in_option.set("Length of password")
combo = [8,12,16,20]
option =  OptionMenu(root, in_option , *combo)
option.grid(row=0, column=0)
option.place(x=10, y=0, width=200)

var = StringVar()
radio_low = Radiobutton(root, text="Low", variable=var, value="weak")
radio_low.grid(row=0, column=4, sticky='W')
radio_middle = Radiobutton(root, text="Medium", variable=var, value="med")
radio_middle.grid(row=0, column=5, sticky='W')
radio_strong = Radiobutton(root, text="Strong", variable=var, value="strong")
radio_strong.grid(row=0, column=6 , sticky='W')

info = Label(root, text="*Please select only one option for strength of password", background="black",fg="white", font=('times', (10)))
info.grid(row=0, column=6)

random_pass =Label(root, text="Password", background="black", fg="black", font=('times',(26)))
random_pass.grid(row=2, column=0)
pass_entry = Entry(root, font=(20))
pass_entry.grid(row=3, column=0)

copy_btn = Button(root, text="Copy", command=copy)
copy_btn.grid(row=3, column=5)

generate_button = Button(root, text="Generate", command=generate)
generate_button.grid(row=3, column=4)

info2 = Label(root, text="*Select 'Generate' to generate password 'Copy' to copy the generated password to the clipboard",background="black",fg="white", font=('times', (10)))
info2.grid(row=3, column=6)

root.mainloop()