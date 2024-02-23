import mouse
import time
import keyboard
time.sleep(3)

while keyboard.is_pressed('esc') == False:
    mouse.click('left')
    time.sleep(0.1)