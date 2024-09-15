from PIL import Image

filename = "Red_Rose.jpg"

with Image.open(filename) as img:
    img.load()

img.getbands()
red, green, blue = img.split()

zeroed_band = red.point(lambda _: 0)

red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))

img.show()
red_merge.show()
green_merge.show()
blue_merge.show()

red_merge.save("red_merge.jpg", "JPEG")
green_merge.save("green_merge.jpg", "JPEG")
blue_merge.save("blue_merge.jpg", "JPEG")