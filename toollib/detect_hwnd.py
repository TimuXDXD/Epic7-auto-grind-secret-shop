import win32gui
import win32ui
import win32api
import win32con
def getwithclick(type = 0):
    if type == 0:
        print("定位模擬器畫面，請用滑鼠左鍵點擊模擬器畫面")
    else:
        print("定位模擬器畫面，請用滑鼠右鍵點擊模擬器畫面")
    while 1:
        if type == 0:
            button = 0x01
        else:
            button = 0x02
        left = win32api.GetKeyState(button)
        while 1:
            a = win32api.GetKeyState(button)
            if a!= left:
                if a>=0:
                    curX, curY = win32gui.GetCursorPos()
                    hwnd = win32gui.WindowFromPoint((curX, curY))
                    print(win32gui.GetWindowText(hwnd))
                    # info = showhwndinformation(hwnd)
                    # print(info)
                    return hwnd
                
print(getwithclick())