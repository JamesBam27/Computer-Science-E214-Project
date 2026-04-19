#class to represent time

class Clock:
    
    # Set Initial Time
    def __init__(self,time):
        self.time = time

    # Add 1 to time value
    def updateTime(self):
        self.time +=1	
