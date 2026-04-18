import stddraw #type: ignore

def setScale(x=1,y=1):
    stddraw.setXscale(0,x)
    stddraw.setYscale(0,y)

def displayTitleScreen():

    # Init and Draw Title
    stddraw.clear(stddraw.BLACK)	
    setScale(1,1)
    stddraw.setFontSize(50)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.text(0.5,0.9,"ALIEN INVADERS")

    # Draw Heading
    stddraw.setFontSize(35)
 
    stddraw.text(0.5,0.7,"Instructions")

    # Draw Instructions
    stddraw.setFontSize(18)
    stddraw.text(0.5,0.6,"[A] move left,[S] stop, [D] move right")
    stddraw.text(0.5,0.5,"[Q] Rotate left, [W] stop rotate, [E] rotate right")
    stddraw.text(0.5,0.4,"[Space] to shoot")
    stddraw.text(0.5,0.2,"[X] to quit")
    stddraw.text(0.5,0.1,"PRESS ANY KEY TO START")
