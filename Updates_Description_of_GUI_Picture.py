# Taking Screenshot Using An Tkinter application

import pyautogui   # import PyAutoGUI library       # Required installation pip install pyautogui and  sudo apt-get install scrot
import tkinter as tk  # import tkinter library

path_toFile = '/home/bernat/Documents/Estudiant/Python/environments/pildoras/Gràfics/Calculadora/'
fileName = 'calc_Clear_button_locate.png'
button_location = pyautogui.locateOnScreen(path_toFile+fileName)     # Locates the image from File in the current screen
left = button_location.left
right = button_location.width
top = button_location.top
bottom = button_location.height
# define a method that will call whenever to take the screenshot
def take():
    image = pyautogui.screenshot(path_toFile+"Calc_Screenshot_update.png", region = (left-390,top-140,right+420,bottom+580))
take()
