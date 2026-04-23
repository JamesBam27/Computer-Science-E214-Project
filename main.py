import stddraw  # type: ignore
import stdaudio  # type: ignore
import titlescreen, gamemanager, threading, score, leaderboard


# Music class controls and plays the titlescreen music
class Music:

    def __init__(self):
        self.play = True

    def play_music(self):
        while self.play:
            stdaudio.playFile("./Assets/audio/music")


def main():

    # -- INITIALISATION

    # Score and State Related Variables
    leaderBoardManager = (
        leaderboard.LeaderBoardManager()
    )  # Initialise LeaderBoard Manager
    scoreBoard = score.ScoreBoard()  # create a ScoreBoard object
    level = 0
    player_number = 0

    # Canvas
    stddraw.setCanvasSize(1000, 1000)  # Set the canvas size to 1000 x 1000
    titlescreen.displayTitleScreen()  # set the title screen on the canvas
    stddraw.setPenColor(stddraw.WHITE)  # change pen color to black

    # Music
    tunes = Music()  # create a music object
    threading.Thread(target=tunes.play_music, daemon=True).start()

    # -- START GAME

    # Wait For First Valid Input
    while True:
        if stddraw.hasNextKeyTyped():  # check if a key is pressed
            key = stddraw.nextKeyTyped()
            if key in ["1", "2", "3", "4"]:
                player_number = key

                tunes.play = False  # end the music
                stddraw.clear()  # clear the title screen
                break  # end the title screen loop
            elif key == "x":
                tunes.play = False  # end the music
                stddraw.clear()  # clear the title screen
                break

        stddraw.show(10)  # keep displaying the title screen

    # Create a GameManager instance, pass in inital alient velocity, tally object and selected player parameters
    alien_velocity_initial = 0.0005
    gameManager = gamemanager.GameManager(
        alien_velocity_initial, scoreBoard, player_number
    )
    alien_velocity = alien_velocity_initial

    ## -- GAME LOOP

    while True:

        # Run A Game Loop, Store The New Game State
        game_state = gameManager.play_game()

        if game_state == "level_end":

            # The level has ended. Adjust parameters like level value and alien speed.

            alien_velocity = alien_velocity + 0.0008  # increase the speed of the alien
            gameManager._alien_velocity = (
                alien_velocity  # update the value for the object
            )
            level += 1  # increase the level
            stddraw.setFontSize(50)  # change the font size to 50
            stddraw.text(
                0.5, 0.5, "level " + str(level)
            )  # Display the level in the middle of the screen
            stddraw.show(1000)  # wait a second to dispaly the level
            stddraw.setFontSize(18)  # reset the font size

        elif game_state == "game_over":

            # Reset Alien Speed
            gameManager._alien_velocity = alien_velocity_initial 
            alien_velocity  = alien_velocity_initial
            # Reset Canvas Parameters
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.setFontSize(18)

            # Reset The Level, Score and Player Lives
            level = 0
            scoreBoard.score = 0
            gameManager.player_lives = 3

        # If the game has ended, exit the game loop
        elif game_state == "game_quit":
            break


if __name__ == "__main__":
    main()
