from ctypes import windll
import mouse
from tkinter import Tk

def WinColorToHex(color) :
    print("r =", hex(color)[6:8], "; g =", hex(color)[4:6], "; b =", hex(color)[2:4])

    result = hex(color)[6:8]
    if(hex(color)[4:6] == "") :
        result += "00"
    else :
        result += hex(color)[4:6]
    if(hex(color)[2:4] == "") :
        result += "00"
    else :
        result += hex(color)[2:4]
    return result

hdc = windll.user32.GetDC(0)

isPressed = mouse.is_pressed("left")
while not isPressed :
    isPressed = mouse.is_pressed("left")

color = WinColorToHex(windll.gdi32.GetPixel(hdc, mouse.get_position()[0], mouse.get_position()[1]))
print(color)
Tk().clipboard_append(color);