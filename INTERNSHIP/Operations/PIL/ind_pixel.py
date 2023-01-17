from PIL import Image

thresh=200
img1=Image.open('images\ladybug.jpg')
img1.show()

gray=img1.convert('L')
# gray.show()

x,y=gray.size
# print(x,y)

for i in range(x):
    for j in range(y):
        
      #if intensity less than threshold, assign white
      if gray.getpixel((x,y)) < thresh:
        gray.putpixel((x,y),0)

      #if intensity greater than threshold, assign black 
      else:
        gray.putpixel((x,y),255)

gray.show()


# bin_image=binarize(img)
# bin_image
        



