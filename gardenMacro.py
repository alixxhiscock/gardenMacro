import keyboard
import time
import mouse
import threading
import random
from tkinter import *
import mss
from PIL import Image

# global variables
global turbo
turbo = False
monitor = 1
crop = "melon"

# Y Values: 1-75 2-73 3-71 4-69 5-67

def Start():
    keyboard.wait('v')
    while True:
        farm()

def farm():
    if crop in ["wart", "carrot"]:
        oneLength('a', 120)
        oneLength('d', 120)
        oneLength('a', 120)
        oneLength('d', 120)
        oneLength('a', 120)
        resetPos()
    elif crop in ["melon", "pumpkin"]:
        #checkRepellent()
        oneLengthMelon('a', 73)
        oneLengthMelon('d', 73)
        oneLengthMelon('a', 73)
        oneLengthMelon('d', 73)
        oneLengthMelon('a', 73)
        oneLengthMelon('d', 73)
        oneLengthMelon('a', 73)
        oneLengthMelon('d', 73)
        oneLengthMelon('a', 73)
        oneLengthMelon('d', 73)
        resetPos()
    elif crop in ["cactus"]:
        cactus()
def export():
    toggleButton['text'] = "Stop"
    threading.Thread(target=Start, daemon=True).start()
    Stop()


def oneLength(keytopress, lengthinsecs):
    checkLocation()
    mouse.press('left')
    time.sleep(random.uniform(0.02, 0.03))
    keyboard.press(keytopress)
    time.sleep(lengthinsecs)
    keyboard.release(keytopress)
    time.sleep(0.6)

def oneLengthMelon(keytopress, lengthinsecs):
    checkLocation()
    mouse.press('left')
    time.sleep(random.uniform(0.02, 0.03))
    keyboard.press(keytopress)
    keyboard.press('w')
    time.sleep(lengthinsecs)
    keyboard.release(keytopress)
    keyboard.release('w')
    time.sleep(0.6)

def Stop():
    toggleButton['text'] = "Start"
    keyboard.wait('x')
    keyboard.release('a')
    keyboard.release('w')
    keyboard.release('d')
    mouse.release('left')
    raise SystemExit(0)


def resetPos():
    time.sleep(0.02)
    keyboard.send('t')
    time.sleep(0.2)
    if (turbo):
        keyboard.write('/warp garden')
    else:
        keyboard.write('/warp garden', random.uniform(0.08, 0.13))
    time.sleep(0.2)
    keyboard.send('enter')

def forwardCactus():
    keyboard.press('w')
    time.sleep(0.28)
    keyboard.release('w')
    print("finished forward")


def toggleTurbo():
    global turbo
    turbo = not turbo


def initWindow():
    win = Tk()
    win.title("Superfarmer")
    win.geometry("300x300")
    global toggleButton
    toggleButton = Button(win, text="Macro", command=export, width=300, height=100)
    toggleButton.config(font=("Helvetica", 40))
    toggleButton.pack()
    turboButton = Button(win, text="Turbo", command=toggleTurbo, width=300, height=100)
    win.mainloop()


def screenshotFore():
    global monitor
    with mss.mss() as mss_instance:
        mss_instance.shot(mon=monitor, output=f'monitor-{monitor}.png')
def checkLocation():
    screenshotFore()
    if inHub():
        print("Detected in Hub or Village")
        keyboard.send('t')
        time.sleep(0.2)
        keyboard.write('/warp garden', random.uniform(0.08, 0.13))
        time.sleep(0.2)
        keyboard.send('enter')
        time.sleep(2)
        keyboard.release('a')
        keyboard.release('d')
        mouse.release('left')
        farm()
def inHub():
    if(rgb_of_pixel(f'monitor-{monitor}.png',1739,466) == (79, 236, 236)): #PC
        return True
    elif(rgb_of_pixel(f'monitor-{monitor}.png',1633,383) == (85, 255, 255)): #Laptop
        return True
    else:
        return False

def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    return (r, g, b)

def checkRepellent():
    keyboard.press('7')
    time.sleep(0.18)
    mouse.click('right')
    time.sleep(0.18)
    keyboard.press('2')

def cactus():
    checkRepellent()
    for i in range(0,10):
        if(checkLocation()):
            print('in hub')
            return True
        keyboard.press('2')
        oneLength('a', 24)
        forwardCactus()
        if (checkLocation()):
            return True
        oneLength('d', 24)
        forwardCactus()
    if (checkLocation()):
        return True
    oneLength('a', 24)
    forwardCactus()
    if (checkLocation()):
        return True
    oneLength('d', 24)
    resetPos()
    time.sleep(2)

if __name__ == '__main__':
    initWindow()