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
    bullet = shooter.Bullet(xs,ys,a,0.05)
    playerone = shooter.Shooter(x,vx,shot,xs,ys,a,av,bullet)
    xAlien = 0
    yAlien = 1
    vAlien = 0.005
    vxAlien = -vAlien *math.cos(math.pi/36)
    vyAlien = vAlien * math.sin(math.pi/36)
    alien2 = aliens.Aliens(xAlien+0.1,yAlien,vxAlien,vyAlien,0,0,False,0.1,0)
    alien1 = aliens.Aliens(xAlien+0.2,yAlien,vxAlien,vyAlien,0,0,False,0,0.1)
    blown = False
    while True:
        stddraw.clear()
        playerone.shooter()
        alien1.xs = playerone.xs
        alien1.ys= playerone.ys
        alien1.shot = playerone.shot
        alien2.xs = playerone.xs
        alien2.ys= playerone.ys
        alien2.shot = playerone.shot
        alien1.alien()
        alien2.alien()
        stddraw.show(10)

def main():
    playGame()

if __name__ == "__main__": main()
