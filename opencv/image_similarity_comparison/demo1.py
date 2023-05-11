# 图片相似度对比(灰度对比)

import cv2

def compare_images(image_a, image_b):
    # 读取图片
    img1 = cv2.imread(image_a)
    img2 = cv2.imread(image_b)

    # 用截取方式将图片缩放成相同大小
    img1 = cv2.resize(img1, (500, 500))
    img2 = cv2.resize(img2, (500, 500))

    # 将图片类型转换为灰度图像
    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 计算直方图
    '''
    参数：
    image：输入图像，必须是一个单通道或多通道的8位图像。
    channels：要计算直方图的通道。列表形式，如[0]表示通道0，[0，1，2]表示所有通道。
    mask：用于排除图像中某些区域的掩膜，如果不需要，可以设置为None。
    histSize：每个通道的直方图大小。例如：[256，256，256]表示每个通道的直方图都有256个bin。
    ranges：每个通道bin的范围。例如：[0,256,0,256,0,256]表示每个通道的bin范围是0-255。
    hist：计算得到的直方图。
    accumulate：是否累加。如果设置为True，则新的直方图将添加到前一个直方图中。

    针对histSize和ranges参数说明:
    在计算直方图时，bin是指将像素值分成的若干个区间。具体来说，我们需要指定像素值的取值范围（通常是0~255），
    并将该范围分成若干个小区间，每个区间就称为一个bin。例
    如，如果我们将像素值的取值范围划分为16个区间，则会得到一个16维的直方图（也称为16个bin的直方图）。
    每个bin中记录的是对应区间内像素值出现的次数。

    bin的数量直接影响了直方图的计算结果。如果我们将像素值范围划分得太细，每个bin内的样本数量会相对较少，
    可能会导致直方图的分布不够平滑，噪声干扰也会比较大。如果bin数量过少，
    则会丢失部分像素值信息，可能会导致直方图无法准确地反映图像中像素的分布情况。
    因此，选取好的bin数量对于直方图的计算结果是至关重要的。在OpenCV中，一般可以通过调整参数来指定bin的数量。
    '''
    img1_hist = cv2.calcHist([img1_gray], [0], None, [256], [0, 256])
    img2_hist = cv2.calcHist([img2_gray], [0], None, [256], [0, 256])

    # 计算两个直方图的相似度
    '''
    cv2.compareHist()函数用于比较两个直方图的相似性。函数的四个参数分别为：

    hist1：第一个直方图。
    hist2：第二个直方图。
    method：直方图比较方法。有四种可选方法：

    - cv2.HISTCMP_CORREL：相关性比较法，值越大表示越相似。取值范围[-1, 1]。当为1时表示两个直方图完全相同，为-1时则完全不同。
    - cv2.HISTCMP_CHISQR：卡方比较法，值越小表示越相似。取值范围[0, ∞)，也就是值越小时越相似。当两个直方图完全相同时，卡方距离为0。
    - cv2.HISTCMP_INTERSECT：交叉比较法，值越大表示越相似。取值范围[0, 1]。当两个直方图相同时，交叉比较为1。
    - cv2.HISTCMP_BHATTACHARYYA：Bhattacharyya距离比较法，值越小表示越相似。取值范围[0, 1]。当两个直方图非常相似时，Bhattacharyya距离为0。当两个直方图完全不同时，Bhattacharyya距离为1。

    mask：可选掩码。如果有选择，只有掩码部分图像的直方图参与计算。

    函数返回值为比较的结果，结果越大则表示两个直方图越相似，结果越小则表示两个直方图越不同。
    '''
    similarity = cv2.compareHist(img1_hist, img2_hist, cv2.HISTCMP_CORREL)

    print(similarity)

compare_images('img1.jpeg', 'img1.jpeg')
compare_images('img1.jpeg', 'img2.jpeg')
compare_images('img1.jpeg', 'img3.jpeg')
compare_images('img1.jpeg', 'img4.jpg')