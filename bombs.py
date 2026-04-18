import stddraw #type: ignore
import stdaudio #type: ignore
from picture import Picture #type: ignore
import clock
import random
import threading

class Bomb(): #class that represents a bomb which is to fall from the aliens
    def __init__(self,y,x,xShooter,yShooter,gameOver): 
        self.y = y #set the y coordinate
        self.x = x#set the x coordinate
        self.xShooter = xShooter#set the xposition of the shooter
        self.yShooter = yShooter#set the y position of the shooter
        self.bomb = Picture("./Assets/img/bomb2.png")#set the picture of the bomb
        self.gameOver = gameOver#set the gameover object

    def bombUpdate(self):#move the bomb and check if it has hit a player
        vy = -0.01#set the velocity
        self.y = self.y  + vy#move it down
        stddraw.picture(self.bomb,self.x,self.y)#draw the bomb
        if abs(self.xShooter - self.x)<0.025 and abs(self.yShooter - self.y)<0.025:#check if it got too close the the shooter and if it did take a life
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
