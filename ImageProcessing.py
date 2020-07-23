from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')

print(img)  # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x242F0796160>
print(img.format)  # JPEG
print(img.size)  # (640, 640)
print(img.mode)  # RGB
print(dir(img))  # displays every method we can apply to img

blurred_image = img.filter(ImageFilter.BLUR)
blurred_image.save("./Filtered Images/blur.png", 'png')

smooth_image = img.filter(ImageFilter.SMOOTH)  # Mainly used for landscape images
smooth_image.save("./Filtered Images/smooth.png", 'png')

sharpen_image = img.filter(ImageFilter.SHARPEN)
sharpen_image.save('./Filtered Images/sharpened.png', 'png')

converted_image = img.convert('L')
converted_image.save('./Filtered Images/grey.png', 'png')
converted_image.show()  # displays the image on your systems default viewer

crooked = converted_image.rotate(90)
crooked.save('./Filtered Images/crooked.png', 'png')

resize = converted_image.resize((300, 300))
resize.save('./Filtered Images/resized.png', 'png')

# Cropping Images
box = (100, 100, 400, 400)
region = img.crop(box)
region.save('./Filtered Images/cropped.png', 'png')

astronaut_img = Image.open('./Filtered Images/astro.jpg')
print(astronaut_img.size)  # (5611, 5339)
astronaut_img.thumbnail((400, 400))
astronaut_img.save('./Filtered Images/astronaut_thumbnail.jpg')
print(astronaut_img.size)  # (400, 381)
