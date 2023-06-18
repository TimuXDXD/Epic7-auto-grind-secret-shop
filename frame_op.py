import win32gui
import win32ui
import win32api
import win32con
from win32lib import *
import numpy as np
import cv2
from PIL import Image
from pathlib import Path
import os
import time

TEMPLATE_MAP = {
        'cb': 'template/CB_template.bmp',
        'mm': 'template/MM_template.bmp',
        'buy': 'template/BUY_template.bmp'
        }

def get_screen_resolution():
    screen_width = win32api.GetSystemMetrics(0)
    screen_height = win32api.GetSystemMetrics(1)
    return screen_width, screen_height

def getScreenSize(hwnd):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # print(left, top, right, bottom)
    width = right - left
    height = bottom - top
    return width, height

def find_template(frame, spec, center=False):
    # return template's (x, y, match rate)
    
    template_file = TEMPLATE_MAP[spec]
    template = cv2.imread(template_file)
    # print(frame.shape, template.shape)
    result = cv2.matchTemplate(frame, template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_ind, max_ind = cv2.minMaxLoc(result)
    if center:
        return min_ind[0]+template.shape[1]//2, min_ind[1]+template.shape[0]//2, 100-min_val*100
    return min_ind[0], min_ind[1], 100-min_val*100

def grabScreen_backend(hwnd, filename='screenshot.bmp', savefile=False):
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    # print(left, top, right, bottom)
    width = right - left
    height = bottom - top
    hdc = win32gui.GetWindowDC(hwnd)
    img_dc = win32ui.CreateDCFromHandle(hdc)
    mem_dc = img_dc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(bmp)
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (0, 0), win32con.SRCCOPY)

    # Save temp bmp file for screenshot
    if savefile:
        folder = 'temp'
        Path(folder).mkdir(parents=True, exist_ok=True)
        file = os.path.join(folder, filename)
        bmp.SaveBitmapFile(mem_dc, file)

    # Direct return np arrary
    signedIntsArray = bmp.GetBitmapBits(True)
    img = Image.frombuffer(
        'RGB',
        (width, height),
        signedIntsArray, 'raw', 'BGRX', 0, 1
    )
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    # Cleaning up the objects
    img_dc.DeleteDC()
    mem_dc.DeleteDC()
    win32gui.ReleaseDC(hwnd, hdc)
    win32gui.DeleteObject(bmp.GetHandle())

    return img

def buy(hwnd, frame, pos: tuple):
    img = frame[pos[1]:pos[1]+72, pos[0]:, :]
    res_x, res_y, val = find_template(img, 'buy', center=True)
    # print(res_x, res_y, val)
    
    click_pos(hwnd, (pos[0] + res_x, pos[1] + res_y))
    time.sleep(0.4)
    click_key(hwnd, 'y')
    time.sleep(0.5)

if __name__ == '__main__':

    out_hwnd = win32gui.FindWindow(None, 'Epic 7')
    # print(hwnd)

    # win32gui.SetForegroundWindow(out_hwnd)

    hwndChilddict = dict()
    win32gui.EnumChildWindows(out_hwnd, lambda hwnd, param: param.update({win32gui.GetWindowText(hwnd): hwnd}), hwndChilddict)
    # print(hwndChilddict)
    
    in_hwnd = hwndChilddict['HD-Player']

    img = grabScreen_backend(in_hwnd, filename='exception.bmp', savefile=True)