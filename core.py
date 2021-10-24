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
        dilated_img = cv2.dilate(plane, np.ones((blurKernel,blurKernel), np.uint8))
        bg_img = cv2.medianBlur(dilated_img, 21)
        diff_img = 255 - cv2.absdiff(plane, bg_img)
        norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
        #result_planes.append(diff_img) #will add methods prolly
        result_norm_planes.append(norm_img)
    #result = cv2.merge(result_planes)
    result_norm = cv2.merge(result_norm_planes)
    return result_norm

def grayLineArt(img,blurKernel = 7):
    '''
    line art but gray
    '''
    gray_input = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    dilated_img = cv2.dilate(gray_input, np.ones((blurKernel,blurKernel), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(gray_input, bg_img)
    norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    return norm_img

def grayLineArtOld(img,blurKernel = 7):
    '''
    line art but gray
    '''
    hsv_input = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_plane = cv2.split(hsv_input)[0]
    dilated_img = cv2.dilate(h_plane, np.ones((blurKernel,blurKernel), np.uint8))
    bg_img = cv2.medianBlur(dilated_img, 21)
    diff_img = 255 - cv2.absdiff(h_plane, bg_img)
    norm_img = cv2.normalize(diff_img,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    return norm_img


# test func
# img = cv2.imread("testImg/phos.jpg")
# if img is not None:
#     cv2.imshow("image",img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# cv2.imshow("image",cv2.cvtColor(img,cv2.COLOR_BGR2GRAY))
# cv2.waitKey(0)
# cv2.destroyAllWindows()