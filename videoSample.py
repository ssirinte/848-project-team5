'''
# Python program for Detection of a 
# specific color(blue here) using OpenCV with Python
import cv2
import numpy as np 
 
# Webcamera no 0 is used to capture the frames
cap = cv2.VideoCapture(0) 
 
# This drives the program into an infinite loop.
while(1):       
    # Captures the live stream frame-by-frame
    _, frame = cap.read() 
    # Converts images from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([110,50,50])
    upper_red = np.array([130,255,255])
 
    # Here we are defining range of bluecolor in HSV
    # This creates a mask of blue coloured 
    # objects found in the frame.
    mask = cv2.inRange(hsv, lower_red, upper_red)
     
    # The bitwise and of the frame and mask is done so 
    # that only the blue coloured objects are highlighted 
    # and stored in res
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
     
    # This displays the frame, mask 
    # and res which we created in 3 separate windows.
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
 
# Destroys all of the HighGUI windows.
cv2.destroyAllWindows()
 
# release the captured frame
cap.release()
'''
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#count = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #if count == 40:
    #    cv2.imwrite("frame.jpg", frame)
    #fgbg = cv2.BackgroundSubtractorMOG()
    
    #count += 1
    # Our operations on the frame come here

    # define the list of boundaries
    boundaries = [
        ([17, 15, 100], [50, 56, 200]),
        ([86, 31, 4], [220, 88, 50]),
        ([25, 146, 190], [62, 174, 250]),
        ([103, 86, 65], [145, 133, 128])
    ]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    lower = np.array([-7, 100, 100], dtype = "uint8")
    upper = np.array([13, 255, 255], dtype = "uint8")
 
    # find the colors within the specified boundaries and apply
    # the mask
    #fgmask = fgbg.apply(frame)

    #equ = cv2.equalizeHist(frame)

    #cv2.imshow('frame',fgmask)
    mask = cv2.inRange(hsv, lower, upper)
    output = cv2.bitwise_and(hsv, hsv, mask = mask)
 
    # show the images
    cv2.imshow('frame',np.hstack([frame,output]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
