class BoardState:
    def __init__(self, state):
        self.state = state
    # move from (y1, x1) -> (y2, x2)
    # in the form ((y1, x1), (y2, x2))
    def updateState(self, move):
        coord1 = move[0]
        coord2 = move[1]
        self.state[coord1[0]][coord1[1]] = self.state[coord2[0]][coord2[1]] 
    
    @getattr
    def getState(self):
        return self.state

    
    

