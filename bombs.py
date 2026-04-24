import stddraw  # type: ignore
import stdaudio  # type: ignore
from picture import Picture  # type: ignore
import clock
import random
import threading
import constants

# Bombs are spawned by aliens. They fall down
# and deal 1 life worth of damage to the player
# if one hits them.


class Bomb:  # Implemented by James Bam

    def __init__(self, x, y):
        self.y = y  # y coord
        self.x = x  # x coord
        self.alive = True
        self.img = Picture("./Assets/img/bomb2.png")  # set the picture of the bomb
        
    def update_position(self):
        
        # Update Y Position
        self.y = self.y + constants.BOMB_SPEED 

        # Draw Bomb
        stddraw.picture(self.img, self.x, self.y)

    def check_collision(self, player_position_x):

        # Check if Bomb Intersects Player Hitbox, Check if Bomb has Crossed The Lower Bound
        player_collision = abs(player_position_x - self.x) < constants.BOMB_HITBOX and abs(constants.SHOOTER_Y - self.y) < constants.BOMB_HITBOX
        bottom_bound_crossed = self.y < constants.BOTTOM_BOUND

        # If the Bomb has hit a Player or a Boundary, we Remove it from play
        # and flag it as dead
        if player_collision or bottom_bound_crossed:
            self.y = 2
            self.alive = False

            # We tell the GameManager that the Player
            # was hit by a Bomb
            if player_collision:
                return True
            else:
                return False

