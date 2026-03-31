import titlescreen
import gameplay
import stddraw
def main():
    titlescreen.displayTitleScreen()
    while True:
        if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                stddraw.clear()
                break
        stddraw.show(10)
    while gameplay.playGame():
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setFontSize(12)



if __name__ == "__main__":main()
