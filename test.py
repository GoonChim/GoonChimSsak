import pyautogui as pag
import time
import cv2
import telegram
from telegram import chat
import schedule
from datetime import datetime
from imagesearch import *
# print(pag.position())


while True:

    t1 = datetime.now()

    while True:
        # // 'cvd, fire 차트'
        pag.moveTo(584, 11)
        time.sleep(0.2)
        pag.click(584, 11)
        time.sleep(0.2)
        pag.press('f5')
        time.sleep(10)
        num = pag.locateAllOnScreen("1.png", confidence=0.95)

        p_list = list(num)

        if len(p_list) == 0:
            continue
        else:
            num1 = pag.locateCenterOnScreen('1.png')
            pag.click(num1)
            time.sleep(10)

            pag.press('end')
            time.sleep(2)
            # pag.moveTo(1908, 1033)
            # pag.click(1908, 1033, 20, 0.05)
            pag.screenshot('2.png', region=(484, 205, 1010, 530))

            time.sleep(1)
            # /  106,11 //84, 423 //104, 393
        # /  크립토 퀀트 '레버리지, 펀딩비, 미결제'
            # pag.moveTo(106, 11)
            # pag.click(106, 11)
            pag.hotkey('ctrl', '1')
            time.sleep(0.3)

            pag.moveTo(104, 393)
            pag.click(104, 393)
            time.sleep(4)

        # /  272, 278
            pag.screenshot('3.png', region=(272, 278, 1650, 760))
            time.sleep(1.5)

        # /  97, 294
        # /  크립토 퀀트 '총거래소 고래 비율'
            pag.moveTo(97, 294)
            time.sleep(0.3)
            pag.click(97, 294)
            time.sleep(10)

        # /  272, 278
            pag.screenshot('4.png', region=(272, 278, 1650, 760))
            time.sleep(1.5)

        # /  97, 356
        # /  크립토 퀀트 'Stablecoins Ratio'
            pag.moveTo(97, 356)
            time.sleep(0.3)
            pag.click(97, 356)
            time.sleep(7)

        # /  272, 278
            pag.screenshot('5.png', region=(272, 278, 1650, 760))
            time.sleep(1)
            pag.hotkey('ctrl', '2')
            # /  텔레그램 챗 봇
            bot = telegram.Bot(
                '2033796506:AAFUO6fKAiIDHBSsjNVOmwgKNfixpVCQKNg')
            mc = '-1001560198802'
            # mc = '1860806710'

            f = open('2.png', 'rb')
            ff = open('3.png', 'rb')
            fff = open('4.png', 'rb')
            ffff = open('5.png', 'rb')

        # /  838, 17
            bot.send_photo(mc, f)
            time.sleep(0.2)

            bot.send_photo(mc, ff)
            time.sleep(0.2)

            bot.send_photo(mc, fff)
            time.sleep(0.2)

            bot.send_photo(mc, ffff)
            break

# # /  106,11 //84, 423 //104, 393
# # /  크립토 퀀트 '레버리지, 펀딩비, 미결제'
#     # pag.moveTo(106, 11)
#     # pag.click(106, 11)
#     pag.hotkey('ctrl', '1')
#     time.sleep(1)

#     pag.moveTo(104, 393)
#     pag.click(104, 393)
#     time.sleep(4)

# # /  272, 278
#     pag.screenshot('3.png', region=(272, 278, 1650, 760))
#     time.sleep(1.5)

# # /  97, 294
# # /  크립토 퀀트 '총거래소 고래 비율'
#     pag.moveTo(97, 294)
#     time.sleep(0.5)
#     pag.click(97, 294)
#     time.sleep(10)

# # /  272, 278
#     pag.screenshot('4.png', region=(272, 278, 1650, 760))
#     time.sleep(1.5)

# # /  97, 356
# # /  크립토 퀀트 'Stablecoins Ratio'
#     pag.moveTo(97, 356)
#     time.sleep(1.5)
#     pag.click(97, 356)
#     time.sleep(7)

# # /  272, 278
#     pag.screenshot('5.png', region=(272, 278, 1650, 760))
#     time.sleep(1)
#     pag.hotkey('ctrl', '2')

# /  텔레그램 챗 봇
#     bot = telegram.Bot('2033796506:AAFUO6fKAiIDHBSsjNVOmwgKNfixpVCQKNg')
#     # mc = '-1001560198802'
#     mc = '1860806710'

#     f = open('2.png', 'rb')
#     ff = open('3.png', 'rb')
#     fff = open('4.png', 'rb')
#     ffff = open('5.png', 'rb')

# # /  838, 17
#     bot.send_photo(mc, f)
#     time.sleep(0.5)

#     bot.send_photo(mc, ff)
#     time.sleep(0.5)

#     bot.send_photo(mc, fff)
#     time.sleep(0.5)

#     bot.send_photo(mc, ffff)

    #
    t2 = datetime.now()
    delta = t2 - t1
    time.sleep(3600 - delta.total_seconds())
