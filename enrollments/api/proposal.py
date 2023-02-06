import time

import pyautogui

time.sleep(4)
count = 0
while count < 10:
    pyautogui.typewrite(f"ok on it!!!!{count}")
    pyautogui.press("enter")
    count += 1
