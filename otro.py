import cv2 as cv
import numpy as np

# Global Variables
DELAY_CAPTION = 1500
DELAY_BLUR = 3000
MAX_KERNEL_LENGTH = 31
src = None
dst = None
window_name = 'Smoothing Demo'


def main():
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    imageName = 'Input.jpg'
    global src
    src = cv.imread(cv.samples.findFile(imageName))
    if display_caption('Original Image') != 0:
        return 0
    global dst
    dst = np.copy(src)
    if display_dst(DELAY_CAPTION) != 0:
        return 0
    if display_caption('Gausiana + Bilateral') != 0:
        return 0
    dst = cv.GaussianBlur(src, (3, 3), 0)
    for i in range(1, MAX_KERNEL_LENGTH, 2):
        dst = cv.bilateralFilter(dst, i, i * 2, i / 2)
    cv.imwrite("ResultadosPunto2/result.png", dst)

    if display_dst(DELAY_BLUR) != 0:
        return 0
    display_caption('Done!')
    return 0


def display_caption(caption):
    global dst
    dst = np.zeros(src.shape, src.dtype)
    rows, cols, _ch = src.shape
    cv.putText(dst, caption,
               (int(cols / 4), int(rows / 2)),
               cv.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
    return display_dst(DELAY_CAPTION)


def display_dst(delay):
    cv.imshow(window_name, dst)
    c = cv.waitKey(delay)
    if c >= 0: return -1
    return 0


if __name__ == "__main__":
    main()