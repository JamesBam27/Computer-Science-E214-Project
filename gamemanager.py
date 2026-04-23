import stddraw  # type: ignore
import stdaudio  # type: ignore
import shooter, math, aliens, random, clock, bombs, constants, bunkers, leaderboard, threading


def play_gameover():
    stdaudio.playFile("./Assets/audio/gameover")


class GameManager:  # class that defines the current instance of the game | Implemeted by James Bam and Robert Van Woudenberg
    def __init__(self, v, tally, player):
        self.alien_velocity = v  # speed of the alien
        self.tally = tally  # score
        self.selected_player = player
        self.player_lives = 3

    def play_game(self):

        # -- INITIALISATION

        time_shot = clock.Clock(
            0
        )  # create a clock object to track the time between bullets shot
        time = clock.Clock(0)  # create a clock object to track the game time

        leaderBoardManager = leaderboard.LeaderBoardManager()

        # Player Initial Parameters
        x = 0.5  # starting x position for shooter
        vx = 0  # starting velocity of shooter in the x direction
        angle = math.pi / 2  # starting angle of turret
        av = 0  # starting angular velocity of turret
        bullet = []  # create an array of bullet objects as an empty array
        player = shooter.Shooter(
            x, vx, angle, av, bullet, time_shot
        )  # create a Shooter object with the initial values specified above

        # Alien Initial Parameters
        x_alien = 0.1  # starting alien position
        y_alien = 0.9  # starting alien position
        vx_alien = (
            self.alien_velocity
        )  # set the initial alien velocity to that of the game instance
        aliens_arr = []  # inintialise an empty array to store the aliens

        # Spawn All 24 Aliens, in 2 rows of 12

        for i in range(12):
            aliens_arr += [
                aliens.Aliens(
                    x_alien + constants.ALIEN_HITBOX * (i + 1),
                    y_alien,
                    vx_alien,
                    bullet,
                    False,
                    0.55 - constants.ALIEN_HITBOX * i,
                    constants.ALIEN_HITBOX * i,
                    player,
                    self.tally,
                )
            ]

        for i in range(12):
            aliens_arr += [
                aliens.Aliens(
                    x_alien + constants.ALIEN_HITBOX * (i + 1),
                    y_alien - constants.ALIEN_HITBOX,
                    vx_alien,
                    bullet,
                    False,
                    0.55 - constants.ALIEN_HITBOX * i,
                    constants.ALIEN_HITBOX * i,
                    player,
                    self.tally,
                )
            ]

        # Pick a random alien and drop an initial bomb.
        # Game loop will throw and error if bomb is not
        # initially defined.
        random_alien = aliens_arr[random.randrange(0, 24)]
        bomb = bombs.Bomb(random_alien.x, random_alien.y, player.x)

        # Spawn Bunkers
        bunker1 = bunkers.Bunker(0.2, 0.4, 3, bullet, bomb, aliens_arr)
        bunker2 = bunkers.Bunker(0.8, 0.4, 3, bullet, bomb, aliens_arr)

        boss_spawned = False

        # We don't want the displayed highscore to change while we play the game,
        # so we get it before the game starts, so the display stays constant while
        # the player played the game.
        player_highscore = leaderBoardManager.get_score(self.selected_player)

        # -- MAIN GAME LOOP

        while True:

            # Update Time and Bunker States
            time.updateTime()  # add to the time for the game time
            time_shot.updateTime()  # add to the time for the time between shots
            stddraw.clear(stddraw.BLACK)
            bunker1.update_bunker()
            bunker2.update_bunker()

            # Display Selected Player and Highscore
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.setFontSize(18)
            stddraw.text(
                0.2,
                0.95,
                f"Player {self.selected_player} Selected. Highscore: {player_highscore}",
            )

            self.tally.update_score(self.selected_player)  # update the score board
            bomb.set_shooter_x(player.x)
            bomb_hit = bomb.bomb_update()  # update the bombs
            stddraw.text(
                0.1, 0.9, "Lives: " + str(self.player_lives)
            )  # draw the lives in the top right hand corner

            # Spawn a Boss Alien after a specified time has passed.
            #
            if random.randrange(50) == 0 and time.time > 500 and not boss_spawned:
                boss = aliens.Boss(
                    random.random(),
                    random.uniform(0.5, 1),
                    vx_alien + 0.002,
                    bullet,
                    False,
                    0,
                    0,
                    player,
                    self.tally,
                    5,
                )
                boss_spawned = True

            # Check If All Aliens have been killed.
            #
            all_aliens_destroyed = True
            for alien in aliens_arr:
                all_aliens_destroyed = all_aliens_destroyed and alien.dead

            random_alien = aliens_arr[random.randrange(0, 24)]  # choose a random alien

            # If Chosen Alien Is Dead, Try Again
            while random_alien.dead and not all_aliens_destroyed:
                random_alien = aliens_arr[random.randrange(0, 24)]

            # Drop a bomb from the selected Alien.
            # Chance is random, new roll each game loop.
            if random.randrange(100) == 0 and bomb.y < 0:
                bomb.y = random_alien.y
                bomb.x = random_alien.x
                bomb.x_shooter = player.x  # We Give the Bomb Our Players Position

            # -- Update Game State

            # Call Shooter Update
            # If the function returns True, the "x" key
            # Has Been Pressed, and we quit the game.
            if player.update_shooter():
                return "game_quit"

            # Player Has Beaten The Level
            if all_aliens_destroyed:
                return "level_end"

            # - Fail Conditions

            # Has the player been hit
            # by a bomb?
            if bomb_hit:
                if self.update_game_over():
                    self.end_game()
                    stddraw.show(1000)
                    return "game_over"

            # Manage The Boss Alien
            # Check if it is Alive,
            # Check if it has hit anything,
            # Update its position.
            if boss_spawned:
                if boss.update_alien():
                    if self.update_game_over():
                        self.end_game()
                        stddraw.show(1000)
                        return "game_over"
                    boss_spawned = False

            # Check Whether An Alien Has Killed The Player
            for alien in aliens_arr:
                if alien.update_alien():  # Has the alien hit the player?
                    if self.update_game_over():  # Does the player have enough lives?
                        self.end_game()  # Display the gameover message
                        stddraw.show(1000)
                        return "game_over"

            stddraw.show(10)
    #check if the player has enough lives: If they don't remove a life. If they do return true to end the game
    def update_game_over(self):
        if self.player_lives > 0:
            self.player_lives -= 1
            return False
        else:
            return True

    # Display Game over in red on the screen
    def end_game(self):
        stddraw.setFontSize(30)
        stddraw.setPenColor(stddraw.RED)
        stddraw.text(0.5, 0.5, "Game Over")
        threading.Thread(target=play_gameover, daemon=True).start()
