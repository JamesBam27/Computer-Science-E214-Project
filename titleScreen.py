import stdio
import stddraw
def setScale(x=1,y=1):
    stddraw.setXscale(0,x)
    stddraw.setYscale(0,y)
def displayTitleScreen():
    setScale(100,100)
    stddraw.setFontSize(20)
    stddraw.text(50,90,"COSMIC CONQUISTADORS")
    stddraw.setFontSize(16)
    stddraw.text(50,70,"Instructions")
    stddraw.setFontSize(12)
    stddraw.text(50,60,"[A] move left,[S] stop, [D] move right")
    stddraw.text(50,50,"[Q] Rotate left, [W] stop rotate, [E] rotate right")
    stddraw.text(50,40,"[Space] to shoot")
    stddraw.text(50,30,"[H] for help")
    stddraw.text(50,20,"[X] to quit")
    while True:
        if stddraw.hasNextKeyTyped():
            if stddraw.nextKeyTyped() =="x":
                break
        stddraw.show(10)

    

    

def main():
    displayTitleScreen()

if __name__ == "__main__":main()

