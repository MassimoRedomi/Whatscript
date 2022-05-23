import cv2
import numpy as np
import pyautogui
import time
import random

#region=(890, 1410, 300, 80) CHECK IF MESSAGE
#region=(925, 1500, 80, 80) CHECK SMILE


# check images are the same
def equalimagini(originale, duplicato):
    if originale.shape == duplicato.shape:
        b,g,r=cv2.split(cv2.subtract(originale, duplicato))
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            return True
        else:
            return False
    else:
        return False

# read next val
def lettura():
    img=pyautogui.screenshot(region=(890, 1410, 300, 80))
    img.save("imagini/img.png")
    duplicato=cv2.imread("imagini/img.png")
    originale=cv2.imread("imagini/init.png")

    return originale, duplicato

#phrases
def frasi():
    n=random.randint(1,6)
    if n==1:
        pyautogui.write("Hey Ciao", interval=0.30)
    if n==2:
        pyautogui.write("e tu", interval=0.30)
    if n==3:
        pyautogui.write("hahahaha",interval=0.30)
    if n==4:
        pyautogui.write("NO no", interval=0.30)
    if n==5:
        pyautogui.write("Come vanno le cose?",interval=0.30)
    if n==6:
        pyautogui.write("Bene bene dai",interval=0.30)
    pyautogui.press("enter")


#check if we are in whatsapp
def checkifwhatsapp():
    img=pyautogui.screenshot(region=(925, 1500, 80, 80))
    img.save("imagini/checkdup.png")
    duplicato=cv2.imread("imagini/checkdup.png")
    originale=cv2.imread("imagini/check.png")
    return duplicato, originale

#in case of bad init images, take another screenshots
def takeagaininits():
    time.sleep(5)
    img=pyautogui.screenshot(region=(890, 1410, 300, 80))
    img.save("imagini/init.png")
    img=pyautogui.screenshot(region=(925, 1500, 80, 80))
    img.save("imagini/check.png")

#main loop menu
def mainloop():
    time.sleep(5)

    oricheck, duplicheck=checkifwhatsapp()
    if equalimagini(oricheck, duplicheck):
        print("siamo su whatsapp")
        originale,duplicato=lettura()
        if equalimagini(originale, duplicato):
            print("non è arrivato un messagio")
            time.sleep(2)
            mainloop()
        else:
            print("E arrivato un messaggio")
            frasi()
            frasi()
            mainloop()
    else:
        print("non sono su whatsapp")
        mainloop()

#MAIN

#To work with the script you have 5 seconds to run it and put in place whatsapp
#start de conversation that you want to be automatic

takeagaininits()
mainloop()
