from ctypes.wintypes import RGB
from webbrowser import Grail
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
##1.다양한 그래프 만들기##
'''
x = np.array([5,10,15])
y = np.array([10,20,15])
plt.plot(x,y,'b-o', label='Data 1')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()
plt.show()
'''

##2.라인 그래프 생성하기##
'''
x = np.linspace(0,2,100)
y1 = 0.5 * x
y2 = 0.5 * x**2
y3 = 0.5 * x**3
plt.plot(x,y1,label="linear")
plt.plot(x,y2,label="qudratic")
plt.plot(x,y3,label="cubic")

plt.legend()
plt.show()
'''

##3.B.G.R & R.B.G
#이미지 불러오기
image = cv.imread('cat.jpg')
#1.BGR
plt.figure()
plt.imshow(image)
plt.title("BGR")
#plt.show()

#2.RGB
rgb=cv.cvtColor(image, cv.COLOR_BGR2RGB)
plt.figure()
plt.imshow(rgb)
plt.title("RGB")
#plt.show()

#3.GRAY
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray)
plt.title("gray")
#plt.show()

#4.convert to the GRAY
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title("GRAY")
#plt.show()

#5.blur
blur = cv.blur(image, (50, 50))
blur = cv.cvtColor(blur, cv.COLOR_BGR2RGB)
plt.subplot(121)
plt.imshow(rgb)
plt.title("RGB")
plt.subplot(122)
plt.imshow(blur)
plt.title("Blur")
#plt.show()

#6.Edge Detecction
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(gray, cmap='gray')
plt.title('Gray')

edges=cv.Canny(gray, 100, 200)
plt.subplot(121)
plt.imshow(gray, cmap='gray')
plt.title('Gray')
plt.subplot(122)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detecction")
plt.show()