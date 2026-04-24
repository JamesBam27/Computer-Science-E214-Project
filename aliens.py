import stddraw  # type: ignore
from picture import Picture  # type: ignore
import constants


class Aliens:  # implemented by James Bam
    def __init__(self, x, y, velocity, bullet, dead, right_bound, left_bound, score_board):
        self.x = x  # set the x position
        self.y = y  # set the y position
        self.velocity = velocity  # set the x velocity
        self.bullet = bullet  # set the array of bullets
        self.dead = dead  # set if the aliens is dead or alive
        self.health = 1
        self.right_bound = right_bound  # set the right boundary for the alien
        self.left_bound = left_bound  # set the left boundary for the alien
        # SHOOTER WAS HERE
        self._score_board = score_board  # set the score
        self.img = Picture("./Assets/img/Alien.png")

    def update_alien(self):

        # if the alien reaches its boundary turn it around and move it down
        

        """
        # check all the bullets
        for i in self.bullet:
            # if bullet too close to the alien kill the alien
            if (
                abs(self.x - i.x) < constants.ALIEN_HITBOX
                and abs(self.y - i.y) < constants.ALIEN_HITBOX
            ):
                # To remove an alien, we move it outside of the screen space.
                i.x = -1
                i.y = -1
                self.kill_alien()
                self.tally.increment()

            """

    def update_position(self):

        if not self.left_bound <= self.x <= constants.RIGHT_BOUND - self.right_bound:
            self.velocity = -self.velocity
            self.y = self.y - constants.ALIEN_ADVANCE_DISTANCE

        self.x = self.x + self.velocity  # move the alien in the x direction

        stddraw.picture(self.img, self.x, self.y)

    def check_collision(self, player_position_x):

        bottom_bound_crossed = self.y < constants.BOTTOM_BOUND
        player_hit = abs(player_position_x - self.x) < constants.ALIEN_HITBOX and abs(constants.SHOOTER_Y - self.y) < constants.ALIEN_HITBOX

        if bottom_bound_crossed or player_hit:
            self.x = 2
            self.dead = True

            return player_hit
        
    def check_bullets(self, bullets):

        for bullet in bullets:

            bullet_hit = (abs(self.x - bullet.x) < constants.ALIEN_HITBOX) and (abs(self.y - bullet.y) < constants.ALIEN_HITBOX)

            if bullet_hit and not bullet._hit:
                bullet.destroy_bullet()
                
                self.health -= 1

    def check_health(self, game_manager):

        if self.health <= 0:
            self.dead = True
            game_manager.alien_destroyed()


# Inherits from the alien class:
# same as normal aliens except the boss has multiple lives and
# has to be hit a certain amout of times to die.
class Boss(Aliens):
    def __init__(self, x, y, velocity, bullet, dead, health, right_bound, left_bound, score_board):
        super().__init__(
            self, x, y, velocity, bullet, dead, right_bound, left_bound, score_board
        )  # call the parents constructor
        self.change_img()
        self.health = health

    # have a diffrent picture
    def change_img(self):
        self.img = Picture("./Assets/img/Alien2.png")
