import stddraw #type: ignore
import stdaudio #type: ignore
from picture import Picture #type: ignore
import clock
import score
import math
import threading
import random

def play_gameover():
    stdaudio.playFile("./Assets/audio/gameover")
    
class Aliens:
    def __init__(self,x,y,vx,vy,bullet,blown,width,length,shooter,tally,time,gameover):
        self.x= x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.bullet = bullet
        self.blown = blown
        self.width = width
        self.length = length
        self.shooter = shooter
        self.tally = tally
        self.time = time
        self.gameover = gameover

    def alien(self):
        alien = Picture("./Assets/img/Alien.png")
        if not 0+self.length<=self.x<=1-self.width:
            self.vx = -self.vx
            self.y =self.y - 0.05
        if not self.y<=1:
            pass
        self.x = self.x + self.vx
        
        for i in self.bullet:
            if (abs(self.x-i.x)<0.05 and abs(self.y - i.y)<0.05):
                i.x = -1
                i.y=-1
                self.x = 1
                self.y= 1
                self.width = 0
                self.length = 0
                self.vx = 0
                self.vy = 0
                self.blown = True
                self.tally.addScore()
        if (self.y < 0 or (abs(self.shooter.x-self.x)<0.05 and abs(0.15 - self.y)<0.05) ) and not self.blown:
            self.x = 1
            self.y= 1
            self.width = 0
            self.length = 0
            self.vx = 0
            self.vy = 0
            self.blown = True
            return self.gameover.updateGameOver()
        if not self.blown:
            stddraw.picture(alien,self.x,self.y)
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

