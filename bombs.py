import clock
import stddraw
import random
from picture import Picture
import stdaudio
import threading
import gameover
class Bomb():
    def __init__(self,y,x,xShooter,yShooter,gameOver):
        self.y = y
        self.x = x
        self.xShooter = xShooter
        self.yShooter = yShooter
        self.bomb = Picture("bomb2.png")
        self.gameOver = gameOver
    def bombUpdate(self):
        vy = -0.005
        self.y = self.y  + vy
        stddraw.picture(self.bomb,self.x,self.y)
        if abs(self.xShooter - self.x)<0.05 and abs(self.yShooter - self.y)<0.05:
           self.y = -1 
           return self.gameOver.updateGameOver()
def main():
   bomb = Bomb(1,random.random(),0,0)
   while True:
       stddraw.clear()
       bomb.bombUpdate()
       if (random.randrange(100) == 0 and bomb.y<0):
          bomb.y = 1
          bomb.x = random.random()
       stddraw.show(10)
if __name__ == "__main__": main()
