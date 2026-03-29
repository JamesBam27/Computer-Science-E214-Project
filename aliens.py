import stddraw
import math
from picture import Picture
class Aliens:
    def __init__(alienOne,x,y,vx,vy,xs,ys,blown,width,length):
        alienOne.x= x
        alienOne.y = y
        alienOne.vx = vx
        alienOne.vy = vy
        alienOne.xs = xs
        alienOne.ys = ys
        alienOne.blown = blown
        alienOne.width = width
        alienOne.length = length

    def alien(alienOne):
        alien = Picture("Alien.png")
        blownPic = Picture("Blown.png")
        if not 0+alienOne.length<alienOne.x<1-alienOne.width:
            alienOne.vx = -alienOne.vx
        if not alienOne.y<1:
            alienOne.vy = -alienOne.vy
        alienOne.x = alienOne.x + alienOne.vx
        alienOne.y = alienOne.y + alienOne.vy
        if (abs(alienOne.x-alienOne.xs)<0.05 and abs(alienOne.y - alienOne.ys)<0.05) or alienOne.blown:
            stddraw.picture(blownPic,alienOne.x,alienOne.y,0.1,0.1)
            alienOne.blown = True
        else:
            stddraw.picture(alien,alienOne.x,alienOne.y,0.1,0.1)
        if alienOne.y < 0 and not alienOne.blown:
            stddraw.setFontSize(30)
            stddraw.setPenColor(stddraw.RED)
            stddraw.text(0.5,0.5,"Game Over")
def main():
    xAlien = 0
    yAlien = 1
    vAlien = 0.001
    vxAlien = vAlien *math.cos(math.pi/36)
    vyAlien = vAlien * math.sin(math.pi/36)
    alien2 = Aliens(xAlien+0.1,yAlien,vxAlien,vyAlien,0,0,False,0.1,0)
    alien1 = Aliens(xAlien+0.2,yAlien,vxAlien,vyAlien,0,0,False,0,0.1)
    while True:
        stddraw.clear()
        alien1.alien()
        alien2.alien()
        stddraw.show(10)
if __name__ =="__main__":main()

