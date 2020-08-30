#!/usr/bin/env python3

import _thread
import time
import pyautogui

width, height = pyautogui.size()

print(width, height)

# 移动到绝对位置
# for i in range(10):
#     pyautogui.moveTo(300, 300, duration=0.25)
#     pyautogui.moveTo(400, 300, duration=0.25)
#     pyautogui.moveTo(400, 400, duration=0.25)
#     pyautogui.moveTo(300, 400, duration=0.25)

x, y = pyautogui.position()
print(x, y)

# 实时获取当前鼠标的位置
# try:
#     while True:
#         x, y = pyautogui.position()
#         time.sleep(0.1)
#         print(x, y)
# except KeyboardInterrupt:
#     print('\nExit.')

def print_position( threadName, delay):
    try:
        while True:
            x, y = pyautogui.position()
            print(x, y)
            time.sleep(delay)
    except KeyboardInterrupt:
        print('\nExit.')

try:
    _thread.start_new_thread(print_position, ('Thread_positon', 0.5))
except:
    print("Error: unable to start thread")

# 鼠标控制
pyautogui.click(x=1766, y=636, button='left')

while True:
    pass