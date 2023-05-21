# 3 mins
# 5 mins
# pyautogui
import pyautogui as gui
while True:
    Width, Height = gui.size()
    gui.moveTo(Width/2, Height/2)
    gui.sleep(60)