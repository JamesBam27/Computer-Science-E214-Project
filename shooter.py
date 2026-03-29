import stddraw
from picture import Picture
import math
class Bullet:
    def __init__(shot,x,y,a,v):
        shot.x=x
        shot.y =y
        shot.a =a
        shot.v =v
    def shoot(shot):
        vx = math.cos(shot.a) * shot.v
        vy = math.sin(shot.a) *shot.v
        shot.x = shot.x  +vx
        shot.y = shot.y  +vy
        stddraw.point(shot.x,shot.y)
def curser(x,y,a):
    y = y + 0.015
    stddraw.line(x,y,x + math.cos(a)/10,y+math.sin(a)/10)
class Shooter:
    def __init__(player1,x,vx,shot,xs,ys,a,av,bullet):
        player1.x = x
        player1.vx = vx
        player1.shot = shot
        player1.xs = xs
        player1.ys = ys
        player1.a = a
        player1.av = av
        player1.bullet = bullet

    def shooter(player1):
        ship = Picture("ship2.gif")
        vxp = 0.005
        vxn = -0.005
        avp = 0.01
        avn =-0.01
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            if key == "d":
                player1.vx = vxp
            else:
                if key == "a":
                    player1.vx  =vxn
                else:
                    if key == "s":
                        player1.vx = 0
                    else:
                        if key =="x":
                            return
                        else:
                            if key == " ":
                                if not player1.shot:
                                    player1.shot = True
                                    player1.xs = player1.x
                                    player1.bullet.x = player1.xs
                                    player1.bullet.a = player1.a

                            else:
                                if key == "e":
                                    player1.av = avn
                                else:
                                    if key == "q":
                                        player1.av  =avp
                                    else:
                                        if key == "w":
                                            player1.av = 0

        player1.a = player1.a  +player1.av
        if not  0<player1.a<math.pi:
            player1.av =-player1.av
        curser(player1.x,0.15,player1.a)
        if player1.shot:    
            player1.bullet.shoot()
            player1.xs= player1.bullet.x
            player1.ys = player1.bullet.y
        if not (0<player1.xs<1 and 0<player1.ys<1):
            player1.shot = False
            player1.bullet.y = 0.15
            player1.bullet.x = 0.5
            player1.xs = 0.5
            player1.ys = 0.15

        if player1.x <0 or player1.x>1:
            player1.vx = -player1.vx
        player1.x = player1.x + player1.vx
        stddraw.picture(ship,player1.x,0.15,0.2,0.2)
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
