# Task 1 - TO-DO LIST
#A To-Do List application is a useful project that helps users manage and organize their tasks efficiently. This project aims to create acommand-line or GUI-based application using Python, allowing users to create, update, and track their to-do lists

from tkinter import *
from tkinter import messagebox

task_list = []
count_task = 1

#function to create new task
def newTask():
    task = entry.get()
    if task != "":
        lb.insert(END, task)
        #task_list.append(task)
        entry.delete(0,'end')
    else:
        messagebox.showwarning("warning", "Please enter some task !")

#function to delete the task
def deleteTask():
    lb.delete(ANCHOR)


#create window 
root = Tk()
root.geometry('500x550+500+200')
root.title('TO DO LIST')
tdl = Label(root, text='To Do List Application', background='grey',fg='black',font=('times', 24))
tdl.pack()
root.config(bg='grey')
root.resizable(width=False, height=False)

frame=Frame(root)
frame.pack(pady=10)

lb = Listbox(frame , 
             width = 25,
             height = 10,
             font = ('Times', 18),
             bd=0,
             highlightthickness=0, 
             #highlightbackground='grey',
             #highlightcolor='grey',
             activestyle="none",
             )
lb.pack(side=LEFT, fill=BOTH)

for task in task_list:
    lb.insert(END , task)

sb = Scrollbar(frame)
sb.pack(side='right', fill =BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

entry = Entry(root, font=('times', 18))
entry.pack(pady=20)

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add task',
    font=('times', 18),
    bg='blue',
    padx=20,
    pady=10,
    command=newTask
)

addTask_btn.pack(fill=BOTH, expand=True, side='left')

delTask_btn = Button(
    button_frame,
    text='Delete task',
    font=('times', 18),
    bg='blue',
    padx=20,
    pady=10,
    command=deleteTask
)

delTask_btn.pack(fill=BOTH, expand=True, side='left')

root.mainloop()