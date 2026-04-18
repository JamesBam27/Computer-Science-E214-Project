import stddraw #type: ignore
import stdaudio #type: ignore
from picture import Picture #type: ignore
import clock
import score
import math
import threading
import random
import constants
    
class Aliens:
    def __init__(self,x,y,v_x,bullet,blown,width,length,shooter,tally,time,game_over):
        self.x= x#set the x position
        self.y = y#set the y position
        self.v_x = v_x#set the x velocity
        self.bullet = bullet#set the array of bullets
        self.blown = blown#set if the aliens is dead or alive
        self.width = width#set the right boundary for the alien
        self.length = length#set the left boundary for the alien
        self.shooter = shooter#set the shooter object
        self.tally = tally#set the score
        self.time = time#set the time
        self.game_over = game_over #set the gameover object
        self.alien = Picture("./Assets/img/Alien.png")
    def kill_alien(self): 
        self.x = 1
        self.y= 1
        self.width = 0
        self.length = 0
        self.v_x = 0 #stop the alien
        self.blown = True


    def update_alien(self):
        if not self.length<=self.x<=constants.RIGHT_BOUND-self.width: #if the alien reaches its boundary turn it around and move it down
            self.v_x = -self.v_x
            self.y =self.y - 0.05
        self.x = self.x + self.v_x #move the alien in the x direction
        
        for i in self.bullet:#check all the bullets
            if (abs(self.x-i.x)<constants.ALIEN_HITBOX and abs(self.y - i.y)<constants.ALIEN_HITBOX): #if it is too close to the alien kill the alien 
                i.x = -1 #move its position to off the screen
                i.y=-1
                self.kill_alien()
                self.tally.add_score()
        if (self.y < constants.BOTTOM_BOUND or (abs(self.shooter.x-self.x)<constants.ALIEN_HITBOX and abs(constants.SHOOTER_Y - self.y)<constants.ALIEN_HITBOX) ) and not self.blown: # if an alive alien hits the floor or the player remove a life or end the game
            self.kill_alien()
            return True
        if not self.blown:# draw the alien only if it is alive
            stddraw.picture(self.alien,self.x,self.y)
        return False
def main():
    xAlien = 0
    yAlien = 1
    vAlien = 0.001
    v_xAlien = vAlien *math.cos(math.pi/36)
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

