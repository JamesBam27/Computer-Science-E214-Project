import stddraw #type: ignore
import highscore

class ScoreBoard:#class to keep the players score

   def __init__(self):
       self.score = 0 #start with a socre of 0
       self.highscoreManager = highscore.highScore() #create a highscore manager object

   def update_score(self): #display the score in the top right hand coner
      stddraw.text(0.8,0.9,"Score: " + str(self.score)) 
      self.highscoreManager.update(self.score)
      
   def add_score(self): #add one to the score
      self.score  +=1
