import titlescreen
import gameplay
import stddraw
import threading
import stdaudio
class Music():
    def __init__(self):
        self.play = True
    def play_music(self):
        while self.play:
            stdaudio.playFile("music")
def main():
    titlescreen.displayTitleScreen()
    tunes = Music()
    threading.Thread(target=tunes.play_music,daemon=True).start()
    while True:
        if stddraw.hasNextKeyTyped():
                key = stddraw.nextKeyTyped()
                tunes.play = False
                stddraw.clear()
                break
        stddraw.show(10)
    vAlien = 0.005
    game = gameplay.GamePlay(vAlien)
    gameStatus = game.playGame()
    level  =0
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



if __name__ == "__main__":main()
