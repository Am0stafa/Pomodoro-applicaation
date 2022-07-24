from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 # 4 sets then long break
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps =0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def resetTimer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    global reps
    reps -=1

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def startTimer():
    global reps
    workSec = WORK_MIN * 60
    shortBreak = SHORT_BREAK_MIN * 60
    longBreak = LONG_BREAK_MIN * 60
    
    if reps % 2 == 0:
        title_label.config(text="Work", fg=GREEN)
        countDown(workSec)
        reps+=1
        check_marks["text"]=reps
    elif reps % 2 != 0:
        title_label.config(text="Break", fg=RED)
        if reps == 7:
            countDown(longBreak)
            reps = 0
            check_marks["text"]=reps
        else:
            countDown(shortBreak)
            reps+=1
            check_marks["text"]=reps
        
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countDown(count):
    mins = count//60
    sec = count%60
    global reps
    if sec == 0:
        sec ="00"
    elif sec < 10:
        sec = f"0{sec}"
    global reps    
    
    canvas.itemconfig(timer_text,text=f"{mins}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countDown, count - 1)
    else:
        if reps % 2 == 0: 
            canvas.itemconfig(timer_text,text=f"25:00")
        elif reps % 2 != 0:
            if reps == 7:
               canvas.itemconfig(timer_text,text=f"15:00")
            else:
                canvas.itemconfig(timer_text,text=f"05:00")
        
 
        



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check_marks = Label(text ="0",fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

start_button = Button(text="Start", highlightthickness=0, command=startTimer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=resetTimer)
reset_button.grid(column=2, row=2)


window.mainloop()