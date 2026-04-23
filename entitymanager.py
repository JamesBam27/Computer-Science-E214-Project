import stddraw  #type: ignore
import stdaudio #type: ignore
import stdio #type: ignores
import shooter, math, aliens, random, clock, bombs, constants, bunkers, leaderboard, threading, score

class EntityManager():

    def __init__(self, alien_count, alien_rows, gamemanager):
        self._alien_count = alien_count
        self._alien_rows = alien_rows
        self._gamemanager = gamemanager
        self._aliens = []

        self.spawn_aliens()
 
    # Function To Spawn/Create aliens initially
    # Function To Update All Aliens               |       Main Update Function
    # - Basically to manage them during runtime,  |       
    #   call each of their updates                |
    # Function To Update All Bunkers              |

    def spawn_aliens(self):

        alien_x_init = 0.1
        alien_y_init = 0.9

        alien_v_init = 0

        bullet = shooter.Bullet(0, 0, 0, 0)

        # Organise Aliens Into Rows
        # We ignore all indexes that fall outside of
        # a perfect set of aliens
        count_per_row = self._alien_count // self._alien_rows
        count_remainder = self._alien_count % self._alien_rows

        for j in range(self._alien_rows):
            for i in range(count_per_row):
                new_alien = aliens.Aliens(
                    alien_x_init + constants.ALIEN_HITBOX * (i + 1),
                    alien_y_init - (constants.ALIEN_HITBOX * j),
                    alien_v_init,
                    bullet,
                    False,
                    0.55 - constants.ALIEN_HITBOX * i,
                    constants.ALIEN_HITBOX * i,
                    shooter.Shooter(0, 0, 0, 0, None, None),
                    score.ScoreBoard(),
                )

                self._aliens.append(new_alien)            

        return self._aliens

    def update_aliens(self, aliens):
        pass

    def update_bullets(self, bullets):
        pass

    def update_boss(self, boss):
        pass

    def spawn_boss(self, boss):
        pass

    def reset_entities(self, aliens, bullets, boss):
        pass



"""
Reference code for alien spawning

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
"""