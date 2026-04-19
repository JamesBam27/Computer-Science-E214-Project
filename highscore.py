import stdio #type: ignore
import os
import json

# OBSOLETE -> function handled by leaderboard.py

datafile_name = "data.txt"

class highScore:

    def update(self, newscore):
        # - Check if the newscore is greater than the current highscore
        # - If it is: return true, save new highscore
        # - If not: return false, do nothing

        currscore = self.get()

        if (newscore > currscore):
            self._set(newscore)
            return True
        else:
            return False

    def reset(newscore):
        with open(datafile_name, "w") as file:
            file.write("0")
            file.close()

    def get(self):
        # Return Current Highscore
        with open(datafile_name, "r") as file:
            content = file.read().split('\n')
            file.close()
            return int(content[0])
        
    def _set(self, newscore):
        # Set New Highscore
        oldscore = self.get()

        with open(datafile_name, "w") as file:
            file.write(str(newscore))
            file.close()
        
        return oldscore

    def __init__(self):
        # On init, we check if a data file exists
        # If it does not, we create one

        if (os.path.exists("./data.txt")):
            with open(datafile_name, "r") as file:
                content = file.read().split('\n')

                # If the stored data is not an integer, we cannot read a valid score
                # We try to get the first line as an int
                try: 
                    int(content[0]) 
                except:
                    file.close()
                    self.reset() # If it fails, we reset the file
                else:
                    file.close() # If it passes, we just close the file

        else:
            with open(datafile_name, "w") as file:
                stdio.writeln("Data file did not exist. Created.")
                file.write("0")
                file.close()

# TODO
# Currently updating the highscore in score.py.
# Need a better way of managing the score vs highscore.
# Possibly have scoreManager and highscoreManager as seperate objects.
# A bit unncessary but should work well here.
# Look at having a drawManager for drawing stuff like the currentScore
# when you work on this next.
