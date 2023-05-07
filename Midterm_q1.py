from PIL import Image,ImageEnhance


# Open the image
image = Image.open('C:/Users/Fatih Kemal Terzi/image.tiff')



#Color correection

# Apply color correction
brightness = 1.0
contrast = 1.2
saturation = 1.5

# Adjust brightness
enhancer = ImageEnhance.Brightness(image)
image = enhancer.enhance(brightness)

# Adjust contrast
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(contrast)

# Adjust saturation
enhancer = ImageEnhance.Color(image)
image = enhancer.enhance(saturation)


image.save('enhanced_image_2.jpg')

# #cropping and resizing an image

# left = 500
# top = 500
# right =500
# bottom = 500
# image = image.crop((left, top, right, bottom))

# width = 500
# height = 500
# image = image.resize((width, height))

# image.save('d7.jpg')

# image.show()
