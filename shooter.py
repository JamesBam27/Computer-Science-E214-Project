import stddraw
from picture import Picture
import math
def shoot(x,y,a,v):
    vx = math.cos(a) * v
    vy = math.sin(a) *v
    x = x  +vx
    y = y  +vy
    stddraw.point(x,y)
    return x,y
def curser(x,y,a):
    y = y + 0.015
    stddraw.line(x,y,x + math.cos(a)/10,y+math.sin(a)/10)
def shooter(x,vx,shot,xs,ys,a,av):
    ship = Picture("ship2.gif")
    vxp = 0.005
    vxn = -0.005
    avp = 0.01
    avn =-0.01
    if stddraw.hasNextKeyTyped():
        key = stddraw.nextKeyTyped()
        if key == "d":
            vx = vxp
        else:
            if key == "a":
                vx  =vxn
            else:
                if key == "s":
                    vx = 0
                else:
                    if key =="x":
                        return
                    else:
                        if key == " ":
                            if not shot:
                                shot = True
                                xs = x
                        else:
                            if key == "e":
                                av = avn
                            else:
                                if key == "q":
                                    av  =avp
                                else:
                                    if key == "w":
                                        av = 0

    a = a  +av
    if not  0<a<math.pi:
        av =-av
    curser(x,0.15,a)
    if shot:    
        xs,ys = shoot(xs,ys,a,0.05)
    if not (0<xs<1 and 0<ys<1):
        shot = False
        xs = 0.5
        ys = 0.15

    if x <0 or x>1:
        vx = -vx
    x = x + vx
    stddraw.picture(ship,x,0.15,0.2,0.2)
    return x, vx, shot,xs,ys,a,av
def main():
    x = 0.5
    vx =0
    xs = 0.5
    ys = 0.15
    shot =False
    a = math.pi/2
    av =0
    while True:
        stddraw.clear()
        x, vx, shot, xs ,ys,a,av = shooter(x,vx,shot,xs,ys,a,av)
        stddraw.show(10)

if __name__ == "__main__":main()
