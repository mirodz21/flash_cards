from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Cards")

canvas = Canvas(window, width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas.create_image(400,263, image=front_img)
canvas.create_text(400, 150, text="Title",font=("Arial",30,"italic"))
canvas.create_text(400, 260, text="Word",font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)





x_img = PhotoImage(file="./images/wrong.png")
wrong_btn = Button(image=x_img)
wrong_btn.config(bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_btn.grid(row=1, column=0, )

c_img = PhotoImage(file="./images/right.png")
right_btn = Button(image=c_img, bg=BACKGROUND_COLOR, highlightthickness=0)
right_btn.config()
right_btn.grid(row=1, column=1, )




window.mainloop()