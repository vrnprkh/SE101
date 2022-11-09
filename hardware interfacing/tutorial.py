class tutorialLevel:
    #Substates is a list, of substates, each having a list of legal moves
    def __init__(self, subStates, initial = 0, winning = -1):
        
        self.subStates = subStates
        self.initial = initial
        self.currentSubstate = initial
        self.winning = winning