from PIL import Image,ImageDraw
import random

base = Image.new('RGB',(200,200),'black')

foodcount = random.randrange(3,6)
#rando places
for x in range(foodcount):
    x = random.randrange(200)
    y = random.randrange(200)
    ImageDraw.Draw(base).rectangle((x,y,x+random.randrange(5,20),y+random.randrange(5,20)),fill = 'green')
base.save('1.png')
    
