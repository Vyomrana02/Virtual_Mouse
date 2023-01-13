from pynput.keyboard import Key, Listener
import pyautogui as pg
import sys
import keyboard

def show(key):
    x = pg.position()
    if(keyboard.is_pressed('up+left')):
        try:
            pg.moveTo(x[0]-5,x[1]-5)
        except KeyboardInterrupt:
            sys.exit()
    elif(keyboard.is_pressed('up+right')):
        try:
            pg.moveTo(x[0]+5,x[1]-5)
        except KeyboardInterrupt:
            sys.exit()
    elif(keyboard.is_pressed('down+left')):
        try:
            pg.moveTo(x[0]-5,x[1]+5)
        except KeyboardInterrupt:
            sys.exit()
    elif(keyboard.is_pressed('down+right')):
        try:
            pg.moveTo(x[0]+5,x[1]+5)
        except KeyboardInterrupt:
            sys.exit()
    elif(key == key.up):
        try:
            pg.moveTo(x[0],x[1]-5)
        except KeyboardInterrupt:
            sys.exit()
    elif(key == Key.down):
        try:
            # x = pg.position()
            pg.moveTo(x[0],x[1]+5)
        except KeyboardInterrupt:
            sys.exit()
    elif(key == Key.left):
        try:
            # x = pg.position()
            pg.moveTo(x[0]-5,x[1])
        except KeyboardInterrupt:
            sys.exit()
    elif(key == Key.right):
        try:
            # x = pg.position()
            pg.moveTo(x[0]+5,x[1])
        except KeyboardInterrupt:
            sys.exit()
    elif key == Key.esc:
        return False

with Listener(on_press = show) as listener:
	listener.join()