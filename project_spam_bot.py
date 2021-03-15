# automated message
# import relevant module

import time
import pyautogui
# let's code!
def sendMessage():
    time.sleep(6)
    text = open('msg.txt')
    for each_line in text:
        pyautogui.typewrite(each_line)



        pyautogui.press('enter')


sendMessage()

