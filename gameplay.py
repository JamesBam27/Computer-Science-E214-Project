import shooter
import stddraw
import math
import aliens
def playGame():
    x = 0.5
    vx =0
    xs = 0.5
    ys = 0.15
    shot =False
    a = math.pi/2
    av =0
    xAlien = 0
    yAlien = 1
    vAlien = 0.001
    vxAlien = -vAlien *math.cos(math.pi/36)
    vyAlien = vAlien * math.sin(math.pi/36)
    blown = False
    while True:
        stddraw.clear()
        x, vx, shot, xs ,ys,a,av = shooter.shooter(x,vx,shot,xs,ys,a,av)
        xAlien,yAlien,vxAlien,vyAlien,blown = aliens.alien(xAlien,yAlien,vxAlien,vyAlien,xs,ys,blown)
        if xAlien == 0:
            break
        stddraw.show(10)

def main():
    playGame()

if __name__ == "__main__": main()
