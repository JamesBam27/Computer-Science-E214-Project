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

    def __init__(self, y, x, shooter_x):
        self.y = y  # set the y coordinate
        self.x = x  # set the x coordinate
        self.shooter_x = shooter_x
        self.bomb = Picture("./Assets/img/bomb2.png")  # set the picture of the bomb

    def kill_bomb(self):
        self.y = -1
    def set_shooter_x(self,x):
        self.shooter_x = x

    def bomb_update(self):  # move the bomb and check if it has hit a player
        velocity_y = -0.01  # set the velocity
        self.y = self.y + velocity_y  # move it down
        stddraw.picture(self.bomb, self.x, self.y)  # draw the bomb
        if (
            abs(self.shooter_x - self.x) < constants.BOMB_HITBOX
            and abs(constants.SHOOTER_Y - self.y) < constants.BOMB_HITBOX
        ):  # check if it got too close the the shooter and if it did take a life
            self.y = -1
            return True
        return False
