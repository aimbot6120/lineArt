from numpy import result_type
import core
import sys
import cv2

def help():
    print("usage - main.py [filename] [option {1,2}]\n")

def parser():
    n = len(sys.argv)
    if n == 2:
        str = sys.argv[1]
        return str,1
            
    elif n == 3:
        str = sys.argv[1]
        num = int(sys.argv[2])

        if num == 1 or num == 2:  #color
            return str, num
        else:
            print("invalid option\n")
            help()
            exit(0)
    elif n == 1:
        help()
        exit()
    else:
        print("too many arguments\n")
        help()
        exit()

def imgLoader(str):
    img = cv2.imread(str)
    if img is None:
        print(" cannot read or find image")
        exit(0)
    return img

def imgWriter(img,str,option):
    filename = ""
    # if option == 1:
    #     filename = "color_"+str
    # if option == 2:
    #     filename = "gray_"+str
    filename = str #ask for filename
    cv2.imwrite(filename,img)
    print("saved as " + filename + "\n")

def applyFilter(img,option):
    if option == 1:
        return core.lineArt(img)
    if option == 2:
        return core.grayLineArt(img)

def main():
    str,option = parser()
    img = imgLoader(str)
    imgWriter(applyFilter(img,option),str,option)

if __name__ == "__main__":
    main()

