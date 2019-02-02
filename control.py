from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse=Controller()
    mouse.position(500,200)

def controlKeyboard():
    keyboard=Controller()
    keyboard.type("I am awesome")

controlKeyboard()


#Controlling your mouse
#Listening to your mouse
#Controlling your keyboard
#Listening to your keyboard

