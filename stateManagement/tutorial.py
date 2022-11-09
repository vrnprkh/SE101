class TutorialLevel:
    #Substates is a list, of substates, each having a list of legal moves
    def __init__(self, subStates):        
        self.subStates = subStates
        self.currentSubstate = 0
    
    def checkLegal(self, move):
        if move in self.subStates[self.current][1]:
            return True
    
    def makeMove(self, move):
        if move in self.subStates[self.current][1]:
            self.current = self.subStates[self.current][1][2]
        
    
    