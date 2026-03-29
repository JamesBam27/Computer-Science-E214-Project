import stdio
import stddraw
import gameplay
def setScale(x=1,y=1):
    stddraw.setXscale(0,x)
    stddraw.setYscale(0,y)
def displayTitleScreen():
    setScale(1,1)
    stddraw.setFontSize(20)
    stddraw.text(0.5,0.9,"COSMIC CONQUISTADORS")
    stddraw.setFontSize(16)
    stddraw.text(0.5,0.7,"Instructions")
    stddraw.setFontSize(12)
    stddraw.text(0.5,60,"[A] move left,[S] stop, [D] move right")
    stddraw.text(0.5,0.5,"[Q] Rotate left, [W] stop rotate, [E] rotate right")
    stddraw.text(0.5,0.4,"[Space] to shoot")
    stddraw.text(0.5,0.3,"[H] for help")
    stddraw.text(0.5,0.2,"[X] to quit")
    

    

    

def main():
    gameplay.playGame()

if __name__ == "__main__":main()

