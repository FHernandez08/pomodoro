from difflib import restore
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

# timer label
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45), bg=YELLOW)
title_label.grid(column=1, row=0)

# start button
start_btn = Button(text="Start", highlightthickness=0)
start_btn.grid(column=0, row=2)

# Reset button
reset_btn = Button(text="Reset", highlightthickness=0)
reset_btn.grid(column=2, row=2)

# checkmark label
checkmark_label = Label(text="✓", fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

window.mainloop()