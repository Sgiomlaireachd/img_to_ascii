import cv2
from Braille import braille

magnitude = 7
img = cv2.imread('./bart.jpg')
height, width, clr = img.shape
new_width = width // magnitude
new_height = height // magnitude

if new_width % 2:
    new_width += 1
if new_height % 3:
    new_height += 3 - new_height % 3

print(new_height, new_width)

img = cv2.resize(img, (new_width, new_height))

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

binary_img = cv2.adaptiveThreshold(
    gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
print(binary_img.shape)

res = ''
for i in range(0, new_height, 3):
    for j in range(0, new_width, 2):
        params = [
            binary_img[i][j] == 255,
            binary_img[i][j+1] == 255,
            binary_img[i+1][j] == 255,
            binary_img[i+1][j+1] == 255,
            binary_img[i+2][j] == 255,
            binary_img[i+2][j+1] == 255,
        ]
        res += braille(params)
    res += '\n'

with open('./result.txt', 'w') as file:
    file.write(res)

cv2.imshow('a', binary_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
