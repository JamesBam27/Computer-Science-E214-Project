import stddraw #type: ignore
import leaderboard

class ScoreBoard:#class to keep the players score

   def __init__(self):
       self.score = 0 #start with a score of 0
       self.leaderBoardManager = leaderboard.LeaderBoardManager()

   # Give The Current Score to the Leaderboard Manager and Display It
   # On Screen
   def update_score(self, player):
      stddraw.text(0.8,0.9,"Score: " + str(self.score)) 
      self.leaderBoardManager.update(self.score, player)
      
   def increment(self): #add one to the score
      self.score  +=1
