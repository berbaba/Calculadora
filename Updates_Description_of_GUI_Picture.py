# Taking Screenshot Using An Tkinter application

import pyautogui            # import PyAutoGUI library: Required installation pip install pyautogui
import tkinter as tk        # and  sudo apt-get install scrot

path_toFile = '/home/bernat/Documents/Estudiant/Python/environments/pildoras/Gràfics/Calculadora/'
fileName = 'calc_Clear_button_locate.png'
button_location = pyautogui.locateOnScreen(path_toFile+fileName) # Locates the image from File in the current screen
left = button_location.left - 390           # Once the target is located, the shape coordinates are corrected
right = button_location.width + 420         # manually
top = button_location.top - 140
bottom = button_location.height + 580
# define a method that will call whenever to take the screenshot
def take():
    image = pyautogui.screenshot(path_toFile+"Calc_Screenshot_update.png", region = (left,top,right,bottom))
take()
