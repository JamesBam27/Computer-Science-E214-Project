import stdio #type: ignore
import os
import json

datafile_name = "data.json"

class LeaderBoardManager():

    # Should technically make this class a Singleton but I don't think
    # its worth complicating it. We just must not create more than one
    # instance of this class.

    # The Player will choose between 4 "save slots" when they begin the game.
    # By Default, save 1 will be selected. 


    # Update The Current Highscore of the Selected Player, We Handle The Logic Ourselves
    # Return True if the newscore is a Highscore, Return False if not.
    def update(self, newscore, player):
        
        current = self.get_score(player)

        if newscore > current:
            self._set(newscore, player)
            return True
        else:
            return False

    # Return The Stored Score of the Selected Player
    def get_score(self, player):
        return self.get_data()[str(player)]['score']
    
    # Return all Leaderboard Data
    def get_data(self):
        with open(datafile_name, "r") as file:
            content = json.load(file)
            return content
    
    # Write a new Score Value for the Selected Player to the Data File
    def _set(self, newscore, player):
        
        old = self.get_score(player)
        
        content = self.get_data()
        content[str(player)]['score'] = newscore

        with open(datafile_name, "w") as file:
            json.dump(content, file)
        
        return self.get_score(player)
    
    # Reset all Saved Scores to Zero
    def reset(self):

        content = self.get_data()

        for i in content:
            self._set(0, int(i))

    # Initalise the LeaderBoard Manager. Check whether our Data File exists, Create
    # and Populate it if not.
    def __init__(self):

        if os.path.exists(datafile_name) and os.path.getsize(datafile_name) > 0:
            with open(datafile_name, "r") as file:
                content = json.load(file)

        else:
            with open(datafile_name, "w") as file:
                stdio.writeln("Data file did not exist or was empty. Created and populated.")
                json.dump({str(i): {'name': f'Player {i}', 'score': 0} for i in range(1, 5)}, file)