import cv2 as cv
import sys
import os

path= sys.argv[1]

files = sorted(os.listdir(path))

for count,i in enumerate(files):
    image = cv.imread(path+"/"+i)
    image = cv.copyMakeBorder(image, 0, 72, 0, 96, cv.BORDER_CONSTANT, None, value = 0)
    cv.imwrite(("./padded/%06d.png" % count),image)
