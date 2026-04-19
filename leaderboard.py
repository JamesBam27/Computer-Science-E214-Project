import stdio #type: ignore
import os
import json

datafile_name = "data.json"

class LeaderBoardManager():

    # Should technically make this class a Singleton but I don't think
    # its worth complicating it. We just must not create more than one
    # instance of this class.

    def __init__(self):

        if os.path.exists(datafile_name) and os.path.getsize(datafile_name) > 0:
            with open(datafile_name, "r") as file:
                content = json.load(file)
                file.close()

        else:
            with open(datafile_name, "w") as file:
                stdio.writeln("Data file did not exist or was empty. Created and populated.")
                json.dump({str(i): {'name': f'Player {i}', 'score': 0} for i in range(1, 5)}, file)
                file.close()