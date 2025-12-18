from PIL import Image

img1 = Image.open("img_red.jpg")
img2 = Image.open("img_blue.jpg")
img3 = Image.open("img_green.jpg")
pack = Image.merge("RGB", (img1, img2, img3))
pack.save("pack.jpg")

img = Image.open("pack.jpg")
img.thumbnail((80, 80))
img.save("avatar.jpg")



