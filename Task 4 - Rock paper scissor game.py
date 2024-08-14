#TASK 4 - Rock-Paper-Scissors Game

# User Input: Prompt the user to choose rock, paper, or scissors.
# Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer.
# Game Logic: Determine the winner based on the user's choice and the computer's choice.
# Rock beats scissors, scissors beat paper, and paper beats rock.
# Display Result: Show the user's choice and the computer's choice. Display the result, whether the user wins, loses, or it's a tie.
# Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds.
# Play Again: Ask the user if they want to play another round.
# User Interface: Design a user-friendly interface with clear instructions and feedback

import random 
from tkinter import * 
import tkinter as tk

root = Tk()
root.geometry("300x300")
root.title("Rock Paper Scissor Game")

# Computer Value
computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

# Reset The Game
def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text="Player")
    l3.config(text="Computer")
    l4.config(text="")

# Disable the Button 
def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"

#if player selected rock
def isrock():
    c_v = computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Match draw"
    elif c_v == "Scissor":
        match_result = "Player win"
    else:
        match_result = "Computer win"
    
    l4.config(text=match_result)
    l1.config(text= "Rock")
    l3.config(text= c_v)
    button_disable()

#if player selected paper
def ispaper():
    c_v =  computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Player win"
    elif c_v == "Paper":
        match_result = "Match draw"
    else:
        match_result = "Computer win"

    l4.config(text=match_result)
    l1.config(text= "Paper")
    l3.config(text= c_v)
    button_disable()

#if player selected scissor
def issci():
    c_v =  computer_value[str(random.randint(0,2))]
    if c_v == "Rock":
        match_result = "Computer win"
    elif c_v == "Paper":
        match_result = "Player win"
    else:
        match_result = "Match draw"

    l4.config(text=match_result)
    l1.config(text= "Scissor")
    l3.config(text= c_v)
    button_disable()



Label(root, text="Rock Paper Scissor", font="normal 20 bold", fg="purple").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame, text="Player",font=14)
l2 = Label(frame, text="vs", font=10)
l3 = Label(frame, text="Computer",font=14)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(root ,text="", width=15, bg="white", font="normal 20 bold", borderwidth=2)
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock", font=14, width=5,command=isrock)
b2 = Button(frame1, text="Paper", font=14, width=5,command=ispaper)
b3 = Button(frame1, text="Scissor", font=14, width=5,command=issci)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack()

Button(root, text="Reset the game", font=14, fg="red", command=reset_game).pack(pady=20)

root.mainloop()

