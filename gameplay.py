import shooter
import stddraw
import math
import aliens
import main
import titlescreen
import score
import random
import clock
import bombs
import gameover
class GamePlay:
    def __init__(self,vAlien):
        self.vAlien = vAlien
    def playGame(self):
        gameOver = gameover.GameOver()
        tally =score.scoreBoard()
        timeShot = clock.Clock(0)
        time = clock.Clock(0) 
        x = 0.5
        vx =0
        xs = -1
        ys = -1
        shot =False
        a = math.pi/2
        av =0
        bullet =[shooter.Bullet(xs,ys,a,0.05)]
        playerone = shooter.Shooter(x,vx,shot,a,av,bullet,timeShot)
        xAlien = 0.1
        yAlien = 0.9
        vAlien = self.vAlien
        vxAlien = vAlien *math.cos(math.pi/36)
        vyAlien = -vAlien * math.sin(math.pi/36)
        aliensArr = []
        for i in range(4):
            aliensArr += [aliens.Aliens(xAlien + 0.1*(i+1),yAlien,vxAlien,vyAlien,bullet,False,0.3-0.1*i,0.1*i,playerone,tally,time,gameOver)]
        for i in range(4):
            aliensArr += [aliens.Aliens(xAlien+ 0.1*(i+1),yAlien - 0.1,vxAlien,vyAlien,bullet,False,0.3-0.1*i,0.1*i,playerone,tally,time,gameOver)]
        blown = False
        bomb = bombs.Bomb(1,random.random(),playerone.x,0.15,gameOver)
        while True:
            time.updateTime()
            timeShot.updateTime()
            stddraw.clear(stddraw.GREEN)
            tally.updateScore()
            b = bomb.bombUpdate()
            stddraw.text(0.1,0.9,"Lives: " +str(gameOver.lives))
            if random.randrange(100) == 0 and bomb.y<0:
               bomb.y =1
               bomb.x = random.random()
            bomb.xShooter = playerone.x
            if playerone.shooter():
                return "end"
            f = True
            for i in aliensArr:
                f = f and i.blown
            if f:
                return "endLevel"
            for i in aliensArr:
               i.bullet = bullet
               if i.alien() or b:
                   stddraw.show(1000)
                   return "gameover"
            stddraw.show(10)

def main():
    playGame()

if __name__ == "__main__": main()
