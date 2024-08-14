#TASK 5 - Contact Book

#Contact Information: Store name, phone number, email, and address for each contact.
#Add Contact: Allow users to add new contacts with their details.
#View Contact List: Display a list of all saved contacts with names and phone numbers.
#Search Contact: Implement a search function to find contacts by name or phone number.
#Update Contact: Enable users to update contact details.
#Delete Contact: Provide an option to delete a contact.
#User Interface: Design a user-friendly interface for easy interaction.
	

from tkinter import *

root = Tk() 

root.geometry('400x500') 
root.config(bg='grey')
# Information List 
datas = [] 

# Add Information 
def add(): 
	global datas 
	datas.append([Name.get(),Number.get(),mail.get(),address.get(1.0, "end-1c")]) 
	update_book() 

# View Information 
def view(): 
	Name.set(datas[int(select.curselection()[0])][0]) 
	Number.set(datas[int(select.curselection()[0])][1]) 
	address.delete(1.0,"end") 
	address.insert(1.0, datas[int(select.curselection()[0])][2]) 
	mail.set(datas[int(select.curselection()[0])][3]) 

# Delete Information 
def delete(): 
	del datas[int(select.curselection()[0])] 
	update_book() 

#reset list
def reset(): 
	Name.set('') 
	Number.set('') 
	address.delete(1.0,"end") 
	mail.set('')

# Update Information 
def update_book(): 
	select.delete(0,END) 
	for n,p,a,e in datas: 
		select.insert(END, n) 

# Add Buttons, Label, ListBox 
Name = StringVar() 
Number = StringVar() 
mail = StringVar()

frame = Frame() 
frame.pack(pady=10) 

frame1 = Frame() 
frame1.pack() 

frame2 = Frame() 
frame2.config(bg='grey')
frame2.pack(pady=10) 

frame3 = Frame()
frame3.pack()

Label(frame, text = 'Name', font='arial 12 bold',background='grey', fg='black').pack(side=LEFT) 
Entry(frame, textvariable = Name,width=50).pack() 

Label(frame1, text = 'Phone No.', font='arial 12 bold',background='grey', fg='black').pack(side=LEFT) 
Entry(frame1, textvariable = Number,width=50).pack() 

Label(frame2, text = 'Address', font='arial 12 bold',background='grey').pack(side=LEFT) 
address = Text(frame2,width=37,height=5) 
address.pack() 

Label(frame3, text = 'Email address', font='arial 12 bold',background='grey', fg='black').pack(side=LEFT) 
Entry(frame3, textvariable = mail,width=50).pack()

Button(root,text="Add",font="arial 12 bold",command=add).place(x= 100, y=270) 
Button(root,text="View",font="arial 12 bold",command=view).place(x= 100, y=310) 
Button(root,text="Delete",font="arial 12 bold",command=delete).place(x= 100, y=350) 
Button(root,text="Reset",font="arial 12 bold",command=reset).place(x= 100, y=390) 

scroll_bar = Scrollbar(root, orient=VERTICAL) 
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12) 
scroll_bar.config (command=select.yview) 
scroll_bar.pack(side=RIGHT, fill=Y) 
select.place(x=200,y=260) 

# Execute Tkinter 
root.mainloop()