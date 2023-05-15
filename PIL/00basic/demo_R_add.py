'''把一副图像的RGB通道的R值增加50后输出一副新的图像，观察肉眼是否能识别'''

from PIL import Image


image = Image.open('img1.jpeg')
pixels = image.load()


# image.size返回的是二元组: (width, height)
for i in range(image.size[0]):
    for j in range(image.size[1]):
        # 获取某个位置像素的rgb值
        r, g, b = image.getpixel((i, j))
        # 修改某个位置的rgb像数值
        image.putpixel((i, j), (min(r + 20, 255), min(g + 20, 255), min(b + 20, 255)))

        # 单个通道8左右人眼就可以识别出来
        # image.putpixel((i, j), (min(r + 8, 255), g, b))
        # image.putpixel((i, j), (r, min(g + 2, 255), b))
        # image.putpixel((i, j), (r, g, min(b + 8, 255)))

image.show()
image.save('img1_new.jpeg')