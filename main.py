from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"


data = pd.read_csv("./data/french_words.csv")
df = data.to_dict("records")
rand_word = {}

def next_card():
    global rand_word, flip_timer
    window.after_cancel(flip_timer)
    rand_word = random.choice(df)
    canvas.itemconfig(card, image=front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=rand_word["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card, image=back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=rand_word["English"], fill="white")


window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Cards")

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(window, width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card = canvas.create_image(400,263, image=front_img)
card_title = canvas.create_text(400, 150, text="Title",font=("Arial",30,"italic"))
card_word = canvas.create_text(400, 260, text="Word",font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# X BUTTON
x_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=x_img)
wrong_btn.config(bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0, )

# CHECK BUTTON
c_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=c_img, bg=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_btn.config()
right_btn.grid(row=1, column=1, )

next_card()


window.mainloop()