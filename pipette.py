from ctypes import windll, byref
import pyautogui
import keyboard
import pyperclip


## Transforme une couleur donné par la fonction GetPixel() en hexadécimal
def WinColorToHex(color) :
    color = hex(color)[2:8].zfill(6)
    return color[4:6] + color[2:4] + color[0:2]

## Écouteur d'événement pour la touche shift
def on_shift_press(event):
    pos = pyautogui.position()
    color = windll.gdi32.GetPixel(hdc, pos[0], pos[1])
    color = WinColorToHex(color)
    print(color)
    pyperclip.copy(color)


hdc = windll.user32.GetDC(0)
windll.user32.ScreenToClient()
keyboard.on_press_key("shift", on_shift_press)

print("Appuyez sur \"Shift\" pour copier la couleur sur la souris")
while True:
    keyboard.wait()
