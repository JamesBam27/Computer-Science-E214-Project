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
    while gameplay.playGame():
        stddraw.setPenColor(stddraw.BLACK)
        stddraw.setFontSize(12)



if __name__ == "__main__":main()
