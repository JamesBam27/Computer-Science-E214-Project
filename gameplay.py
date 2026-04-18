import stddraw #type: ignore
import shooter
import math
import aliens
import main
import score
import random
import clock
import bombs
import gameover
class GamePlay:#class that defines the current instance of the game
    def __init__(self,vAlien,tally):
        self.vAlien = vAlien#speed of the alien
        self.tally = tally#score

    def playGame(self):
        gameOver = gameover.GameOver()#create a GameOver object
        timeShot = clock.Clock(0) #create a clock object to track the time between bullets shot
        time = clock.Clock(0) #create a clock object to track the game time
        x = 0.5#starting x position for shooter
        vx =0 #starting velocity of shooter
        a = math.pi/2 #starting angle of turret
        av =0 #starting angular velocity of turret
        bullet =[] #create an array of bullet objects as an empty array
        playerone = shooter.Shooter(x,vx,a,av,bullet,timeShot) #create a Shooter object with the initial values specified above
        xAlien = 0.1 #starting alien position
        yAlien = 0.9 #starting alien position
        vxAlien = self.vAlien  #set the initial alien velocity to that of the game instance
        aliensArr = [] #inintialise an empty array to store the aliens
        for i in range(12): #initialise 24 aliens in two rows
            aliensArr += [aliens.Aliens(xAlien + 0.05*(i+1),yAlien,vxAlien,bullet,False,0.7-0.05*i,0.05*i,playerone,self.tally,time,gameOver)]
        for i in range(12):
            aliensArr += [aliens.Aliens(xAlien+ 0.05*(i+1),yAlien - 0.05,vxAlien,bullet,False,0.7-0.05*i,0.05*i,playerone,self.tally,time,gameOver)]
        blown = False #**
        randomAlien = aliensArr[random.randrange(0,24)] #choose a random alien
        bomb = bombs.Bomb(randomAlien.x,randomAlien.y,playerone.x,0.15,gameOver) #create a bomb object 
        while True: #keep the game running
            time.updateTime() #add to the time for the game time
            timeShot.updateTime() #add to the time for the time between shots
            stddraw.clear(stddraw.GREEN) #set the canvas to green
            self.tally.updateScore()#update the score board
            b = bomb.bombUpdate()#update the bombs
            stddraw.text(0.1,0.9,"Lives: " +str(gameOver.lives)) #draw the lives i nthe top right hand corner
            f = True
            for i in aliensArr: # check if all the aliens are dead
                f = f and i.blown
            randomAlien = aliensArr[random.randrange(0,24)] # choose a random alien

            while (randomAlien.x ==1 and randomAlien.y == 1) and not f: #if that alien is dead keep trying to find an alive one
                randomAlien = aliensArr[random.randrange(0,24)] 
            if random.randrange(100) == 0 and bomb.y<0: #randomly drop a bomb from the random alien
             
               bomb.y =randomAlien.y
               bomb.x = randomAlien.x
            bomb.xShooter = playerone.x #update the x position of the shooter to the bomb 
            if playerone.shooter(): #if the shooter method that update the shooter returns true return "end"
                return "end"
            if f: #if all aliens are dead end the level by returning "endLevel"
                return "endLevel"
            for i in aliensArr: #check all of the aliens to see if they have killed the player
               #i.bullet = bullet
               if i.updateAlien() or b: #has a bomb or an alien killed the player
                   stddraw.show(1000)
                   return "gameover"
            stddraw.show(10)#display the game

def main():
    playGame()

if __name__ == "__main__": main()
