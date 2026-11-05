import pyautogui
import keyboard
import random
import time

vel = [0.0,0.0]
width, height = pyautogui.size()
pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0

def clamp(n, min_val, max_val):
    return max(min_val, min(n, max_val))

maxspeed = 1.0

counter = 0
while True:
    vel[0] += random.randrange(-1,2)*0.01
    vel[1] += random.randrange(-1,2)*0.01

    vel[0] = clamp(vel[0],-maxspeed,maxspeed)
    vel[1] = clamp(vel[1],-maxspeed,maxspeed)
# tyeestgrdhj
    pos = pyautogui.position()

    if pos.x >= width-10 or pos.x == 0:
        vel[0] *= -1

    if pos.y >= width-10 or pos.y == 0:
        vel[1] *= -1


    pyautogui.moveRel(vel[0],vel[1],0,0,False,False)

    if keyboard.is_pressed("esc"):
        break

    time.sleep(0)