import stddraw #type: ignore
import stdaudio #type: ignore
from picture import Picture #type: ignore
import math
import threading

class Bullet:

    def __init__(self,x,y,a,v):
        self.x = x
        self.y = y
        self.a = a
        self.v = v

    def shoot(self):
        vx = math.cos(self.a) * self.v
        vy = math.sin(self.a) *self.v
        self.x = self.x + vx
        self.y = self.y + vy
        stddraw.point(self.x,self.y)

def curser(x,y,a):
    y = y + 0.015
    stddraw.line(x,y,x + math.cos(a)/10,y+math.sin(a)/10)

def play_sound():
    stdaudio.playFile("./Assets/audio/Lazer")

class Shooter:
    
    def __init__(self,x, v, shot, a, av, bullet, time):
        self.x = x
        self.velocity = v
        self.angular_velocity = av
        self.angle = a
        self.has_shot = shot
        self.bullet = bullet
        self.time = time

    def shooter(self):
        ship = Picture("./Assets/img/ship2.png")
        vxp = 0.005
        vxn = -0.005
        avp = 0.01
        avn = -0.01
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == "d":
                self.velocity = vxp
            else:
                if key == "a":
                    self.velocity  =vxn
                else:
                    if key == "s":
                        self.velocity = 0
                    else:
                        if key =="x":
                            return True
                        else:
                            if key == " " and (self.time.time>1):
                                threading.Thread(target=play_sound).start()
                                self.time.time = 0 
                                if not self.has_shot:
                                    self.has_shot = True
                                    self.bullet[0].x = self.x
                                    self.bullet[0].y = 0.15
                                    self.bullet[0].a = self.angle
                                else:
                                   self.bullet += [Bullet(self.x,0.15,self.angle,0.05)]

                            else:
                                if key == "e":
                                    self.angular_velocity = avn
                                else:
                                    if key == "q":
                                        self.angular_velocity  =avp
                                    else:
                                        if key == "w":
                                            self.angular_velocity = 0
                                        

        self.angle = self.angle + self.angular_velocity
        if not  0 < self.angle < math.pi:
            self.angular_velocity = -self.angular_velocity
        curser(self.x, 0.15, self.angle)
        for i in self.bullet:   
            if not (0<i.x<1 and 0<i.y<1):
               i.y = -1
               i.x = -1
            else:
                i.shoot() # Updates Bullet Position etc.
		
        if self.x <0 or self.x>1:
            self.velocity = -self.velocity
        self.x = self.x + self.velocity
        stddraw.picture(ship,self.x,0.15)

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

if __name__ == "__main__": main()
