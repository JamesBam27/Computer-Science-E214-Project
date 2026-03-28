import stddraw
import math
from picture import Picture

def alien(x,y,vx,vy,xs,ys,blown):
    alien = Picture("Alien.png")
    blownPic = Picture("Blown.png")
    if not 0<x<1:
        vx = -vx
    if not 0 <y<1:
        vy = -vy
    x = x + vx
    y = y + vy
    if (abs(x-xs)<0.2 and abs(y - ys)<0.2) or blown:
        stddraw.picture(blownPic,x,y,0.1,0.1)
        blown = True
    else:
        stddraw.picture(alien,x,y,0.1,0.1)
    return x,y,vx,vy,blown
def main():
    xAlien = 0
    yAlien = 1
    vAlien = 0.001
    vxAlien = -v *math.cos(math.pi/36)
    vyAlien = v * math.sin(math.pi/36)

    while True:
        stddraw.clear()
        xAlien,yAlien,vxAlien,vyAlien = alien(xAlien,yAlien,vxAlien,vyAlien,0,0)
        stddraw.show(10)
if __name__ =="__main__":main()

