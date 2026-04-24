import stddraw  # type: ignore
import stdaudio  # type: ignore
import shooter, math, aliens, random, clock, bombs, constants, bunkers, leaderboard, threading, entitymanager

# TODO Remove
import stdio #type: ignore


def play_gameover():
    stdaudio.playFile("./Assets/audio/gameover")


class GameManager:  # class that defines the current instance of the game | Implemeted by James Bam and Robert Van Woudenberg
    def __init__(self, velocity, score_board, player_number):
        self._alien_velocity = velocity  # speed of the alien
        self._score_board = score_board  # score
        self._player_number = player_number
        self.player_lives = 3
        self._player_hit = False

    def play_game(self):

        # -- INITIALISATION

        # create a clock object to track the time between bullets shot
        shooting_clock = clock.Clock(0)
        # create a clock object to track the game time
        clock_main = clock.Clock(0)  

        bullets = []  # create an array of bullet objects as an empty array

        # Create a Shooter (player) instance
        player = shooter.Shooter(
            0.5, # Initial x Position
            0, # Initial Velocity
            bullets, 
            shooting_clock # TODO Delete, localise to shooter.py
        )

        # Create LeaderBoard Manager and Entity Managers
        leaderBoardManager = leaderboard.LeaderBoardManager()
        entityManager = entitymanager.EntityManager(24, 2, self, clock_main, player)

        # Spawn The Aliens TODO Move this somewhere else
        aliens_arr = entityManager.spawn_aliens()

        # Spawn Bunkers
        #bunker1 = bunkers.Bunker(0.2, 0.4, 3, bullets, bombs, aliens_arr)
        #bunker2 = bunkers.Bunker(0.8, 0.4, 3, bullets, bombs, aliens_arr)

        boss_spawned = False

        # We don't want the displayed highscore to change while we play the game,
        # so we get it before the game starts, so the display stays constant while
        # the player played the game.
        player_highscore = leaderBoardManager.get_score(self._player_number)

        # -- MAIN GAME LOOP

        while True:

            #stdio.writeln(str(shooting_clock.get_time()) + " | " + str(clock_main.get_time()))

            # Update Time and Bunker States
            clock_main.updateTime()  # add to the time for the game time
            shooting_clock.updateTime()  # add to the time for the time between shots
            stddraw.clear(stddraw.BLACK)

            entityManager.manage_bombing()

            entityManager.update_aliens()

            entityManager.update_bullets()

            # TODO ENTITY MANAGER

            #bunker1.update_bunker()
            #bunker2.update_bunker()

            # Display Selected Player and Highscore
            stddraw.setPenColor(stddraw.WHITE)
            stddraw.setFontSize(18)
            stddraw.text(
                0.2,
                0.95,
                f"Player {self._player_number} Selected. Highscore: {player_highscore}",
            )
            
            # Draw Count of Player's Lives
            stddraw.text(0.1, 0.9, "Lives: " + str(self.player_lives)) 

            # Spawn a Boss Alien after a specified time has passed.
            #
            """
            if random.randrange(50) == 0 and clock_main.time > 500 and not boss_spawned:
                boss = aliens.Boss(
                    random.random(),
                    random.uniform(0.5, 1),
                    0.005 + 0.002,
                    bullets,
                    False,
                    0,
                    0,
                    player,
                    self._score_board,
                    5,
                )
                boss_spawned = True
            """
            # Check If All Aliens have been killed.
            #
            all_aliens_destroyed = True
            for alien in aliens_arr:
                all_aliens_destroyed = all_aliens_destroyed and alien.dead

            # -- Update Game State



            # Call Shooter Update
            # If the function returns True, the "x" key
            # Has Been Pressed, and we quit the game.
            if player.update_shooter(entityManager):
                return "game_quit"

            # Player Has Beaten The Level
            if all_aliens_destroyed:
                return "level_end"

            # - Fail Conditions

            # Has the player been hit
            # by a bomb?
            if self._player_hit:
                if self.update_game_over():
                    self.end_game()
                    stddraw.show(1000)
                    return "game_over"

            # Manage The Boss Alien
            # Check if it is Alive,
            # Check if it has hit anything,
            # Update its position.
            """
            if boss_spawned:
                if boss.update_alien():
                    if self.update_game_over():
                        self.end_game()
                        stddraw.show(1000)
                        return "game_over"
                    boss_spawned = False
            """
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
        
    def damage_player(self):
        # TODO We need to remove lives from the player here
        self._player_hit = True

    def alien_destroyed(self):
        self._score_board.increment()

            

    # Display Game over in red on the screen
    def end_game(self):
        stddraw.setFontSize(30)
        stddraw.setPenColor(stddraw.RED)
        stddraw.text(0.5, 0.5, "Game Over")
        threading.Thread(target=play_gameover, daemon=True).start()
