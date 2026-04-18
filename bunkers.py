import stddraw
import aliens
import bombs
import shooter
import constants
class Bunker():
    def __init__(self,x,y,health,bullet,bomb,alien):
        self.x = x
        self.y  =y
        self.health = health
        self.bullet = bullet
        self.bomb  =bomb
        self.alien = alien
    def update_bunker(self):
        if self.health>0:
            for i in self.bullet:
                if abs(i.x-self.x) <=0.05 and abs(i.y-self.y)<=0.05:
                    self.health -=1
                    i.kill_bullet()
            if abs(self.bomb.x-self.x) <=0.05 and abs(self.bomb.y-self.y)<=0.05:
                self.health -=1
                self.bomb.kill_bomb()
            for i in self.alien:
                if abs(i.x-self.x) <=0.05 and abs(i.y-self.y)<=0.05:
                    self.health -=1
                    i.kill_alien()
            stddraw.filledSquare(self.x,self.y,0.05)



