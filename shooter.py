import stddraw  # type: ignore
import stdaudio  # type: ignore
from picture import Picture  # type: ignore
import math
import threading
import constants


# Implemented by Robert Van Woudenberg
class Bullet:  # class to represent a bullet shot by the player

    def __init__(self, x, y, angle, v):
        self.x = x  # set the x position
        self.y = y  # set the y position
        self.angle = angle  # set the angle it should travel at
        self.v = v  # set the velocity

    def kill_bullet(self):  # put the bullet off the screen
        self.y = -1
        self.x = -1

    def shoot(self):  # update the position of the bullet and display it on the screen
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

    def __init__(self, x, vx, a, av, bullet, time):
        self.x = x  # set the x position
        self.vx = vx  # set the x velocity
        self.angle_v = av  # set the angular velocity
        self.angle = a  # set the angle of the turret
        self.bullet = bullet  # set the array of bullets currently on the screen
        self.time = (
            time  # set the Clock object of the timeComputer-Science-E214-Project
        )
        self.ship = Picture(
            "./Assets/img/ship2.png"
        )  # create the picture object of the shooter
        self.vx_positive = 0.005  # set the positive x velocity
        self.vx_negative = -0.005  # set the negative x velocity
        self.angle_v_positive = 0.01  # set the positive angular velocity of the turret
        self.angle_v_negative = -0.01  # set the negative angular velocity of the turret

    def update_shooter(
        self,
    ):  # method that updates the infomation on the shooter and performs all logic of the shooter
        if stddraw.hasNextKeyTyped():  # check if a key has been typed
            key = stddraw.nextKeyTyped()
            if key == "d":
                self.vx = self.vx_positive  # move right
            else:
                if key == "a":
                    self.vx = self.vx_negative  # move left
                else:
                    if key == "s":
                        self.vx = 0  # stop
                    else:
                        if key == "x":
                            return True  # close the program
                        else:
                            if key == " " and (
                                self.time.time > 20
                            ):  # shoot the bullet only after a certain amount of time from the last one
                                threading.Thread(
                                    target=play_sound
                                ).start()  # play the bullet sound
                                self.time.time = 0  # reset the shot timer
                                self.bullet += [
                                    Bullet(
                                        self.x, 0.15, self.angle, constants.BULLET_SPEED
                                    )
                                ]  # add a bullet to the bullet array
                            else:
                                if key == "e":
                                    self.angle_v = (
                                        self.angle_v_negative
                                    )  # move the turret anticlockwise
                                else:
                                    if key == "q":
                                        self.angle_v = (
                                            self.angle_v_positive
                                        )  # move the turret clockwise
                                    else:
                                        if key == "w":
                                            self.angle_v = 0  # stop the turret

        self.angle = self.angle + self.angle_v  # move the turret
        if (
            not 0 < self.angle < math.pi
        ):  # if the turret has an angle less than zero and greater than 90 degrees turn the turret around
            self.angle_v = -self.angle_v
        curser(self.x, constants.SHOOTER_Y, self.angle)  # update and draw the curser
        for i in self.bullet[:]:  # check all the bullets
            if not (
                constants.LEFT_BOUND < i.x < constants.RIGHT_BOUND
                and constants.BOTTOM_BOUND < i.y < constants.TOP_BOUND
            ):  # if they are off the screen remove the alien for the list
                self.bullet.remove(i)
            else:
                i.shoot()  # update the position and draw all the bullets

        if (
            self.x < constants.LEFT_BOUND or self.x > constants.RIGHT_BOUND
        ):  # if the shooter reaches the end of the screen turn around
            self.vx = -self.vx
        self.x = self.x + self.vx  # move the shooter
        stddraw.picture(self.ship, self.x, constants.SHOOTER_Y)  # draw the shooter
