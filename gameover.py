import stddraw #type: ignore
import stdaudio #type: ignore
import threading

def play_gameover():
    stdaudio.playFile("gameover")
class GameOver:
    def __init__(self):
        self.lives = 3
    def updateGameOver(self):
        if self.lives>0:
            self.lives -=1
            return False
        else:
            stddraw.setFontSize(30)
            stddraw.setPenColor(stddraw.RED)
            stddraw.text(0.5,0.5,"Game Over")
            threading.Thread(target=play_gameover,daemon=True).start()
            return True