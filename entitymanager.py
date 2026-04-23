import stddraw  #type: ignore
import stdaudio #type: ignore
import stdio #type: ignores
import shooter, math, aliens, random, clock, bombs, constants, bunkers, leaderboard, threading, score

class EntityManager():

    def __init__(self, alien_count, alien_rows, gamemanager, manager_clock, player_reference):
        self._alien_count = alien_count
        self._alien_rows = alien_rows
        self._gamemanager = gamemanager
        self._aliens = []
        self._clock_manager = manager_clock
        self._bomb_interval = 100
        self._last_bomb_time = 0
        self._bombs = []
        self._player_ref = player_reference

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
                    score.ScoreBoard(),
                )

                self._aliens.append(new_alien)            

        return self._aliens
    
    def manage_bombing(self):
        time_delta = self._clock_manager.get_time() - self._last_bomb_time

        #stdio.writeln(time_delta)

        if time_delta >= self._bomb_interval:
            self._last_bomb_time = self._clock_manager.get_time()
            self.spawn_bomb()

        self.update_bombs()
            

    def spawn_bomb(self):
        aliens_alive = []

        for alien in self._aliens:
            if alien.dead == False:
                aliens_alive.append(alien)

        self._aliens = aliens_alive

        alien_random = self._aliens[random.randrange(0, self._alien_count)]

        bomb = bombs.Bomb(alien_random.x, alien_random.y)

        stdio.writeln("Bomb Spawned at : " + str(alien_random.x) + " " + str(alien_random.y))
        
        self._bombs.append(bomb)

    def update_bombs(self):

        for bomb in self._bombs[:]:
            if not bomb.alive:
                self._bombs.remove(bomb)
            else:
                bomb.update_position()
                player_hit = bomb.check_collision(self._player_ref.x)

                if player_hit:
                    self._gamemanager.player_hit()


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

"""