# Test project of GUI python library Tkinter
from tkinter import *

# ------------ WINDOW ------------------------------------

root = Tk()
frame_calc = Frame(root)
frame_calc.pack()

# ------------ GLOBAL ------------------------------------

chain = [0,0,0,0,True]
reset_screen = False

# ------------ SCREEN ------------------------------------

screenNumber = StringVar()
screenNumber.set("0")
screen = Entry(frame_calc, font=('Verdana',30),textvariable = screenNumber)
screen.grid(row=0,column=0, ipady =30,padx=10, pady=10, columnspan = 4)
screen.config(bg = "black", width=20, fg = "green", justify = "right")

# ------------ Functionalities ------------------------------------
# ------------ Mouse Operated ------------------------------------

# def save(opt):
#     return(num_1)       # Catch return in case key ANS

def key_pressed(num):
    global reset_screen
    global chain
    scr = screenNumber.get()
    if reset_screen == True:
        screenNumber.set(num)
        reset_screen = False
    else:
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
    print(screenNumber.get())

def clear():                                # Clears screen to 0 and saved values to 0
    global chain
    chain[:] = [0,0,0,0,True]
    screenNumber.set("0")

def operation(ope):
    global reset_screen
    reset_screen = True
    global chain
    try:                                 # For the case there's only a dot in screen
        scr = float(screenNumber.get())
    except ValueError:
        scr = 0
    if chain[-1] == True:
        chain[-5] = scr
        chain[-4] = ope
    else:
        chain[-3] = scr
        chain[-2] = ope
    last_operation = chain[-4]
    result(last_operation)

def result(op):
    global chain
    if op == "+":
        res = chain[-5] + chain[-3]
    if op == "-":
        res = chain[-5] - chain[-3]
    if op == "x":
        if chain[-1] == False:
            res = chain[-5] * chain[-3]
        else:
            res = float(screenNumber.get())
    if op == "/":
        res = chain[-5] / chain[-3]
    if op == "=":
        res = chain[-5]

    screenNumber.set(res)
    chain[-5] = res
    if chain[-1] == False:
        chain[-4] = chain[-2]
    chain[-1] = False

# ------------ Functionalities ------------------------------------
# ------------ Keyboard Operated ------------------------------------
var = input("algo")


# ------------ KEYPAD ------------------------------------
# ------------ row 1 ------------------------------------

button_7 = Button(frame_calc, text = "7", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("7"))
button_7.grid(row=1, column=0)
button_8 = Button(frame_calc, text = "8", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("8"))
button_8.grid(row=1, column=1)
button_9 = Button(frame_calc, text = "9", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("9"))
button_9.grid(row=1, column=2)
button_div  = Button(frame_calc, text = "/", width = 9, height = 6, font=(None,15), command=lambda:operation("/"))
button_div.grid(row=1, column=3)
button_clc  = Button(frame_calc, text = "Clear", width = 9, height = 6, font=(None,15), command=lambda:clear())
button_clc.grid(row=1, column=4)

# ------------ row 2 ------------------------------------

button_4 = Button(frame_calc, text = "4", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("4"))
button_4.grid(row=2, column=0)
button_5 = Button(frame_calc, text = "5", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("5"))
button_5.grid(row=2, column=1)
button_6  = Button(frame_calc, text = "6", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("6"))
button_6.grid(row=2, column=2)
button_mult = Button(frame_calc, text = "x", width = 9, height = 6, font=(None,15), command=lambda:operation("x"))
button_mult.grid(row=2, column=3)

# ------------ row 3 ------------------------------------

button_1  = Button(frame_calc, text = "1", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("1"))
button_1.grid(row=3, column=0)
button_2  = Button(frame_calc, text = "2", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("2"))
button_2.grid(row=3, column=1)
button_3  = Button(frame_calc, text = "3", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("3"))
button_3.grid(row=3, column=2)
button_sum  = Button(frame_calc, text = "+", width = 9, height = 6, font=(None,15), command=lambda:operation("+"))
button_sum.grid(row=3, column=3)

# ------------ row 4 ------------------------------------

button_dot  = Button(frame_calc, text = ".", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("."))
button_dot.grid(row=4, column=0)
button_0  = Button(frame_calc, text = "0", width = 9, height = 6, font=(None,15), command=lambda:key_pressed("0"))
button_0.grid(row=4, column=1)
button_eq  = Button(frame_calc, text = "=", width = 9, height = 6, font=(None,15), command=lambda:operation("="))
button_eq.grid(row=4, column=2)
button_minu  = Button(frame_calc, text = "-", width = 9, height = 6, font=(None,15), command=lambda:operation("-"))
button_minu.grid(row=4, column=3)


root.mainloop()
