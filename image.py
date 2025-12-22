from PIL import Image

img = Image.open("test.jpg")
red, green, blue = img.split()

new_red = red.crop((100, 0, red.width, red.height))
new_green = green.crop((0, 0, blue.width - 100, blue.height))
new_blue = blue.crop((50, 0, green.width - 50, green.height))


new_image = Image.merge("RGB", (new_red, new_green, new_blue))
new_image.thumbnail((100, 100))
new_image.save("new_icon.jpg")


