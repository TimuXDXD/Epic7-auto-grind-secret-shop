## Epic 7 Secret Shop Automatic Grinding Tool - 第七史詩自動刷神秘商店小工具

### Intro - 簡介
This tool uses the win32 library to replace the slower adb library, and can also be executed in the background. - 本工具使用win32庫替代較慢的adb庫，並同樣可以後台執行

### Notice - 須知
1. The tool works on bluestack 5, but should theoretically also work on bluestack 4. - 本工具適用於 bluestack 5，但理論上也適用於 bluestack 4
2. All languages supported. - 支援所有語言
3. When the missons from the high command is completed, the current version of the tool will be interrupted by the pop-up window and no longer work properly. The solution of this problem is expected to be updated later. - 當指揮總部的派遣任務完成時，目前的工具版本將會被跳出來的視窗干擾並不再正常工作，預計在之後的版本解決此問題
4. **There is no guarantee that the account will not be banned by the official, and I do not assume any responsibility. - 不保證不會被官方鎖帳號，本人不承擔任何責任**

### How to use - 如何使用
1. Download `autoSSv1.0.zip` from [releases](https://github.com/TimuXDXD/Epic7-auto-grind-secret-shop/releases/tag/v1.0) and unzip it.- 下載 `autoSSv1.0.zip` 檔並解壓縮
2. The window name of bluestack needs to be set to "Epic 7". - Bluestack 的視窗名稱需要設置為「Epic 7」
3. When using tools, the starting screen must be in the secret shop. - 使用工具時起始畫面須在神秘商店
4. You will need to add bluestack built-in game control buttons, and modify the settings in the ".env" file according to the set values. - 你會需要新增bluestack內建的遊戲控制按鈕，並根據設定的值修改「.env」檔案中的設定值
* For example the following - 例如以下
    * 'z' as refresh key - 'z'為刷新鍵
    ![](https://hackmd.io/_uploads/HJZ4CJAP2.png)
    * 'x' as confirm key - 'x'為確認鍵
    ![](https://hackmd.io/_uploads/HkwaJgRPn.png)
    * 'F2' as the key to drag up - 'F2'為向上拖曳鍵
    ![](https://hackmd.io/_uploads/r1UmZgADn.png)
    * 'y' as buy key - 'y'為購買鍵
    ![](https://hackmd.io/_uploads/rkPkMl0Dh.png)
    * Done - 完成
    
| Button | Key | var of ".env" |
| -------- | -------- | -------- |
| refresh - 刷新 | z | UPDATE_KEY |
| Confirm - 確認 | x | CONFIRM_KEY |
| Drag up - 向上滑動 | F2 | SCROLLING_KEY |
| Buy - 購買 | y | BUY_KEY |

* Setting in ".env" file: - 在".env"檔案裡的設定
```
UPDATE_KEY = 'z'
CONFIRM_KEY = 'x'
SCROLLING_KEY = 'F2'
BUY_KEY = 'y'
```
5. That's it. Open the `autoSS.exe` and enter the number of times you want to refresh. - 這樣就完成了，打開exe，並輸入刷新次數。
![](https://hackmd.io/_uploads/rkqnmxAPn.png)
    * Make sure you have enough gold and skystone. - 確保你的金幣與天空時數量足夠
    * You can stop the program at any time by typing `ctrl+c`. - 你可以在任何時候輸入`ctrl+c`停止程式

### Debug Requires - 調試需求
> If you are only using exe files then you can ignore debug requirements. - 如果你只使用exe檔案，那麼可以忽略調試需求

* Python >= 3.9
* Install packages with pip
`pip install -r requirements.txt`