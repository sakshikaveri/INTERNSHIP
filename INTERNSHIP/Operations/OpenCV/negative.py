import cv2


img1=cv2.imread('images\countryside.jpg')
cv2.imshow('Original image',img1)
cv2.waitKey(0)

img_size=img1.size
print(img_size)
img_shape=img1.shape
print(img_shape)


for x in range(0,256):
    for y in range(0,255):
        output=255-img1
cv2.imshow('Final image',output)
cv2.waitKey(0)
cv2.destroyAllWindows()
            



