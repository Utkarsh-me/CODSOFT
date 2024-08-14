# TASK 2 - CALCULATOR
# Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice. Perform the calculation and display the result

from tkinter import *

expression = ""

#clear command 
def clear():
    global expression 
    expression = "" 
    eq.set("") 

#when the number is pressed
def press(num):
    global expression
    expression = expression + str(num)
    eq.set(expression)

# for = 
def equals():
    try:
        global expression
        total = str(eval(expression))
        eq.set(total)
        expression = ""
    except:
        eq.set("error")
        expression = ""


root = Tk()
root.config(background="black")
root.title("Simple Calculator")

root.geometry('380x200+550+250')

frame = Frame(root, width=430, height=50, bg='black')
frame.grid()
eq = StringVar()
entry = Entry(frame, textvariable=eq, font=(20))
entry.grid(columnspan=4, ipadx=80, ipady=5)

clr = Button(frame, text='C', fg='black', command= clear, height=1, width=7)
clr.grid(row=1, column=3)

btn1 = Button(frame, text=' 1 ', fg='black', command=lambda: press(1), height=1, width=7) 
btn1.grid(row=2, column=0)

btn2 = Button(frame, text=' 2 ', fg='black', command=lambda: press(2), height=1, width=7) 
btn2.grid(row=2, column=1)

btn3 = Button(frame, text=' 3 ', fg='black', command=lambda: press(3), height=1, width=7) 
btn3.grid(row=2, column=2)

plus = Button(frame, text=' + ', fg='black', command=lambda: press('+'), height=1, width=7) 
plus.grid(row=2, column=3)

btn4 = Button(frame, text=' 4 ', fg='black', command=lambda: press(4), height=1, width=7) 
btn4.grid(row=3, column=0)

btn5 = Button(frame, text=' 5 ', fg='black', command=lambda: press(5), height=1, width=7) 
btn5.grid(row=3, column=1)

btn6 = Button(frame, text=' 6 ', fg='black', command=lambda: press(6), height=1, width=7) 
btn6.grid(row=3, column=2)

minus = Button(frame, text=' - ', fg='black', command=lambda: press('-'), height=1, width=7) 
minus.grid(row=3, column=3)

btn7 = Button(frame, text=' 7 ', fg='black', command=lambda: press(7), height=1, width=7) 
btn7.grid(row=4, column=0)

btn8 = Button(frame, text=' 8 ', fg='black', command=lambda: press(8), height=1, width=7) 
btn8.grid(row=4, column=1)

btn9 = Button(frame, text=' 9 ', fg='black', command=lambda: press(9), height=1, width=7) 
btn9.grid(row=4, column=2)

mul = Button(frame, text=' x ', fg='black', command=lambda: press('*'), height=1, width=7) 
mul.grid(row=4, column=3)

equ = Button(frame, text=' = ', fg='black', command=equals, height=1, width=7) 
equ.grid(row=5, column=0)

btn0 = Button(frame, text=' 0 ', fg='black', command=lambda: press(0), height=1, width=7) 
btn0.grid(row=5, column=1)

decimal = Button(frame, text=' . ', fg='black', command=lambda: press('.'), height=1, width=7) 
decimal.grid(row=5, column=2)

div = Button(frame, text=' / ', fg='black', command=lambda: press('/'), height=1, width=7) 
div.grid(row=5, column=3)

root.mainloop()