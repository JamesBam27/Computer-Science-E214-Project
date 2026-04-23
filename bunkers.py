import stddraw  # type: ignore
import aliens
import bombs
import shooter
import constants
from picture import Picture  # type: ignore


class Bunker:  # implemented by James Bam

    def __init__(self, x, y, health, bullet, bomb, alien):
        self.x = x
        self.y = y
        self.health = health
        self.bullet = bullet
        self.bomb = bomb
        self.alien = alien
        self.bunker = Picture("./Assets/img/bunker.png")

    def update_bunker(self):
        #Check if a bullet, bomb or alien has hit the bunker. Kill the entity and if heath <=0 kill the bunker
        if self.health > 0:
            for i in self.bullet:
                if abs(i.x - self.x) <= constants.BUNKER_HITBOX and abs(i.y - self.y) <= constants.BUNKER_HITBOX:
                    self.health -= 1
                    i.kill_bullet()

            if abs(self.bomb.x - self.x) <= constants.BUNKER_HITBOX and abs(self.bomb.y - self.y) <= constants.BUNKER_HITBOX:
                self.health -= 1
                self.bomb.kill_bomb()

            for i in self.alien:
                if abs(i.x - self.x) <= constants.BUNKER_HITBOX and abs(i.y - self.y) <= constants.BUNKER_HITBOX:
                    self.health -= 1
                    i.kill_alien()

            stddraw.picture(self.bunker, self.x, self.y)
