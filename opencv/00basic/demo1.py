'''
基础使用

1. 读取图片
2. 保存图片
3. 显示图片
4. 翻转图片
5. 色彩转换
'''


import cv2


# 读取图片
img1 = cv2.imread('img1.jpeg')
print(img1)
# img2 = cv2.imread('image1.jpeg', cv2.IMREAD_COLOR)
# 灰度图片，也就是只有每个像素的亮度，而没有色彩
# 在很多图像处理时，都需要先处理为灰度图像在进行处理，灰度图像处理起来比有色彩的图像更简单
img3 = cv2.imread('img1.jpeg', cv2.IMREAD_GRAYSCALE)
# img4 = cv2.imread('image1.jpeg', cv2.IMREAD_UNCHANGED)

# 保存图片
# cv2.imwrite('image1_1.jpeg', img1)
# cv2.imwrite('image1_2.jpeg', img2)
# cv2.imwrite('image1_3.jpeg', img3)
# cv2.imwrite('image1_4.jpeg', img4)

# 显示图片
# cv2.imshow('image', img3)
# cv2.waitKey(0) # 指定0表示一直等待
# cv2.destroyAllWindows()

# 定义一个显示图片方式，供后续调用
def showImg(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 翻转图片(根据第二个参数来决定按x轴还是y轴，或者xy轴同时翻转)
img5 = cv2.flip(img1, 0)
# showImg(img5)
img5 = cv2.flip(img1, 1)
# showImg(img5)
img5 = cv2.flip(img1, -1)
# showImg(img5)

# 灰度和彩色转换
img6 = cv2.cvtColor(img1, cv2.COLOR_RGB2GRAY)
img7 = cv2.cvtColor(img3, cv2.COLOR_GRAY2RGB)
# RGB转换为HSV/YUV表示
img8 = cv2.cvtColor(img1, cv2.COLOR_RGB2HSV)
img9 = cv2.cvtColor(img1, cv2.COLOR_BGR2YUV)
# showImg(img6)
# showImg(img7)
# showImg(img8)
# showImg(img9)







