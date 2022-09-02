from PIL import Image, ImageDraw
import random


base = Image.new('RGB',(2000,2000),'black')
for x in range(0,2000,10):
    for y in range(0,2000,10):
        if random.choice([True, False]):
            ImageDraw.Draw(base).rectangle((x,y,x+10,y+10),fill ='red')
base.save('rando.png')
