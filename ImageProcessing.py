from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img)  # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x242F0796160>
print(img.format)  # JPEG
print(img.size)  # (640, 640)
print(img.mode)  # RGB
print(dir(img))  # displays every method we can apply to img

blurred_image = img.filter(ImageFilter.BLUR)
blurred_image.save("blur.png", 'png')

smooth_image = img.filter(ImageFilter.SMOOTH)  # Mainly used for landscape images
smooth_image.save("smooth.png", 'png')

sharpen_image = img.filter(ImageFilter.SHARPEN)
sharpen_image.save('sharpened.png', 'png')

converted_image = img.convert('L')
converted_image.save('grey.png', 'png')
