import stddraw #type: ignore
import leaderboard

def setScale(x=1,y=1):
    stddraw.setXscale(0,x)
    stddraw.setYscale(0,y)

def displayTitleScreen(): #Implemented By Robert Van Woudenberg
    
    # Inititalise and Draw Title
    stddraw.clear(stddraw.BLACK)	
    setScale(1,1)
    stddraw.setFontSize(50)
    stddraw.setPenColor(stddraw.GREEN)
    stddraw.text(0.5,0.9,"ALIEN INVADERS")

    leaderboardManager = leaderboard.LeaderBoardManager()

    # Draw Leaderboard and Player Scores
    leaderboard_content = leaderboardManager.get_data()

    stddraw.setFontSize(18)
    stddraw.text(0.8,0.8,"LEADERBOARD:")

    stddraw.setFontSize(16)
    for i in leaderboard_content:
        stddraw.text(0.8, 0.79 - (int(i) * 0.025), f"Player {i} --- {leaderboard_content[i]['score']}")

    # Draw Heading
    stddraw.setFontSize(35)
    stddraw.text(0.5,0.7,"Instructions")

    # Draw Instructions
    stddraw.setFontSize(18)
    stddraw.text(0.5,0.6,"[A] move left,[S] stop, [D] move right")
    stddraw.text(0.5,0.5,"[Q] Rotate left, [W] stop rotate, [E] rotate right")
    stddraw.text(0.5,0.4,"[Space] to shoot")
    stddraw.text(0.5,0.2,"[X] to quit")
    stddraw.text(0.5,0.25,"TO START, TYPE 1, 2, 3 or 4 TO SELECT A SAVE SLOT")

