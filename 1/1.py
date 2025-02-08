import cv2

import numpy as np


def detect_traffic_light_color(image,rect):
    x,y,w,h = rect

    roi = image[y:y+h,x:x+w]

    image_hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

    red_lower = np.array([0,120,70])
    red_upper = np.array([10,250,255])
    


    yellow_lower =np.array([9,100,100])
    yellow_upper = np.array([30,255,255])


    green_lower = np.array([35, 100, 100])  
    green_upper = np.array([85, 255, 255])  



    red_mask = cv2.inRange(image_hsv,red_lower,red_upper)
    yellow_mask = cv2.inRange(image_hsv,yellow_lower,yellow_upper)
    green_mask = cv2.inRange(image_hsv,green_lower,green_upper)

   
    font = cv2.FONT_HERSHEY_TRIPLEX
    font_scale =  0.2
    font_thickness = 1


    if cv2.countNonZero(red_mask) > cv2.countNonZero(yellow_mask) and cv2.countNonZero(red_mask) > cv2.countNonZero(green_mask):
        text_color = (0,0,255)
        message = "Detected signal status : Stop"
        color = "red"


    elif cv2.countNonZero(yellow_mask) > cv2.countNonZero(red_mask) and cv2.countNonZero(yellow_mask) > cv2.countNonZero(green_mask):

        text_color = (0,255,255)
        message = "Detected signal status : Caution"
        color = "yellow"


    else:
        text_color = (0,255,0)
        message = "Dectected signal status : GO"
        color = 'green'



    cv2.putText(image,message,(0,30),font,font_scale+0.5,text_color,font_thickness,cv2.LINE_AA)

    return image,color



image =cv2.imread("traffic1.png")
rect = [421,21,150,300]

output_image, color = detect_traffic_light_color(image, rect)
cv2.imshow("Traffic Light Detection", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
