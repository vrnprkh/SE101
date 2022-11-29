class TutorialLevel:
    #Substates is a list, of substates, each having a list of legal moves
    def __init__(self, subStates):        
        self.subStates = subStates
        self.current = 0
        self.sensorMap = None
    
    def checkLegal(self, move):
        if move in self.subStates[self.current][1]:
            return True
    
    def makeMove(self, move):
        # TODO TEST ME !
        if move in self.subStates[self.current][1][0]:
            for e in self.subStates[self.current][1]:
                if e[:1] == move:
                    self.current = e[2]