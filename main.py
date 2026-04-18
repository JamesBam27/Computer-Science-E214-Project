import stddraw #type: ignore
import stdaudio #type: ignore
import stdio #type: ignore
import titlescreen
import gameplay
import threading

# TODO Create a MusicManager
# TODO Group initialisation etc. Make it easier to read. 

class Music():

    def __init__(self):
        self.play = True

    def play_music(self):
        while self.play:
            stdaudio.playFile("./Assets/audio/music")

def main():

    # Display TitleScreen and Play Music

    titlescreen.displayTitleScreen()
    tunes = Music()
    threading.Thread(target=tunes.play_music,daemon=True).start()

    # Wait For A Key to be Pressed, then stop playing music

    while True:
        if stddraw.hasNextKeyTyped():
            key = stddraw.nextKeyTyped()
            tunes.play = False
            stddraw.clear()
            break
        stddraw.show(10)


    # Initialising
    
    vAlien = 0.005
    game = gameplay.GamePlay(vAlien)
    gameStatus = game.playGame()
    level = 0

    # Manage Game State
    # endLevel - 
    # gameover - 
    # end - 
    while True:
        if gameStatus == "endLevel":
            vAlien = vAlien + 0.005
            game.vAlien = vAlien
            level +=1
            stddraw.setFontSize(50)
            stddraw.text(0.5,0.5,"level " +str(level))
            stddraw.show(1000)
            stddraw.setFontSize(12)
        else:
            if gameStatus == "gameover":
                game.vAlien = 0.005
                stddraw.setPenColor(stddraw.BLACK)
                stddraw.setFontSize(12)
                level = 0
            else:
                if gameStatus == "end":
                    break
        gameStatus = game.playGame()

if __name__ == "__main__": main()


