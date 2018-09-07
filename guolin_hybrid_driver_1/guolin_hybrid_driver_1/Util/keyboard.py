# coding=utf-8
import win32api
import win32con

VK_CODE = {
    'enter': 0x0D,
    'ctrl': 0x11,
    'a': 0x41,
    'v': 0x56,
    'x': 0x58,
    'del': 0x2E
}
# 键盘键按下,keyName为按键名称，即VK_CODE字典里的key，其中0,0,0 为固定写法
def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, 0, 0)

# 键盘键抬起,keyName为按键名称，即VK_CODE里的key
def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName], 0, win32con.KEYEVENTF_KEYUP, 0)


