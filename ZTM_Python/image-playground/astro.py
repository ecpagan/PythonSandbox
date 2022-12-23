from PIL import Image, ImageFilter

img = Image.open('astro.jpg')
print(img.size)
img.thumbnail((400, 400))  # will take care of the ration and automatically adjust the sizes
img.save('thumbnail.jpg')
img.show()
