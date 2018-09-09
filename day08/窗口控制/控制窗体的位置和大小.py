import win32con
import win32gui
import time
import random


QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")  # TXGuiFoundation是窗体的类，QQ是窗体的标题

# 参数1：要控制的窗体
# 参数2：大致方位.HWND_TOPMOST是上方
# 参数3：位置x
# 参数4：位置y
# 参数5：长度（窗体）
# 参数6：宽度（窗体）
win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, 100, 100, 300, 300, win32con.SWP_SHOWWINDOW)

# 想要窗口满屏不确定的移动。使用循环
while True:
    x = random.randrange(900)
    y = random.randrange(600)
    win32gui.SetWindowPos(QQWin, win32con.HWND_TOPMOST, x, y, 300, 300, win32con.SWP_SHOWWINDOW)