from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        label_timer.config(text="Work time", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    elif reps % 2 == 0 and reps != 8:
        count_down(short_break_sec)
        label_timer.config(text="5 minutes break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
    else:
        count_down(long_break_sec)
        label_timer.config(text="25 minutes break", fg=RED, bg=YELLOW, font=(FONT_NAME, 45, "bold"))

    # if reps % 8 == 0:
    #     count_down(long_break_sec)
    #     label_timer.config(text="25 minutes break", fg=RED, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
    # elif reps % 2 == 0:
    #     count_down(short_break_sec)
    #     label_timer.config(text="5 minutes break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
    # else:
    #     count_down(work_sec)
    #     label_timer.config(text="Work time", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = "0"+str(count_sec)
    canvas.itemconfig(timer_display, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_mark = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            check_mark += "✔"
        label_tick.config(text=check_mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=280, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(144, 112, image=tomato_image)
timer_display = canvas.create_text(144, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

label_timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
label_timer.grid(column=1, row=0)

label_tick = Label(fg=GREEN, bg=YELLOW)
label_tick.grid(column=1, row=3)

button_start = Button(text="Start", font=(FONT_NAME, 20, "bold"), highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", font=(FONT_NAME, 20, "bold"), highlightthickness=0)
button_reset.grid(column=2, row=2)





window.mainloop()

