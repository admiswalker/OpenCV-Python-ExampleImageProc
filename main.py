import glob
import numpy as np
import cv2 as cv

def imgRotate180(vPath):
    for i in range(len(vPath)):
        img = cv.imread(vPath[i])
        imgR180 = cv.rotate(img, cv.ROTATE_180)
        cv.imwrite(('out_%03d.png'%(i)), imgR180)    

def range360to255(range360):
    range255 = int(255.0*float(range360)/360.0)
    return range255

def getBinImg_blue(img):
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)
    img_h, img_s, img_v = cv.split(img_hsv);
    
    #cv.imwrite('./img_h.png', img_h)
    #cv.imwrite('./img_s.png', img_s)
    #cv.imwrite('./img_v.png', img_v)
    
    lower = np.array([range360to255(160), 60, 0])
    upper = np.array([range360to255(240), 255, 255])
    bin_img = cv.inRange(img_hsv, lower, upper)
    return bin_img

def centerOfGravity(bin_img):
    h, w = bin_img.shape[:2]
    xg = 0.0
    yg = 0.0
    xg_sum = 0.0
    yg_sum = 0.0
    for hi in range(h):
        for wi in range(w):
            if bin_img[hi][wi] > 127:
                xg_sum += 1.0
                yg_sum += 1.0
                xg += 1.0*wi
                yg += 1.0*hi
            
    return int(xg/xg_sum), int(yg/yg_sum)

def cropImg(img, xg, yg, width, hight):
    y_begin = yg-hight
    y_end = yg+hight
    x_begin = xg-width
    x_end = xg+width
    imgCropped = img[yg-hight:yg+hight, xg-width:xg+width]
    return imgCropped, x_begin, y_begin, x_end, y_end

def main():
    print(cv.__version__)

    vPath = glob.glob('./data/*')
    print(vPath)
    #imgRotate180(vPath)

    img = cv.imread(vPath[0])
    bin_img = getBinImg_blue(img)
    cv.imwrite('./bin_img.png', bin_img)

    xg, yg = centerOfGravity(bin_img)
    print(xg, yg)

    # 1回だけだと，ノイズが多くて重心がずれるので，大まかな領域を切り取ってから，重心を再計算する．
    #cropSize = 30
    #imgCropped = cropImg(img, xg, yg, width=cropSize, hight=cropSize)
    #cv.imwrite('./imgCropped01.png', imgCropped)

    cropSize = 40
    imgBinCropped, x_begin, y_begin, x_end, y_end = cropImg(bin_img, xg, yg, width=cropSize, hight=cropSize)
    cv.imwrite('./imgBinCropped.png', imgBinCropped)
    
    xg_crop, yg_crop = centerOfGravity(imgBinCropped)
    cropSize = 25
    imgCropped, x_begin, y_begin, x_end, y_end = cropImg(img, x_begin+xg_crop, y_begin+yg_crop, width=cropSize, hight=cropSize)
    cv.imwrite('./imgCropped.png', imgCropped) 


main()

