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
    def __init__(self,x,y,v_x,bullet,blown,right_bound,left_bound,shooter,tally):
        self.x= x#set the x position
        self.y = y#set the y position
        self.v_x = v_x#set the x velocity
        self.bullet = bullet#set the array of bullets
        self.blown = blown#set if the aliens is dead or alive
        self.right_bound = right_bound#set the right boundary for the alien
        self.left_bound = left_bound#set the left boundary for the alien
        self.shooter = shooter#set the shooter object
        self.tally = tally#set the score
        self.alien = Picture("./Assets/img/Alien.png")
    def kill_alien(self,game_over= False): 
        self.x = 1
        self.y= 1
        self.v_x = 0 #stop the alien
        self.blown = True


    def update_alien(self):
        if not self.left_bound<=self.x<=constants.RIGHT_BOUND-self.right_bound: #if the alien reaches its boundary turn it around and move it down
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
            self.kill_alien(True)
            return True
        if not self.blown:# draw the alien only if it is alive
            stddraw.picture(self.alien,self.x,self.y)
        return False
class Boss(Aliens): #boss class that inherits from the alien class: same as alien except the boss has lives and has to be hit a certain amout of times to die
    def __init__(self,x,y,v_x,bullet,blown,right_bound,left_bound,shooter,tally,health):
        super().__init__(x,y,v_x,bullet,blown,right_bound,left_bound,shooter,tally) #call the parents constructor
        self.health = health
        self.change_alien()
    def change_alien(self):#have a diffrent picture
        self.alien = Picture("./Assets/img/Alien2.png")
    def kill_alien(self,game_over=False):
        if self.health>0 and not game_over:
            self.health -= 1
        else:
            super().kill_alien()


