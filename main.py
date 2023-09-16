import cv2 as cv
import time

def apply_3x3_normalizefilter(image):
    kernel_size = 3
    result=cv.blur(image,(kernel_size,kernel_size))
    return result

def apply_11x11_normalizefilter(image):
    kernel_size = 11
    result=cv.blur(image,(kernel_size,kernel_size))
    return result
def apply_3x3_gaussianfilter(image):
    kernel_size = 3
    result = cv.GaussianBlur(image, (kernel_size, kernel_size),0)
    return result

def apply_11x11_gaussianfilter(image):
    kernel_size = 11
    result = cv.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return result
def apply_3x3_medianFilter(image):
    kernel_size = 3
    result =cv.medianBlur(image, kernel_size)
    return result
def apply_11x11_medianFilter(image):
    kernel_size = 11
    result =cv.medianBlur(image, kernel_size)
    return result

def main():
    imageName = 'Input.jpg'
    src = cv.imread("Input.jpg")

    iterations = 5

    result_3x3=src
    start_time = time.time()
    for _ in range(iterations):
        result_3x3 = apply_3x3_normalizefilter(result_3x3)
    end_time = time.time()
    elapsed_time_3x3 = end_time - start_time
    start_time = time.time()

    result_11x11 = apply_11x11_normalizefilter(src)
    end_time = time.time()
    elapsed_time_11x11 = end_time - start_time

    print(f"Time taken for 3x3 filter applied {iterations} times: {elapsed_time_3x3} seconds")
    print(f"Time taken for 11x11 filter applied once: {elapsed_time_11x11} seconds")

    cv.imshow("3x3 Filter Result", result_3x3)
    cv.imshow("11x11 Filter Result", result_11x11)
    cv.imwrite("ResultadosPunto1/result3x3normalizefilter.png", result_3x3)
    cv.imwrite("ResultadosPunto1/result11x11normalizefilter.png", result_11x11)
    cv.waitKey(0)
    cv.destroyAllWindows()

    result_3x3 = src
    start_time = time.time()
    for _ in range(iterations):
        result_3x3 = apply_3x3_gaussianfilter(result_3x3)
    end_time = time.time()
    elapsed_time_3x3 = end_time - start_time
    start_time = time.time()

    result_11x11 = apply_11x11_gaussianfilter(src)
    end_time = time.time()
    elapsed_time_11x11 = end_time - start_time

    print(f"Time taken for 3x3 filter applied {iterations} times: {elapsed_time_3x3} seconds")
    print(f"Time taken for 11x11 filter applied once: {elapsed_time_11x11} seconds")

    cv.imshow("3x3 Filter Result", result_3x3)
    cv.imshow("11x11 Filter Result", result_11x11)
    cv.imwrite("ResultadosPunto1/result3x3gaussianfilter.png", result_3x3)
    cv.imwrite("ResultadosPunto1/result11x11gaussianfilter.png", result_11x11)
    cv.waitKey(0)
    cv.destroyAllWindows()

    result_3x3 = src
    start_time = time.time()
    for _ in range(iterations):
        result_3x3 = apply_3x3_medianFilter(result_3x3)
    end_time = time.time()
    elapsed_time_3x3 = end_time - start_time
    start_time = time.time()

    result_11x11 = apply_11x11_medianFilter(src)
    end_time = time.time()
    elapsed_time_11x11 = end_time - start_time

    print(f"Time taken for 3x3 filter applied {iterations} times: {elapsed_time_3x3} seconds")
    print(f"Time taken for 11x11 filter applied once: {elapsed_time_11x11} seconds")

    cv.imshow("3x3 Filter Result", result_3x3)
    cv.imshow("11x11 Filter Result", result_11x11)
    cv.imwrite("ResultadosPunto1/result3x3medianFilter.png", result_3x3)
    cv.imwrite("ResultadosPunto1/result11x11medianFilter.png", result_11x11)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return 0

if __name__ == "__main__":
    main()