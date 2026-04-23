import stddraw  #type: ignore
import stdaudio #type: ignore
import shooter, math, aliens, random, clock, bombs, constants, bunkers, leaderboard, threading

class EntityManager():

    def __init__(self):
        pass

    # Function To Spawn/Create aliens initially
    # Function To Update All Aliens               |       Main Update Function
    # - Basically to manage them during runtime,  |       
    #   call each of their updates                |
    # Function To Update All Bunkers              |
    