from PIL import ImageGrab
import os
import time

import win32api, win32con

from PIL import ImageOps
from numpy import *

import keyboard
from pynput.keyboard import Key, Controller as keyboardController
from pynput.mouse import Button, Controller as mouseController
keyboard = keyboardController()
mouse = mouseController()

import itertools
import math

###########################
#Coordinates
x_pad = 0
y_pad = 0

FirstTabChrome = -1055, -370
dragPointDistance = 50
scrollLeftGsheet = 1222,646
currentTime = str(time.asctime( time.localtime(time.time()) ))
currentTimeCorrected = currentTime.replace(":","-")

############################

def screenGrab():
    time.sleep(2)
    b1 = (x_pad+1 , y_pad+1 , x_pad+288 , y_pad+165)
    im = ImageGrab.grab(b1)
    im.save(os.getcwd() + '\\full_snap__' + currentTimeCorrected + '.png', 'PNG')
    return im

def fullScreenGrab():
    time.sleep(2)
    b1 = (x_pad+1 , y_pad+1 , x_pad+288 , y_pad+165)
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + currentTimeCorrected + '.png', 'PNG')
    return im





def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print ('Click.')
    
def leftDown():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    print ('left Down')
         
def leftUp():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(.1)
    print ('left release')

def mousePos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))

def drag(cord1,cord2):
    win32api.SetCursorPos((x_pad + cord1[0], y_pad + cord1[1]))
    leftDown()
    time.sleep(1)
    win32api.SetCursorPos((x_pad + cord2[0], y_pad + cord2[1]))
    time.sleep(1)
    leftUp()

def click(cord):
    mousePos(cord)
    leftClick()

def write(wordss):
    
    j = 0
    stringWordss = str(wordss)
    i = len(stringWordss)
    while j < i:
        keyboard.press(stringWordss[j])
        # time.sleep(0.0001)
        keyboard.release(stringWordss[j])
        #time.sleep(0.0001)
        j = j + 1
    # time.sleep(0.1)

def erasee():
    keyboard.press('\b')
    time.sleep(0.0001)
    keyboard.release('\b')

def listPrintCreator():
    i = 1
    while i < 14:
        write("targetTime((")
        # write(i)
        # write(" = ")
        time.sleep(0.5)
        i=i+1

#Cloningan tapi kekny salah
def mouseLOC(cord):
    win32api.SetCursorPos(cord)
    
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,",", y)
    detectedCoordinate = x , y
    write(detectedCoordinate)
    return detectedCoordinate

def get_cords_only():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print (x,",", y)
    detectedCoordinate = x , y
    # write(detectedCoordinate)
    return detectedCoordinate

def detect():
    RGBvalues = screenGrab().getpixel(FirstIncoming)
    print(RGBvalues)
    totall = sum(RGBvalues)
    print(totall)
    return totall

def randomize():
    randomx = random.randint(ChromeRefreshRange[0], ChromeRefreshRange[2])
    print(randomx)
    randomy = random.randint(ChromeRefreshRange[1], ChromeRefreshRange[3])
    print(randomy)
    
    ChromeRefresh = randomx, randomy
    print(ChromeRefresh)

    
    return ChromeRefresh
        
def RGBValueTest():
    tempCoord = get_cords()
    RGBvalues = fullScreenGrab().getpixel(tempCoord)
    print(RGBvalues)
    totall = sum(RGBvalues)
    print(totall)
    return totall

def confirmRGBValue(Cords):
    RGBvalues = fullScreenGrab().getpixel(Cords)
    print(RGBvalues)
    totall = sum(RGBvalues)
    print(totall)
    return totall
################################
#KeyBoard Press Functions


def copyy():
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    #time.sleep(0.5)
    keyboard.release('c')
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def pastee():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    time.sleep(0.1)
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def selectAll():
    keyboard.press(Key.ctrl)
    keyboard.press('a')
    #time.sleep(0.5)
    keyboard.release('a')
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def quitEditCell():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    #time.sleep(0.5)
    arrowUpp()

