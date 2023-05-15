'''根据图像像素进行相似度对比'''

import os
from PIL import Image


def compare_images(image1_path, image2_path, tolerance=50):
    # Open the images
    image1 = Image.open(image1_path)
    image2 = Image.open(image2_path)

    # Get the size of the images
    width, height = image1.size

    # Count the number of different pixels
    different_pixels = 0
    for x in range(width):
        for y in range(height):
            # Get the RGB values of the pixels
            pixel1 = image1.getpixel((x, y))
            pixel2 = image2.getpixel((x, y))

            # Calculate the difference between the RGB values
            difference = abs(pixel1[0] - pixel2[0]) + abs(pixel1[1] - pixel2[1]) + abs(pixel1[2] - pixel2[2])

            # Check if the difference is greater than the tolerance
            # 一般情况下，人眼对于RGB相差50以内比较难以感知，但对于一些特殊情况(比如色盲)可能会有一定的影响
            if difference > tolerance:
                different_pixels += 1

    # Calculate the percentage of different pixels
    total_pixels = width * height
    percentage = different_pixels / total_pixels * 100

    print(f'percentage: {percentage}')


compare_images('img1.jpeg', 'img1.jpeg')
compare_images('img1.jpeg', 'img2.jpeg')
compare_images('img1.jpeg', 'img3.jpeg')
compare_images('img1.jpeg', 'img4.jpg')