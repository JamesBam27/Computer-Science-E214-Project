import stddraw #type: ignore
import stdaudio #type: ignore
import stdio #type: ignore
import titlescreen
import gameplay
import threading
import highscore
import score
#Music class controls and plays the titlescreen music
class Music():

    def __init__(self):
        self.play = True

    def play_music(self):
        while self.play:
            stdaudio.playFile("./Assets/audio/music")

def main():
    stddraw.setCanvasSize(1000,1000) #Set the canvas size to 1000 x 1000 
    scoreManager = highscore.highScore()# Inititalise Score Manager   
    tally = score.ScoreBoard() #create a ScoreBoard object
    titlescreen.displayTitleScreen() #set the title screen on the canvas
    stddraw.setPenColor(stddraw.BLACK) #change pen color to black
    tunes = Music() #create a music object
    threading.Thread(target=tunes.play_music,daemon=True).start() #thread the music to play while the rest of the program executes
    while True:
        if stddraw.hasNextKeyTyped(): #check if a key is pressed
            key = stddraw.nextKeyTyped()
            tunes.play = False #end the music
            stddraw.clear()#clear the title screen
            break #end the title screen loop
        stddraw.show(10) # keep displaying the title screen

    vAlien = 0.0005 #set the starting alien speed
    game = gameplay.GamePlay(vAlien,tally) #create a gameplay object with the initial alien speed and score
    gameStatus = game.playGame() #play th game
    level  =0 #set level to 0
    while True:#game loop
        if gameStatus == "endLevel":#if the .playGame() method returned "endlevel"
            vAlien = vAlien + 0.0025 #increase the speed of the alien
            game.vAlien = vAlien #update the value for the object
            level +=1 #increase the level
            stddraw.setFontSize(50) #change the font size to 50
            stddraw.text(0.5,0.5,"level " +str(level)) #Display the level in the middle of the screen
            stddraw.show(1000)#wait a second to dispaly the level
            stddraw.setFontSize(12)#reset the font size
        else:
            if gameStatus == "gameover":#if the .gamePlay() method returned "gameover"
                game.vAlien = 0.0005 #reset the alien speed
                stddraw.setPenColor(stddraw.BLACK) #reset the pen color
                stddraw.setFontSize(12) #reset the font size
                level = 0#reset the level
                tally.score = 0 #reset the score
            else:
                if gameStatus == "end":#if the .gamePlay() method returned "end"
                    break#end the game
        gameStatus = game.playGame() #play the game again

if __name__ == "__main__": main()
