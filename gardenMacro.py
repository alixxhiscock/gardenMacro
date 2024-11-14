import customtkinter
import keyboard
import mouse
import threading
import random
from tkinter import *
import time
import datetime
import mss
from PIL import Image
from discord import SyncWebhook, Embed, File
from dotenv import load_dotenv
load_dotenv()
import os

def Start(use_repellent):
    keyboard.wait('v')
    while True:
        if use_repellent:
            checkRepellent()
        farm(crop)
def farm(crop):
    if crop =="Wart/Carrot":
        oneLength('a', 120)
        oneLength('d', 120)
        oneLength('a', 120)
        oneLength('d', 120)
        oneLength('a', 120)
    elif crop =="Melon/Pumpkin":
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
    elif crop in ["cactus"]:
        time.sleep(2)
        for i in range(0, 10):
            if (checkLocation()):
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
def export():
    toggleButton.configure(text="Stop")
    use_repellent = checkbox_var.get()
    threading.Thread(target=Start,args=(use_repellent,), daemon=True).start()
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
    toggleButton.configure(text="Start")
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
    keyboard.write('/warp garden', random.uniform(0.08, 0.13))
    time.sleep(0.2)
    keyboard.send('enter')

def forwardCactus():
    keyboard.press('w')
    time.sleep(0.28)
    keyboard.release('w')

def initWindow():
    win = customtkinter.CTk()
    win.title("Superfarmer")
    win.geometry("300x300")

    frame = customtkinter.CTkFrame(win,width=300,height=300)
    frame.pack(expand=True,fill=BOTH,padx=10,pady=10)

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)

    global checkbox_var, monitor
    checkbox_var=BooleanVar()
    check = customtkinter.CTkCheckBox(frame, text="Use Repellent:", variable=checkbox_var, font=("Helvetica", 14))
    check.grid(row=0, column=0, columnspan=2, sticky="n", pady=10)
    check.configure(fg_color="#d9534c")
    customtkinter.CTkLabel(frame, text="Crop:", font=("Helvetica", 14)).grid(row=1, column=0, sticky="e", padx=5, pady=5)

    options = ["Melon/Pumpkin","Cactus","Wart/Carrot","Cocoa","Wheat/Potato","Mushroom"]
    def setCrop(choice):
        global crop
        crop=choice
    global dropCrop
    dropCrop = customtkinter.CTkComboBox(frame, values=options,command=setCrop, state="readonly", font=("Helvetica", 12), width=200)
    dropCrop.grid(row=1, column=1, sticky="w", padx=5, pady=5)
    setCrop("Melon/Pumpkin")

    customtkinter.CTkLabel(frame, text="Monitor:", font=("Helvetica", 14)).grid(row=2, column=0, sticky="e", padx=5, pady=5)
    def setMonitor(choice):
        global monitor
        monitor=choice

    dropMonitor = customtkinter.CTkComboBox(frame, values=['1','2','3'],command=setMonitor, state="readonly", font=("Helvetica", 12), width=200)
    dropMonitor.grid(row=2, column=1, sticky="w", padx=5, pady=5)
    setMonitor("1")

    global toggleButton
    toggleButton = customtkinter.CTkButton(frame, text="Macro", command=export, font=("Helvetica", 14), width=10, height=2)
    toggleButton.configure(fg_color="#d9534c")
    toggleButton.grid(row=3, column=0, columnspan=2, pady=20, sticky="n")

    win.mainloop()
def screenshotFore():
    with mss.mss() as mss_instance:
        mss_instance.shot(mon=int(monitor), output=f'monitor-{monitor}.png')
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
        farm(crop)
def inHub():
    if(rgb_of_pixel(f'monitor-{monitor}.png',1802,491) == (77,231,231)): #PC
        return True
    elif(rgb_of_pixel(f'monitor-{monitor}.png',1633,383) == (85, 255, 255)): #Laptop
        return True
    else:
        return False

def rgb_of_pixel(img_path, x, y):
    im = Image.open(img_path).convert('RGB')
    r, g, b = im.getpixel((x, y))
    return (r, g, b)

def sendDiscord(webhookurl,embed=None,image=None):
    try:
        webhook = SyncWebhook.from_url(webhookurl)
        if image:
            webhook.send(file=image)
        elif embed:
            webhook.send(embed=embed)
        else:
            print("No content to send.")
    except Exception as e:
        print(f'An error occurred : {e}')

def sendRepellentTimeDiscord():
    embed = Embed(title="Super Farmer", description=f'Time {calcTimeMessage(0, 1, 0)}', color=0x03b2f8)
    embed.set_author(name=os.getenv('PLAYERNAME'))
    current_time = datetime.datetime.now().strftime("%H:%M:%S %d-%m-%Y")
    embed.set_footer(text=f"Current Time: {current_time}",icon_url="https://discord.do/wp-content/uploads/2023/08/Elite-Skyblock-Farmers.jpg")
    sendDiscord(os.getenv('TIMEWEBHOOK'),embed=embed)

def sendScreenshotDiscord():
    with open("monitor-1.png","rb") as img_file:
        file=File(img_file,"ss.png")
        sendDiscord(os.getenv('IMAGEWEBHOOK'),image=file)

def calcTimeMessage(days,hours,minutes):
    target_time = datetime.datetime.now() + datetime.timedelta(days=days, hours=hours, minutes=minutes)
    timestamp = int(time.mktime(target_time.timetuple()))
    return f"<t:{timestamp}:R>"

def checkRepellent():
    keyboard.press('7')
    time.sleep(0.18)
    mouse.click('right')
    time.sleep(0.18)
    keyboard.press('2')
    sendRepellentTimeDiscord()

if __name__ == '__main__':
    initWindow()