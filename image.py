from PIL import Image

img = Image.open("test.jpg")
red, blue, green = img.split()

red.save("img_red.jpg")
blue.save("img_blue.jpg")
green.save("img_green.jpg")

img1 = Image.open("img_red.jpg")
coord_red = (100, 0, img1.width, img1.height)
new_red = img1.crop(coord_red)
new_red.save("new_red.jpg")

img2 = Image.open("img_blue.jpg")
coord_blue = (0, 0, img2.width - 100, img2.height)
new_blue = img2.crop(coord_blue)
new_blue.save("new_blue.jpg")

img3 = Image.open("img_green.jpg")
coord_green = (50, 0, img3.width - 50, img3.height)
new_green = img3.crop(coord_green)
new_green.save("new_green.jpg")

img_red = Image.open("new_red.jpg")
img_blue = Image.open("new_blue.jpg")
img_green = Image.open("new_green.jpg")
new_image = Image.merge("RGB", (img_red, img_blue, img_green))
new_image.save("new_test.jpg")

# new_test = Image.open("new_test.jpg")
# new_test.thumbnail((100, 100))
# new_test.save("test_ava.jpg")

