from PIL import Image
from sys import argv


filename = argv[1]
with Image.open(filename) as img:
    img.load()
red_val = green_val = blue_val = 0

for pixels_h in range(0, img.height):
    for pixels_w in range(0, img.width):
        pixel = img.getpixel((pixels_w, pixels_h))
        r, g, b = pixel
        if r > g and r > b:
            red_val += 1
        elif g > r and g > b:
            green_val += 1
        elif b > r and b > g:
            blue_val += 1

if red_val > green_val and red_val > blue_val:
    dominant_color = 'Red'
elif green_val > red_val and green_val > blue_val:
    dominant_color = 'Green'
else:
    dominant_color = 'Blue'

print(f"Преобладающий цвет: {dominant_color}")