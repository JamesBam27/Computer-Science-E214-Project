import stddraw #type: ignore
import stdaudio #type: ignore
from picture import Picture #type: ignore
import math
import threading

class Bullet:#class to represent a bullet shot by the player

    def __init__(self,x,y,a,v):
        self.x=x#set the x position
        self.y =y#set the y position
        self.a =a#set the angle
        self.v =v#set the velocity

    def shoot(self): #update the position of the bullet and display it on the screen
        vx = math.cos(self.a) * self.v
        vy = math.sin(self.a) *self.v
        self.x = self.x  +vx
        self.y = self.y  +vy
        stddraw.point(self.x,self.y)

def curser(x,y,a):#function to update and draw the turret 
    y = y + 0.015
    stddraw.line(x,y,x + math.cos(a)/25,y+math.sin(a)/25)

def play_sound(): #function that plays the bullet sound
    stdaudio.playFile("./Assets/audio/Lazer")

class Shooter: #class that defines the player
    
    def __init__(self,x,vx,a,av,bullet,time):
        self.x = x #set the x position
        self.vx = vx#set the x velocity
        self.av =av#set the angular velocity
        self.a =a#set the angle
        self.bullet = bullet #set the array of bullets
        self.time = time #set the Clock object of the time
        self.ship = Picture("./Assets/img/ship2.png")#create the picture object of the shooter
        self.vxp = 0.005 #set the positive x velocity
        self.vxn = -0.005#set the negative x velocity
        self.avp = 0.01#set the positive angular velocity of the turret
        self.avn =-0.01#set the negative angular velocity of the turret


    def shooter(self):#method that update the infomation on the shooter and perform all logic of the shooter
        if stddraw.hasNextKeyTyped(): #check if a key has been typed
            key = stddraw.nextKeyTyped() #store the key that was most reacently typed
            if key == "d":
                self.vx = self.vxp #move right
            else:
                if key == "a":
                    self.vx  =self.vxn#move left
                else:
                    if key == "s":
                        self.vx = 0#stop
                    else:
                        if key =="x":
                            return True #close the program
                        else:
                            if key == " " and (self.time.time>5): #shoot the bullet only after a certain amount of time from the last one
                                threading.Thread(target=play_sound).start()#play the bullet sound
                                self.time.time = 0 #reset the shot timer
                                self.bullet += [Bullet(self.x,0.15,self.a,0.05)]#add a bullet to the bullet array
                            else:
                                if key == "e":
                                    self.av = self.avn#move the turret anticlockwise
                                else:
                                    if key == "q":
                                        self.av  =self.avp#move the turet clockwise
                                    else:
                                        if key == "w":
                                            self.av = 0 #stop the turret
                                        

        self.a = self.a  +self.av #move the turret
        if not  0<self.a<math.pi:#if the turret has an angle less than zero and greater than 90 degrees turn the turret around
            self.av =-self.av
        curser(self.x,0.15,self.a)#update and draw the curser
        for i in self.bullet:#check all the bullets
            if not (0<i.x<1 and 0<i.y<1):#if they are off the screen remove them 
               self.bullet.remove(i)
            else:
                i.shoot() #update the position and draw all the bullets

        if self.x <0 or self.x>1:#if the shooter reaches the end of the screen turn around
            self.vx = -self.vx
        self.x = self.x + self.vx#move the shooter
        stddraw.picture(self.ship,self.x,0.15)#draw the shooter

def main():
    x = 0.5
    vx =0
    xs = 0.5
    ys = 0.15
    shot =False
    a = math.pi/2
    av =0
    bullet = Bullet(xs,ys,a,0.01)
    playerone = Shooter(x,vx,shot,xs,ys,a,av,bullet)

    while True:
        stddraw.clear()
        playerone.shooter()
        stddraw.show(10)

if __name__ == "__main__":main()
