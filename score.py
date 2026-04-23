import stddraw  # type: ignore
import leaderboard

# Manages the players score and hands it off to the
# LeaderBoard Manager


class ScoreBoard:  # Implemented By James Bam

    def __init__(self):
        self.score = 0
        self.leaderBoardManager = leaderboard.LeaderBoardManager()

    # Give The Current Score to the Leaderboard Manager and Display It
    # On Screen
    def update_score(self, player):
        stddraw.text(0.8, 0.9, "Score: " + str(self.score))
        self.leaderBoardManager.update(self.score, player)

    def increment(self):
        self.score += 1
