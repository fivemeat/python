import openpyxl
from openpyxl import Workbook, load_workbook
# 导入pyautogui库，用于控制键盘和鼠标
import pyautogui as pg
# 导入pyperclip库，用于实现复制和粘贴功能
import pyperclip as cb
# 导入time库，用于控制时间
import time
name = ''
age = ''
big = ''

zongbiao = openpyxl.load_workbook('./12.xlsx')
zb = zongbiao.active
print(zb.title)#获取表名

#zb.append(['111','222','333'])#将内容添加到现有表中
#zongbiao.save('./12.xlsx')#保存表
time.sleep(0.5)
pg.moveTo(206,344)
pg.doubleClick()
pg.hotkey('ctrl','c')
name = cb.paste()
print(name)

pg.moveTo(352,342)
time.sleep(0.3)
pg.doubleClick()
pg.hotkey('ctrl','c')
age = cb.paste()
print(age)

pg.moveTo(459,344)
time.sleep(0.3)
pg.doubleClick()
pg.hotkey('ctrl','c')
big = cb.paste()
print(big)

zb.append([age,name,big])
zongbiao.save('./12.xlsx')#保存表