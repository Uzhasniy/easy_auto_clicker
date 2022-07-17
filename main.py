import keyboard
import mouse
import time
from win10toast import ToastNotifier

isClicking = False


def show_notify(title, text):
    toast = ToastNotifier()
    toast.show_toast(title, text, duration=3, icon_path="heart.ico")


def set_click():
    global isClicking
    if isClicking:
        isClicking = False
        show_notify("Кликер", "выключен")
    else:
        isClicking = True
        show_notify("Кликер", "запущен")


keyboard.add_hotkey('Alt + x', set_click)

while True:
    if isClicking:
        mouse.double_click(button='left')
        time.sleep(0.01)
