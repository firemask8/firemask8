import win32api, win32con
import time
import keyboard

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    
keyboard.wait("c")
time.sleep(2)
while True:
    click()
    if keyboard.is_pressed("c"):
        break
