# from PIL import Image
# im=Image.open('test1.png')
# rgb_im=im.convert('RGB')
# r,g,b=rgb_im.getpixel((150,1))
# print(r,g,b)

import scipy.misc
from PIL import Image
import numpy as np
import random
img=scipy.misc.read("map.png")
count_pun=0
count_in=0
count=0
while count<100000:
    x=random.randint(0, 2735)
    y=random.randint(0, 2480)
    z=0
    if img[x][y][z]==60:
       count_in=count_in+1
       count=count+1
    else:
        if(img[x][y][z]==80):
            count_pun=count_pun+1
            count=count+1
            
area=(count_in/count_pun)*3287263
print(area_pun)
            
        