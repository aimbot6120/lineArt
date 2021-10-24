import numpy as np
import cv2

def lineArt(img,blurKernel = 7):
    
    '''
    targets blobs filled with similar colour, attempts to remove the colour, leaving outlines.
    '''
    rgb_planes = cv2.split(img)
    result_planes = []
    result_norm_planes = []
    for plane in rgb_planes:
        dilated_img = cv2.dilate(plane, np.ones((cv2.blur,blurKernel), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        #result_planes.append(diff_img) #will add methods prolly
        result_norm_planes.append(norm_img)
    #result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)
    return result_norm

def grayLineArt(img):
    '''
    line art but gray
    '''
    colour_result = lineArt(img)
    hsv = cv2.cvtColor(colour_result,cv2.COLOR_BGR2HSV)
    return cv2.split(hsv)[0]