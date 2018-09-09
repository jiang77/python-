import win32con
import win32gui
import time

# 找出窗体的编号(QQWin就是窗体)
QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")  # TXGuiFoundation是窗体的类，QQ是窗体的标题

# 隐藏窗体
win32gui.ShowWindow(QQWin, win32con.SW_HIDE)

time.sleep(2)

# 显示窗体
win32gui.ShowWindow(QQWin, win32con.SW_SHOW)


while Ture:
    QQWin = win32gui.FindWindow("TXGuiFoundation", "QQ")
    win32gui.ShowWindow(QQWin, win32con.SW_HIDE)
    time.sleep(3)
    win32gui.ShowWindow(QQWin, win32con.SW_SHOW)
    time.sleep(3)