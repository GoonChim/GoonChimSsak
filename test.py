import pyautogui
import time
import cv2
import telegram
from telegram import chat
import schedule
from datetime import datetime

# print(pyautogui.position())

while True:

    t1 = datetime.now()

# // 'cvd, fire 차트'
    pyautogui.moveTo(584, 11)
    pyautogui.click(584, 11)
    pyautogui.press('f5')
    time.sleep(12.5)

    pyautogui.screenshot('1.png', region=(394, 768, 1110, 30))
    num1 = pyautogui.locateCenterOnScreen('1.png')
    pyautogui.click(num1)

    time.sleep(7)

    pyautogui.moveTo(1908, 1033)
    pyautogui.click(1908, 1033, 20, 0.05)

    time.sleep(10)
    pyautogui.screenshot('2.png', region=(484, 205, 1010, 530))

    time.sleep(1)

# /  106,11 //84, 423 //104, 393
# /  크립토 퀀트 '레버리지, 펀딩비, 미결제'
    pyautogui.moveTo(106, 11)
    pyautogui.click(106, 11)
    time.sleep(1)

    pyautogui.moveTo(84, 423)
    pyautogui.click(84, 423)
    time.sleep(3)

    pyautogui.moveTo(104, 393)
    pyautogui.click(104, 393)
    time.sleep(4)

# /  272, 278
    pyautogui.screenshot('3.png', region=(272, 278, 1650, 760))
    time.sleep(1.5)

# /  97, 294
# /  크립토 퀀트 '총거래소 고래 비율'
    pyautogui.moveTo(97, 294)
    pyautogui.click(97, 294)
    time.sleep(7)

# /  272, 278
    pyautogui.screenshot('4.png', region=(272, 278, 1650, 760))
    time.sleep(1.5)

# /  97, 356
# /  크립토 퀀트 'Stablecoins Ratio'
    pyautogui.moveTo(97, 356)
    pyautogui.click(97, 356)
    time.sleep(7)

# /  272, 278
    pyautogui.screenshot('5.png', region=(272, 278, 1650, 760))

# /  텔레그램 챗 봇
    time.sleep(1)
    bot = telegram.Bot('2033796506:AAFUO6fKAiIDHBSsjNVOmwgKNfixpVCQKNg')
    mc = '-1001560198802'
    # mc = '1860806710'

    f = open('2.png', 'rb')
    ff = open('3.png', 'rb')
    fff = open('4.png', 'rb')
    ffff = open('5.png', 'rb')

    bot.send_photo(mc, f)
    bot.send_photo(mc, ff)
    bot.send_photo(mc, fff)
    bot.send_photo(mc, ffff)

# /  838, 17
    pyautogui.moveTo(838, 17)
    pyautogui.click(838, 17)

#
    t2 = datetime.now()
    delta = t2 - t1
    time.sleep(2700 - delta.total_seconds())
