import stddraw #type: ignore
import highscore

class scoreBoard:

   def __init__(self, init_score):
       self.score = init_score
       self.highscoreManager = highscore.highScore()

   def updateScore(self):
      stddraw.text(0.8,0.9,"Score: " + str(self.score))
      self.highscoreManager.update(self.score)
      
   def addScore(self):
      self.score  +=1
