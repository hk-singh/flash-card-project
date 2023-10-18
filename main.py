import json
from tkinter import *
import random

import pandas
import pandas as pd
import time

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- PROCESSING THE DATA ------------------------------- #
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")
finally:
    df = pd.DataFrame(data, columns=["French", "English"])
    to_learn = df.to_dict(orient="records")

current_card = {}
# ---------------------------- CARD FUNCTION ------------------------------- #


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def remove_word_from_list():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=next_card)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = canvas.create_image(400, 263, image=card_front)
canvas.grid(row=0, column=0, columnspan=6)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "italic"), fill="black")

#Buttons
right_button = Button(image=right, highlightthickness=0, bg=BACKGROUND_COLOR, command=remove_word_from_list)
right_button.grid(column=4, row=1)

wrong_button = Button(image=wrong, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(column=1, row=1)


# ---------------------------- PROCESSING THE DATA ------------------------------- #



window.mainloop()