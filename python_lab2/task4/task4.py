from PIL import Image, ImageDraw, ImageFont

width, height = 100, 100
color = (0, 0, 255)

red_color = (255, 0, 0)

card1 = Image.new("RGB", size=(width, height), color=(255, 255, 255))
fnt = ImageFont.truetype("arial.ttf", 50)

d = ImageDraw.Draw(card1)
d.rectangle([(0, 0), (width, 5)], fill=color)
d.rectangle([(0, 0), (5, height)], fill=color)
d.rectangle([(0, height-5), (width, height)], fill=color)
d.rectangle([(width-5, 0), (width, height)], fill=color)


card2 = card1.copy()
card3 = card1.copy()
cards = [card1, card2, card3]

for i in range(1, 4):
    d = ImageDraw.Draw(cards[i-1])
    d.text((width // 2, height // 2), str(i), anchor="mm", fill=red_color, font=fnt)
    cards[i-1].show()
    cards[i-1].save(f"card_{i}.jpg", "JPEG")
