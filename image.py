from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SHARPEN)
# filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img = img.convert('L')
# rotate the image
# crooked = filtered_img.rotate(120)
# resize the Image
resize = filtered_img.resize((300, 300))
# save the image
resize.save("grey.png", 'png')
# show the image
# filtered_img.show()
resize.show()
