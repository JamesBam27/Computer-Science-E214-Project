import stddraw  # type: ignore
import stdaudio  # type: ignore
from picture import Picture  # type: ignore
import math
import threading
import constants

# Initial Player Turret Values
initial_turret_angle = math.pi / 2
initial_turret_angular_vel = 0

# Speed at which Player Moves
player_velocity = 0.005

# Implemented by Robert Van Woudenberg
class Bullet:  # class to represent a bullet shot by the player

    def __init__(self, x, y, angle, v):
        self.x = x  # set the x position
        self.y = y  # set the y position
        self.angle = angle  # set the angle it should travel at
        self.v = v  # set the velocity
        self._hit = False

    def destroy_bullet(self):
        self._hit = True

    def update_position(self):  # update the position of the bullet and display it on the screen
        vx = math.cos(self.angle) * self.v
        vy = math.sin(self.angle) * self.v
        self.x = self.x + vx
        self.y = self.y + vy
        stddraw.point(self.x, self.y)


def curser(x, y, angle):  # function to update and draw the turret
    y = y + 0.015
    stddraw.setPenColor(stddraw.ORANGE)
    stddraw.line(x, y, x + math.cos(angle) / 25, y + math.sin(angle) / 25)
    stddraw.setPenColor(stddraw.WHITE)


def play_sound():  # function that plays the bullet sound
    stdaudio.playFile("./Assets/audio/Lazer")


class Shooter:  # class that defines the player

    def __init__(self, x, vx, bullet, shot_clock):
        self.x = x  # set the x position
        self.velocity = vx  # set the x velocity
        self._turret_angular_vel = initial_turret_angular_vel  # set the angular velocity
        self._turret_angle = initial_turret_angle  # set the angle of the turret
        self._bullets = bullet  # set the array of bullets currently on the screen
        self._clock_shooter = shot_clock  # set the Clock object of the time
        self.img = Picture("./Assets/img/ship2.png")  # create the picture object of the shooter
        self.vx_positive = 0.005  # set the positive x velocity
        self.vx_negative = -0.005  # set the negative x velocity
        self._angular_velocity = 0.01  # set the positive angular velocity of the turret

    def update_shooter(self, entity_manager):
        
        if stddraw.hasNextKeyTyped():  # check if a key has been typed
            key = stddraw.nextKeyTyped()

            if key == "d":
                self.velocity = player_velocity  # move right
            elif key == "a":
                self.velocity = -player_velocity  # move left
            elif key == "s":
                self.velocity = 0  # stop
            elif key == "x":
                return True  # close the program
            elif key == " " and (self._clock_shooter.time > 20):  # shoot the bullet only after a certain amount of time from the last one
                self.spawn_bullet(entity_manager)
            elif key == "e":
                self._turret_angular_vel = self._angular_velocity # move the turret anticlockwise
            elif key == "q":
                self._turret_angular_vel = -self._angular_velocity
            elif key == "w":
                self._turret_angular_vel = 0  # stop the turret

        self._turret_angle = self._turret_angle + self._turret_angular_vel  # move the turret

        if not 0 < self._turret_angle < math.pi:  # if the turret has an angle less than zero and greater than 90 degrees turn the turret around
            self._turret_angular_vel = -self._turret_angular_vel

        curser(self.x, constants.SHOOTER_Y, self._turret_angle)  # update and draw the curser
        
        out_of_bounds = self.x < constants.LEFT_BOUND or self.x > constants.RIGHT_BOUND
        
        # If the Shooter reaches the end of the screen turn around
        if out_of_bounds:  
            self.velocity = -self.velocity
        self.x = self.x + self.velocity  # move the shooter
        stddraw.picture(self.img, self.x, constants.SHOOTER_Y)  # draw the shooter

    def spawn_bullet(self, entity_manager):
        threading.Thread(target=play_sound).start()  # play the bullet sound
        self._clock_shooter.time = 0  # reset the shot timer

        # Create Bullet Instance
        bullet = Bullet(self.x, 0.15, self._turret_angle, constants.BULLET_SPEED)

        entity_manager.track_bullet(bullet)