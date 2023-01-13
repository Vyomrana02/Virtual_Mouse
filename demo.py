import pyautogui as pg
import sys
try:
    print("Size of screen : ",pg.size())
    x = pg.position()
    print("Current Location of cursor before changing the coordinates : ",x)
    print()
    pg.moveTo(x[0]+50,x[1]+50,duration = 1)
    y = pg.position()
    print("Current Location of cursor before changing the coordinates : ",y)
    print()
except KeyboardInterrupt:
    sys.exit()

# https://stackoverflow.com/questions/56474278/how-to-mirror-live-webcam-video-when-using-opencv