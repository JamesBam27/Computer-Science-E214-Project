import stddraw  # type: ignore
import stdaudio  # type: ignore
import titlescreen
import gamemanager
import threading
import highscore
import score
import leaderboard


# TODO Create a MusicManager
# TODO Group initialisation etc. Make it easier to read. 

# Music class controls and plays the titlescreen music
class Music:

    def __init__(self):
        self.play = True

    def play_music(self):
        while self.play:
            stdaudio.playFile("./Assets/audio/music")


def main():

    # -- INITIALISATION

    ## -- TEST

    leaderBoard = leaderboard.LeaderBoardManager()

    return

    ## -- END TEST

    # Score and State Related Variables
    score_manager = highscore.highScore()  # Inititalise Score Manager
    tally = score.ScoreBoard()  # create a ScoreBoard object
    level = 0 
    
    # Canvas
    stddraw.setCanvasSize(1000, 1000)  # Set the canvas size to 1000 x 1000   
    titlescreen.displayTitleScreen()  # set the title screen on the canvas
    stddraw.setPenColor(stddraw.WHITE)  # change pen color to black
    tunes = Music()  # create a music object
    threading.Thread(
        target=tunes.play_music, daemon=True
    ).start() 

    # -- START GAME

    # Wait For The Initial Key Press To Start The Game
    while True:
        if stddraw.hasNextKeyTyped():  # check if a key is pressed
            key = stddraw.nextKeyTyped()
            tunes.play = False  # end the music
            stddraw.clear()  # clear the title screen
            break  # end the title screen loop
        stddraw.show(10)  # keep displaying the title screen

    # Create a gameplay object, pass in inital alient velocity and tally object parameters
    vAlien = 0.0005
    gameManager = gamemanager.GameManager(
        vAlien, tally
    )
    

    ## -- GAME LOOP

    while True: 

        # Run The Next Game Loop, Store The New Game State
        game_state = gameManager.play_game() 

        if game_state == "level_end":  # if the .playGame() method returned "endlevel" # TODO level_end

            # The level has ended. Adjust parameters like level value and alien speed.

            vAlien = vAlien + 0.0008  # increase the speed of the alien
            gameManager.vAlien = vAlien  # update the value for the object
            level += 1  # increase the level

            # TODO Get this display changing out of here and somewhere else
            
            stddraw.setFontSize(50)  # change the font size to 50
            stddraw.text(
                0.5, 0.5, "level " + str(level)
            )  # Display the level in the middle of the screen
            stddraw.show(1000)  # wait a second to dispaly the level
            stddraw.setFontSize(18)  # reset the font size

        elif game_state == "game_over": # TODO game_over
            # if the .gamePlay() method returned "gameover"
            gameManager.vAlien = 0.0005  # reset the alien speed
            stddraw.setPenColor(stddraw.WHITE)  # reset the pen color
            stddraw.setFontSize(18)  # reset the font size
            level = 0  # reset the level
            tally.score = 0  # reset the score

        # If the game has ended, exit the game loop
        elif game_state == "game_quit": # if the .gamePlay() method returned "end" # TODO game_quit
            break


if __name__ == "__main__": main()


