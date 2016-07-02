from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

img = Image.open('image/avatar.jpeg')

draw = ImageDraw.Draw(img)
ttFont = ImageFont.truetype ('arial.ttf', 20)
draw.text((img.size[0]-20, 5), '2', fill=(255, 0, 0), font=ttFont)

del draw
# img.save('image/hello.jpeg', 'JPEG')
img.show()
img.close()