# Taking Screenshot Using An Tkinter application
# Now you will learn how to take screenshot from a Tkinter application.
#
# So write the following code snippets on your editor.

import pyautogui   # import PyAutoGUI library       # Required installation pip install pyautogui and  sudo apt-get install scrot
import tkinter as tk  # import tkinter library

# create main window
window = tk.Tk()

# define a method that will call whenever button will be clicked
def take():
    image = pyautogui.screenshot("tkscreen.png")

# create a button
shot_btn = tk.Button(window,text = "Take Screenshot", command= take)

# place the button on the window
shot_btn.place(x=50, y=50)
window.mainloop()
# Now run the above code. Now a GUI window will be appeared, now press the button present on this window. Your screen has been captured. Let’s see the output.
