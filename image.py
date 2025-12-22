from PIL import Image

img = Image.open("test.jpg")
red, green, blue = img.split()

one_red = red.crop((100, 0, red.width, red.height))
second_red = red.crop((50, 0, red.width - 50, red.height))
new_red = Image.blend(one_red, second_red, 0.5)
new_green = green.crop((50, 0, green.width - 50, green.height))
one_blue = blue.crop((0, 0, blue.width - 100, blue.height))
second_blue = blue.crop((50, 0, blue.width - 50, blue.height))
new_blue = Image.blend(one_blue, second_blue, 0.5)


new_image = Image.merge("RGB", (new_red, new_green, new_blue))
new_image.thumbnail((100, 100))
new_image.save("new_icon.jpg")


