# Test project of GUI python library Tkinter
from tkinter import *

root = Tk()
frame_calc = Frame(root)
frame_calc.pack()

# ------------ SCREEN ------------------------------------

screenNumber = StringVar()
screenNumber.set("0")
screen = Entry(frame_calc, textvariable = screenNumber)
screen.grid(row=0,column=0, padx=10, pady=10, columnspan = 4)
screen.config(bg = "black", fg = "green", justify = "right")

# ------------ Functionalities ------------------------------------

def key_pressed(num):
    scr = screenNumber.get()
    if num == ".":
        if "." in scr:
            return
        else:
            screenNumber.set(scr + num)
    elif num == "0":    # If screen number is just 0 do not add another 0
        if scr != "0":
            screenNumber.set(scr + num)      # Gets whatever is in screen and adds the next value
    else:
        if scr == "0":
            screenNumber.set(num)
        else:
            screenNumber.set(scr + num)

def operation(ope):
    num_1 = float(screenNumber.get())

def clear():
    screenNumber.set("0")


# ------------ KEYBOARD ------------------------------------
# ------------ row 1 ------------------------------------

button_7 = Button(frame_calc, text = "7", width = 3, command=lambda:key_pressed("7"))
button_7.grid(row=1, column=0)
button_8 = Button(frame_calc, text = "8", width = 3, command=lambda:key_pressed("8"))
button_8.grid(row=1, column=1)
button_9 = Button(frame_calc, text = "9", width = 3, command=lambda:key_pressed("9"))
button_9.grid(row=1, column=2)
button_div  = Button(frame_calc, text = "/", width = 3, command=lambda:operation("/"))
button_div.grid(row=1, column=3)
button_clc  = Button(frame_calc, text = "Clear", width = 3, command=lambda:clear())
button_clc.grid(row=1, column=4)

# ------------ row 2 ------------------------------------

button_4 = Button(frame_calc, text = "4", width = 3, command=lambda:key_pressed("4"))
button_4.grid(row=2, column=0)
button_5 = Button(frame_calc, text = "5", width = 3, command=lambda:key_pressed("5"))
button_5.grid(row=2, column=1)
button_6  = Button(frame_calc, text = "6", width = 3, command=lambda:key_pressed("6"))
button_6.grid(row=2, column=2)
button_mult = Button(frame_calc, text = "*", width = 3)
button_mult.grid(row=2, column=3)

# ------------ row 3 ------------------------------------

button_1  = Button(frame_calc, text = "1", width = 3, command=lambda:key_pressed("1"))
button_1.grid(row=3, column=0)
button_2  = Button(frame_calc, text = "2", width = 3, command=lambda:key_pressed("2"))
button_2.grid(row=3, column=1)
button_3  = Button(frame_calc, text = "3", width = 3, command=lambda:key_pressed("3"))
button_3.grid(row=3, column=2)
button_sum  = Button(frame_calc, text = "+", width = 3)
button_sum.grid(row=3, column=3)

# ------------ row 4 ------------------------------------

button_dot  = Button(frame_calc, text = ".", width = 3, command=lambda:key_pressed("."))
button_dot.grid(row=4, column=0)
button_0  = Button(frame_calc, text = "0", width = 3, command=lambda:key_pressed("0"))
button_0.grid(row=4, column=1)
button_eq  = Button(frame_calc, text = "=", width = 3)
button_eq.grid(row=4, column=2)
button_minu  = Button(frame_calc, text = "-", width = 3)
button_minu.grid(row=4, column=3)






root.mainloop()
