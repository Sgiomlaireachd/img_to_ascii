import cv2


def image_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)

    else:
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation=inter)
    return resized


dimensions = 50
img = cv2.imread('./kappa.jpg')
img = image_resize(img, height=dimensions)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

binary_img = cv2.adaptiveThreshold(
    gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# binary_img = cv2.Canny(gray_img, 100, 200)
n, m = binary_img.shape
result = ''
for i in range(n):
    for j in range(m):
        if binary_img[i][j] == 255:
            result += '/'
        if binary_img[i][j] == 0:
            result += ' '
    result += '\n'

with open('./result.txt', 'w') as file:
    file.write(result)
