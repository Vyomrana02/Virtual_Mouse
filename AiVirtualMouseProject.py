import sys
sys.path.append('Users\prath\AppData\Local\Programs\Python\Python38\Lib\site-packages')
import cv2
from pynput.keyboard import Key, Listener
import numpy as np
from pynput.keyboard import Key
import HandTrackingModule as htm
import time
import autopy
import keyboard
import pyautogui as py

##########################
wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 7
#########################

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

# cv2.VideoCapture(video_path or device index )
# device index: It is just the number to specify the camera. Its possible values ie either 0 or -1.
cap = cv2.VideoCapture(0)
cap.set(3, wCam) #set width of cam
cap.set(4, hCam) #set height of cam
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size() #screen size of device in which program is open
# print(wScr, hScr)


def show(key):
    if key == Key.esc:
        return True
    else :
        return False
while True:
    
    # 1. Find hand Landmarks
    success, img = cap.read() #cap.read() returns a bool (True/False) saved in success. If the frame is read correctly, 
    # it will be true and store in img
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img)
    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)


    # 3. Check which fingers are up
    fingers = detector.fingersUp()


    # Scroll up
    if len(fingers) > 4  and fingers[0] == 0 and fingers[1]==1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
        length, img, lineInfo = detector.findDistance(4, 8, img)
        # print("IN FUN2")
        cv2.circle(img, (lineInfo[4], lineInfo[5]),15, (0, 255, 0), cv2.FILLED)
        py.scroll(50)

    # drag drop item drop
    if len(fingers) > 4 and fingers[0]==1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
        py.mouseUp(button='left')
    if (len(fingers)>3 and fingers[3] == 0) or (len(fingers)>4 and fingers[4] == 0):
        
        # 4. Only Index Finger : Moving Mode
        if len(fingers)>4 and fingers[1] == 1 and fingers[2] == 1 and fingers[3]==0 and fingers[4]==0:
        # if len(fingers)>2 and fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            
            # 5. Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 7. Move Mouse
            if length > 40:
                autopy.mouse.move(wScr - clocX, clocY)
                cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
                plocX, plocY = clocX, clocY

        # 8. Both Index and middle fingers are up : Clicking Mode Right CLick
        # if len(fingers) > 2 and fingers[1] == 0 and fingers[2] == 1:
        if len(fingers) > 4 and fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # print(length)
            # 10. Click mouse if distance short
            if length > 30:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),15, (0, 255, 0), cv2.FILLED)
                py.click(button = 'left')
        
        # 8. Both Index and middle fingers are up : Clicking Mode Left CLick
        # if len(fingers) > 2 and fingers[1] == 1 and fingers[2] == 0:
        if len(fingers) > 4 and fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # print(length)
            # 10. Click mouse if distance short
            if length > 30:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),15, (0, 255, 0), cv2.FILLED)
                py.click(button = 'right')

        # Double Click
        if len(fingers) > 4 and fingers[1] == 1 and fingers[2] == 1 and fingers[0]==0 and fingers[3]==0 and fingers[4]==0:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)
            # print(length)
            # 10. Click mouse if distance short
            if length < 30:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),15, (0, 255, 0), cv2.FILLED)
                py.doubleClick()
        
        # Scroll Down
        if len(fingers) > 4  and fingers[0] == 0 and fingers[1]==1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:
            length, img, lineInfo = detector.findDistance(4, 8, img)
            # print("IN FUN")
            cv2.circle(img, (lineInfo[4], lineInfo[5]),15, (0, 255, 0), cv2.FILLED)
            py.scroll(-50)

        # Drag and Drop
        if len(fingers) > 4 and fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            
            # 5. Convert Coordinates
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
            # 6. Smoothen Values
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # 7. Move Mouse
            py.mouseDown(button='left')
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY

    # 11. Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    img = cv2.flip(img,1)
    cv2.putText(img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    # 12. Display
    cv2.imshow("Image", img)
    cv2.waitKey(1)
    if keyboard.is_pressed('esc'):
        cv2.destroyAllWindows()
        cap.release()
        break