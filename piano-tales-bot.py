from PIL import ImageGrab,Image
from pyautogui import click
from time import sleep
#website to play http://tanksw.com/piano-tiles/
#get a picture of the zone to click
def picOfZone():
    top = [759,700]
    bot = [1159,710]
    pic = ImageGrab.grab([top[0],top[1],bot[0],bot[1]])
    pic.save("pic.jpg")
    return Image.open("pic.jpg")



def iterAndCheck():
    a = 2 #get a value from within the range of x,y
    b = 3 # y 
    for i in range(4):
        value = picOfZone().getpixel((a,b))
        print(value)
        a+=100
        if sum(value) == 51:
            print(i)
            return i
       
def clickThePlace():
    clicks = [
        [792,650],
        [905,650],
        [1000,650],
        [1100,650]
    ]
    placeByIndex = iterAndCheck()
    click(clicks[placeByIndex][0],clicks[placeByIndex][1])

#first = 1,2 - 91,8 | 2nd = 92,2 - 106,8 | 3rd = 196,2 - 288,8 | 4th = 298,2 - 386,8 
while True:
    picOfZone()
    iterAndCheck()
    clickThePlace()