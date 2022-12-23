from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('blur.png', 'png')  # may get an error if kept as jpg

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('smooth.png', 'png')  # may get an error if kept as jpg

filtered_img = img.convert('L')  # black/white

crooked = filtered_img.rotate(90)
crooked.save('grey.png', 'png')
crooked.show()

resize = filtered_img.resize((300, 300))
resize.save('resize-gray.png', 'png')
resize.show()

box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save('region-gray.png', 'png')
region.show()

print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))
