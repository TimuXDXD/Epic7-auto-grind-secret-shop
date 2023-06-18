import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import win32gui
from grabScreen import getScreenSize

def calCursorPos(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    width, height = getScreenSize(hwnd)
    return (left + int(width/2), top + int(height/2)), (left + int(width/2), top + int(height*0.1))
# src, dst = calCursorPos(hwnd)
# pyautogui.moveTo(src[0], src[1])
# pyautogui.dragTo(dst[0], dst[1], 0.5, button='left')