def givef4():
    time.sleep(0.5)
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    arrowLeftt()
    #time.sleep(0.5)
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    #time.sleep(0.5)
    quitEditCell()

def givef4comparative():
    #time.sleep(0.5)
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    #time.sleep(0.5)
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    #time.sleep(0.5)
    j = 0
    while j < 4:
        j = j + 1
        ctrlLeftt()
    #time.sleep(0.5)
    keyboard.press(Key.f4)
    keyboard.release(Key.f4)
    
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    #time.sleep(0.5)
    arrowUpp()

def copyFormula():
    #time.sleep(0.5)
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    #time.sleep(0.5)
    selectAll()
    copyy()
    quitEditCell()

def pasteFormula():
    #time.sleep(0.5)
    keyboard.press(Key.f2)
    keyboard.release(Key.f2)
    #time.sleep(0.5)
    pastee()
    quitEditCell()

def altTab(tabTimes):
    i = 0
    keyboard.press(Key.alt)
    while i < tabTimes:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(1)
        i = i + 1
    keyboard.release(Key.alt)
#####################################
def arrowUpp():
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    time.sleep(0.1)

def arrowDownn():
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    time.sleep(0.1)

def arrowLeftt():
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    time.sleep(0.1)

def arrowRightt():
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(0.1)

def enterr():
    time.sleep(0.1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(0.1)

def escc():
    time.sleep(0.1)
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    time.sleep(0.1)

#########################################
def ctrlshiftUpp():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def ctrlshiftDownn():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def ctrlshiftLeftt():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def ctrlshiftRightt():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.shift)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.release(Key.shift)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)
#######################################
def ctrlUpp():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def ctrlDownn():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def ctrlLeftt():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def ctrlRightt():
    keyboard.press(Key.ctrl)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

def ctrlEnterr():
    time.sleep(0.1)
    keyboard.press(Key.ctrl)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

##############################################

def shiftUpp():
    keyboard.press(Key.shift)
    keyboard.press(Key.up)
    keyboard.release(Key.up)
    keyboard.release(Key.shift)
    time.sleep(0.1)

def shiftDownn():
    keyboard.press(Key.shift)
    keyboard.press(Key.down)
    keyboard.release(Key.down)
    keyboard.release(Key.shift)
    time.sleep(0.1)

def shiftLeftt():
    keyboard.press(Key.shift)
    keyboard.press(Key.left)
    keyboard.release(Key.left)
    keyboard.release(Key.shift)
    time.sleep(0.1)

def shiftRightt():
    keyboard.press(Key.shift)
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    keyboard.release(Key.shift)
    time.sleep(0.1)

def shiftEnterr():
    keyboard.press(Key.shift)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    keyboard.release(Key.shift)
    time.sleep(0.1)

##############################################

def pasteAndSwitchDown():
    ctrlEnterr()
    ctrlDownn()
    arrowRightt()
    arrowRightt()

def pasteAndSwitchUp():
    ctrlEnterr()
    arrowUpp()
    arrowDownn()
    arrowRightt()
    arrowRightt()

##############################################
# Google Chrome Shortcut

def ctrlT(): #open new tab
    keyboard.press(Key.ctrl)
    keyboard.press("t")
    keyboard.release("t")
    keyboard.release(Key.ctrl)
    time.sleep(0.1)

##############################################
#stackoverflow functions

def find_nth(haystack, needle, n): #find nth occurence in string
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

##############################################

def rapidlyShiftingClick(x1,y1,y2):
    shiftingSpeedY = 10 #pilih sendiri
    currentX = x1
    currentY = y2
    
    while currentY > y1:
        currentXandY = currentX , currentY
        click(currentXandY)
        currentY = currentY - shiftingSpeedY
        time.sleep(0.1)

    

def testttt():
    mouse.scroll(0,-1)



i = 0
def main():
    # testttt()
    # rapidlyShiftingClick(487, 555, 666)
    
    # while i in range (19):
    #     get_cords()
    #     time.sleep(2)
    pass
    
 
if __name__ == '__main__':
    main()

