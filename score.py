import stddraw
class scoreBoard:
   def __init__(self):
       self.score = 0
   def updateScore(self):
      stddraw.text(0.8,0.9,"Score: " + str(self.score))
   def addScore(self):
      self.score  +=1
