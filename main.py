import pyautogui
import time
text= 10
while text > 0:
    time.sleep(3)
    pyautogui.typewrite('Mahmudul Islam Siman')
    time.sleep(1)
    pyautogui.press('enter')
    text= text - 1