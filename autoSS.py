from dotenv import load_dotenv
from frame_op import *
from win32lib import *
import win32gui
import win32con
import time

load_dotenv()
CB_COUNT = 0
MM_COUNT = 0

def buy(hwnd, frame, pos: tuple):
    print('Buying...')
    img = frame[pos[1]:pos[1]+72, pos[0]:, :]
    res_x, res_y, val = find_template(img, 'buy', center=True)
    # print(res_x, res_y, val)
    
    click_pos(hwnd, (pos[0] + res_x, pos[1] + res_y))
    time.sleep(0.4)
    click_key(hwnd, 'y')
    time.sleep(0.5)

def find_store(hwnd):
    global CB_COUNT
    global MM_COUNT
    res = []
    frame = grabScreen_backend(hwnd)
    pos_x, pos_y, val = find_template(frame, 'cb')
    res.append(val)
    if val > int(os.getenv('THRESHOLD')):
        print('Found CB at pos({}, {}). Match rate: {}'.format(pos_x, pos_y, val))
        buy(hwnd, frame, (pos_x, pos_y))
        CB_COUNT += 1
        # return False
    pos_x, pos_y, val = find_template(frame, 'mm')
    res.append(val)
    if val > int(os.getenv('THRESHOLD')):
        print('Found MM at pos({}, {}). Match rate: {}'.format(pos_x, pos_y, val))
        buy(hwnd, frame, (pos_x, pos_y))
        MM_COUNT += 1
        # return False
    return res

def refresh(hwnd):
    # Update
    print('Refreshing...')
    click_key(hwnd, os.getenv('UPDATE_KEY'))
    time.sleep(0.4)
    click_key(hwnd, os.getenv('CONFIRM_KEY'))
    time.sleep(1.5)

    # Find top
    res = find_store(hwnd)
    # print(res)

    # Scroll
    time.sleep(0.5)
    print('Scrolling...')
    click_key(hwnd, os.getenv('SCROLLING_KEY'))
    time.sleep(1.5)

    # Find bottom
    res = find_store(hwnd)
    # print(res)

    return True

if __name__ == '__main__':

    title = 'Epic 7'

    out_hwnd = win32gui.FindWindow(None, title)

    if out_hwnd == 0:
        print('Cannot found the window: \'{}\'.'.format(title))
    else:
        try:
            hwndChilddict = dict()
            win32gui.EnumChildWindows(out_hwnd, lambda hwnd, param: param.update({win32gui.GetWindowText(hwnd): hwnd}), hwndChilddict)
            # print(hwndChilddict)
            
            in_hwnd = hwndChilddict['HD-Player']
            # print(out_hwnd, in_hwnd)
        except:
            pass

        if get_app_name(in_hwnd) != 'HD-Player.exe':
            print('Please make sure the program is running on BlueStack.')
        else:
            # win32gui.SetForegroundWindow(out_hwnd)
            # left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            # print(left, top, right, bottom)
            width, height = getScreenSize(out_hwnd)
            print('The window \'Epic 7\' origin size: ({}, {})'.format(width, height))
            # height = int(1000 * (height / width))
            height = 577
            width = 1000

            # Move window
            dim_x, dim_y = get_screen_resolution()
            print('The screen resolution is ({}, {})'.format(dim_x, dim_y))
            print('='*50)
            print('Trying to move the window to ({}, {}) and rescale to ({}, {})...'.format(dim_x-width, 0, width, height), end='')
            try:
                # win32gui.ShowWindow(out_hwnd, win32con.SW_MAXIMIZE)
                # time.sleep(1)
                win32gui.ShowWindow(out_hwnd, win32con.SW_RESTORE)
                win32gui.MoveWindow(out_hwnd, dim_x-width, 0, width, height, True)
                print('\rTrying to move the window to ({}, {}) and rescale to ({}, {})...Done'.format(dim_x-width, 0, width, height))
            except:
                pass
            left, top, right, bottom = win32gui.GetWindowRect(out_hwnd)
            print('The new window position: LT({}, {}), RB({}, {})'.format(left, top, right, bottom))
            print('The new window size: {}'.format(getScreenSize(out_hwnd)))
            print('='*50)
            count = 0
            while True:
                target = input("Refresh times: ")
                try:
                    target = int(target)
                    break
                except:
                    print('Please input valid number.')
                    continue
            while count < target:
                count += 1
                print('='*50 + '\nCounts: {}'.format(count))
                if not refresh(in_hwnd):
                    break
                print('Total: 聖約書籤 = {}, 神秘獎牌 = {}'.format(CB_COUNT, MM_COUNT))
    input('Enter any key to close...')