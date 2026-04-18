import stddraw #type: ignore
import stdaudio #type: ignore
import threading

def play_gameover():
   stdaudio.playFile("./Assets/audio/gameover")
class GameOver:
    def __init__(self):
        self.lives = 3
    def update_game_over(self):
        if self.lives>0:
            self.lives -=1
            return False
        else:
            return True
    def end_game(self):
        stddraw.setFontSize(30)
        stddraw.setPenColor(stddraw.RED)
        stddraw.text(0.5,0.5,"Game Over")
        threading.Thread(target=play_gameover,daemon=True).start()
        
