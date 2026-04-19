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

# TODO Make this readable and convert to GameManager
# The strat might be to create a new GameManager class,
# and then just use this file as a framework to build
# the GameManager off of. Feel it out. 

import constants
import bunkers
class GameManager: #class that defines the current instance of the game
    def __init__(self,vAlien,tally):
        self.vAlien = vAlien#speed of the alien
        self.tally = tally#score

    def play_game(self):

        # -- INITIALISE

        game_over = gameover.GameOver()#create a GameOver object 
        time_shot = clock.Clock(0) #create a clock object to track the time between bullets shot
        time = clock.Clock(0) #create a clock object to track the game time

        x = 0.5#starting x position for shooter
        vx =0 #starting velocity of shooter
        a = math.pi/2 #starting angle of turret
        av =0 #starting angular velocity of turret

        bullet =[] #create an array of bullet objects as an empty array
        player_one = shooter.Shooter(x,vx,a,av,bullet,time_shot) #create a Shooter object with the initial values specified above
        xAlien = 0.1 #starting alien position
        yAlien = 0.9 #starting alien position
        vxAlien = self.vAlien  #set the initial alien velocity to that of the game instance
        aliens_arr = [] #inintialise an empty array to store the aliens

        for i in range(12): #initialise 24 aliens in two rows
            aliens_arr += [aliens.Aliens(xAlien + constants.ALIEN_HITBOX*(i+1),yAlien,vxAlien,bullet,False,0.55-constants.ALIEN_HITBOX*i,constants.ALIEN_HITBOX*i,player_one,self.tally,time,game_over)]
        for i in range(12):
            aliens_arr += [aliens.Aliens(xAlien+ constants.ALIEN_HITBOX*(i+1),yAlien - constants.ALIEN_HITBOX,vxAlien,bullet,False,0.55-constants.ALIEN_HITBOX*i,constants.ALIEN_HITBOX*i,player_one,self.tally,time,game_over)]
        
        blown = False #**
        random_alien = aliens_arr[random.randrange(0,24)] #choose a random alien
        bomb = bombs.Bomb(random_alien.x,random_alien.y,player_one.x,constants.SHOOTER_Y,game_over) #create a bomb object 
        bunker1= bunkers.Bunker(0.2,0.4,3,bullet,bomb,aliens_arr)
        bunker2 = bunkers.Bunker(0.8,0.4,3,bullet,bomb,aliens_arr)

        # Manage The Game Loop, Run until we reach an end condition
        
        while True:

            time.updateTime() #add to the time for the game time
            time_shot.updateTime() #add to the time for the time between shots
            stddraw.clear(stddraw.GREEN) #set the canvas to green
            bunker1.update_bunker()
            bunker2.update_bunker()

            self.tally.update_score()#update the score board
            bomb_hit = bomb.bomb_update()#update the bombs
            stddraw.text(0.1,0.9,"Lives: " +str(game_over.lives)) #draw the lives i nthe top right hand corner

            all_aliens_destroyed = True
            for i in aliens_arr: # check if all the aliens are dead
                all_aliens_destroyed = all_aliens_destroyed and i.blown
            random_alien = aliens_arr[random.randrange(0,24)] # choose a random alien

            while (random_alien.x ==1 and random_alien.y == 1) and not all_aliens_destroyed: #if that alien is dead keep trying to find an alive one
                random_alien = aliens_arr[random.randrange(0,24)] 
            if random.randrange(100) == 0 and bomb.y<0: #randomly drop a bomb from the random alien
               bomb.y =random_alien.y
               bomb.x = random_alien.x
            bomb.x_shooter = player_one.x #update the x position of the shooter to the bomb 

            # Update Game State

            if player_one.update_shooter(): #if the shooter method that update the shooter returns true return "end"
                return "game_quit"
            if all_aliens_destroyed: #if all aliens are dead end the level by returning "endLevel"
                return "level_end" 
            if bomb_hit:
                if game_over.update_game_over():
                    game_over.end_game()
                    stddraw.show(1000)
                    return "game_over"
            for i in aliens_arr: #check all of the aliens to see if they have killed the player
               if i.update_alien(): #has an alien killed the player
                   if game_over.update_game_over():
                       game_over.end_game()
                       stddraw.show(1000)
                       return "game_over"
            
            

            stddraw.show(10)#display the game


    def run_loop():
        pass
