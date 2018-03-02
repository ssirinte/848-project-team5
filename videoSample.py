import numpy as np
import cv2

cap = cv2.VideoCapture(0)
#count = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #if count == 0:
        #cv2.imwrite("frame.jpg", frame)
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

    # Display the resulting frame
    lower = np.array([60, 0, 0], dtype = "uint8")
    upper = np.array([140, 100, 100], dtype = "uint8")
 
    # find the colors within the specified boundaries and apply
    # the mask
    #fgmask = fgbg.apply(frame)

    #equ = cv2.equalizeHist(frame)

    #cv2.imshow('frame',fgmask)
    mask = cv2.inRange(frame, lower, upper)
    output = cv2.bitwise_and(frame, frame, mask = mask)
 
    # show the images
    cv2.imshow('frame',np.hstack([frame,output]))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()