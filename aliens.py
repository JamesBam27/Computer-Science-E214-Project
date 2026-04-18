import stddraw #type: ignore
import stdaudio #type: ignore
from picture import Picture #type: ignore
import clock
import score
import math
import threading
import random

def play_gameover():#play the gameover music
    stdaudio.playFile("./Assets/audio/gameover")
    
class Aliens:
    def __init__(self,x,y,vx,bullet,blown,width,length,shooter,tally,time,gameover):
        self.x= x#set the x position
        self.y = y#set the y position
        self.vx = vx#set the x velocity
        self.bullet = bullet#set the array of bullets
        self.blown = blown#set if the aliens is dead or alive
        self.width = width#set the right boundary for the alien
        self.length = length#set the left boundary for the alien
        self.shooter = shooter#set the shooter object
        self.tally = tally#set the score
        self.time = time#set the time
        self.gameover = gameover #set teh gameover object
        self.alien = Picture("./Assets/img/Alien.png")


    def updateAlien(self):
        if not 0+self.length<=self.x<=1-self.width: #if the alien reaches its boundary turn it around and move it down
            self.vx = -self.vx
            self.y =self.y - 0.05
        self.x = self.x + self.vx #move the alien in the x direction
        
        for i in self.bullet:#check all the bullets
            if (abs(self.x-i.x)<0.05 and abs(self.y - i.y)<0.05): #if it is too close to the alien kill the alien 
                i.x = -1 #move its position to off the screen
                i.y=-1
                self.x = 1
                self.y= 1
                self.width = 0
                self.length = 0
                self.vx = 0 #stop the alien
                self.blown = True
                self.tally.addScore()
        if (self.y < 0 or (abs(self.shooter.x-self.x)<0.05 and abs(0.15 - self.y)<0.05) ) and not self.blown: # if an alive alien hits the floor or the player remove a life or end the game
            self.x = 1
            self.y= 1
            self.width = 0
            self.length = 0
            self.vx = 0
            self.vy = 0
            self.blown = True
            return self.gameover.updateGameOver()
        if not self.blown:# draw the alien only if it is alive
            stddraw.picture(self.alien,self.x,self.y)
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

#Test Comment

