# 图片相似度对比(HSV对比)


import cv2


def compare_images(image_a, image_b):
    img1 = cv2.imread(image_a)
    img2 = cv2.imread(image_b)

    hsv_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    hsv_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)

    hist1 = cv2.calcHist([hsv_img1], [0, 1], None, [180, 256], [0, 180, 0, 256])
    hist2 = cv2.calcHist([hsv_img2], [0, 1], None, [180, 256], [0, 180, 0, 256])

    # 值越小表示越相似
    similarity = cv2.compareHist(hist1, hist2, cv2.HISTCMP_BHATTACHARYYA)
    print(similarity)

compare_images('img1.jpeg', 'img1.jpeg')
compare_images('img1.jpeg', 'img2.jpeg')
compare_images('img1.jpeg', 'img3.jpeg')
compare_images('img1.jpeg', 'img4.jpg')