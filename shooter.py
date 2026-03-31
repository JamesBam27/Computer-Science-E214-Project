import stddraw
from picture import Picture
import math
class Bullet:
    def __init__(self,x,y,a,v):
        self.x=x
        self.y =y
        self.a =a
        self.v =v
    def shoot(self):
        vx = math.cos(self.a) * self.v
        vy = math.sin(self.a) *self.v
        self.x = self.x  +vx
        self.y = self.y  +vy
        stddraw.point(self.x,self.y)
def curser(x,y,a):
    y = y + 0.015
    stddraw.line(x,y,x + math.cos(a)/10,y+math.sin(a)/10)
class Shooter:
    def __init__(self,x,vx,shot,xs,ys,a,av,bullet):
        self.x = x
        self.vx = vx
        self.shot = shot
        self.xs = xs
        self.ys = ys
        self.a = a
        self.av = av
        self.bullet = bullet

    def shooter(self):
        ship = Picture("ship2.png")
        vxp = 0.005
        vxn = -0.005
        avp = 0.01
        avn =-0.01
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == "d":
                self.vx = vxp
            else:
                if key == "a":
                    self.vx  =vxn
                else:
                    if key == "s":
                        self.vx = 0
                    else:
                        if key =="x":
                            return True
                        else:
                            if key == " ":
                                if not self.shot:
                                    self.shot = True
                                    self.xs = self.x
                                    self.bullet.x = self.x
                                    self.bullet.y = 0.15
                                    self.bullet.a = self.a

                            else:
                                if key == "e":
                                    self.av = avn
                                else:
                                    if key == "q":
                                        self.av  =avp
                                    else:
                                        if key == "w":
                                            self.av = 0
                                        

        self.a = self.a  +self.av
        if not  0<self.a<math.pi:
            self.av =-self.av
        curser(self.x,0.15,self.a)
        if self.shot:    
            self.bullet.shoot()
            self.xs= self.bullet.x
            self.ys = self.bullet.y
        if not (0<self.xs<1 and 0<self.ys<1):
            self.shot = False
            self.bullet.y = -1
            self.bullet.x = -1
            self.xs = -1
            self.ys = -1
		
        if self.x <0 or self.x>1:
            self.vx = -self.vx
        self.x = self.x + self.vx
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

if __name__ == "__main__":main()
