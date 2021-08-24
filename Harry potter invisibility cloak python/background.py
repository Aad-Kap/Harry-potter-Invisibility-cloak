import cv2 #open cv for image capture
#creating a video capture object
cap = cv2.VideoCapture(0) # 0 for integrated camera

#getting the background
while cap.isOpened():
    ret, background = cap.read() # reading from the webcam
    if ret:
        cv2.imshow("image", background)
        if cv2.waitKey(5) == ord('q'):
            #save background image
            cv2.imwrite("image.jpg", background)
            break
cap.release()
cv2.destroyAllWindows()