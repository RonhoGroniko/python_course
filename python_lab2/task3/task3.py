from PIL import Image, ImageFilter, ImageOps

capybara = "capybara.jpg"
logo = "realpython-logo.png"
with Image.open(capybara) as img:
    img.load()


with Image.open(logo) as img_logo:
    img_logo.load()


img_logo = img_logo.convert("L")
threshold = 50
img_logo = img_logo.point(lambda x: 255 if x > threshold else 0)
img_logo = img_logo.resize(
    (img_logo.width // 5, img_logo.height // 5)
)

img_logo = img_logo.filter(ImageFilter.CONTOUR)
img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)

img_logo = ImageOps.invert(img_logo)
bbox = img_logo.getbbox()
img_logo = img_logo.crop(bbox)
img_logo = ImageOps.invert(img_logo)


img.paste(img_logo, (150, 150), img_logo)
img.show()

img.save("capybara_with_watermark.jpg", "JPEG")
