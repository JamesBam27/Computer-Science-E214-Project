import shooter
import stddraw
import math
import aliens
import main
import titlescreen
import score
def playGame():
    tally =score.scoreBoard() 
    x = 0.5
    vx =0
    xs = -1
    ys = -1
    shot =False
    a = math.pi/2
    av =0
    bullet = shooter.Bullet(xs,ys,a,0.05)
    playerone = shooter.Shooter(x,vx,shot,xs,ys,a,av,bullet)
    xAlien = 0.1
    yAlien = 0.9
    vAlien = 0.008
    vxAlien = vAlien *math.cos(math.pi/36)
    vyAlien = -vAlien * math.sin(math.pi/36)
    aliensArr = []
    for i in range(4):
        aliensArr += [aliens.Aliens(xAlien + 0.1*(i+1),yAlien,vxAlien,vyAlien,0,0,False,0.3-0.1*i,0.1*i)]
    for i in range(4):
        aliensArr += [aliens.Aliens(xAlien+ 0.1*(i+1),yAlien - 0.1,vxAlien,vyAlien,0,0,False,0.3-0.1*i,0.1*i)]
    blown = False
    while True:
        stddraw.clear(stddraw.GREEN)
        tally.updateScore()
        if playerone.shooter():
            break
        for i in aliensArr:
           i.xs = playerone.xs
           i.ys = playerone.ys
           if i.blown:
               tally.addScore()
               i.blown = False
               playerone.shot =False
               playerone.bullet.y=-1
               playerone.bullet.x=-1
               playerone.xs = -1
               playerone.ys = -1
           if i.alien():
               stddraw.show(1000)
               return True
        stddraw.show(10)

def main():
    playGame()

if __name__ == "__main__": main()
