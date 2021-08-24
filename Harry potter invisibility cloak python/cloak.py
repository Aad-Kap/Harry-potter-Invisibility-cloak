import cv2 #for image recog
import numpy as np #for arrays

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    #capture the live frame
    ret, cf = cap.read()
    if ret:
        #converting from rgb to hsv color space
        hsv = cv2.cvtColor(cf, cv2.COLOR_BGR2HSV)

        #range for detection of color, in this case RED, can be changed accordingly.

        #lower range for red
        lr = np.array([0,120,70])
        ur = np.array([10,255,255])
        mask1 = cv2.inRange(hsv, lr, ur)

        #upper range for red
        lr = np.array([170,120,70])
        ur = np.array([180,255,255])
        mask2 = cv2.inRange(hsv, lr, ur)

        #generating the final mask

        fMask = mask1 + mask2
        fMask = cv2.morphologyEx(fMask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=10)
        fMask = cv2.morphologyEx(fMask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=10)

        #substituing the red portion with background image to form invisibility illusion

        p1 = cv2.bitwise_and(background, background, mask=fMask)


        #detecting non red things

        red_free = cv2.bitwise_not(fMask)

        #if cloak is not present

        p2 = cv2.bitwise_and(cf, cf, mask=red_free)

        #final output



        cv2.imshow("red cloak", p1+p2)
        if cv2.waitKey(5) == ord('q'):
          break

cap.release()
cv2.destroyAllWindows()


