import numpy as np
from PIL import Image
im=Image.open('C:/Users/Desktop/download.jpg')
pixelMap=im.load()
I=np.asanyarray(Image.open('C:/Users/Desktop/download.jpg'))
img=Image.new(im.mode,im.size)
pixelNew=img.load()
