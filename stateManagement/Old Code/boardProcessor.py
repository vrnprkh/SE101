from boardState import BoardState
from tutorial import TutorialLevel

# Tutorial data is substates
class BoardProcessor:
    def __init__(self, state, tutorialData):
        self.boardState = BoardState(state)
        self.tutorial = TutorialLevel(tutorialData)
        self.sensorMap = None
        
        self.firstCoord = None
        self.secondCoord = None


    def getFirstCoord(self):
        return self.firstCoord

    # takes new sensors, updates self, and other states, SENSOR MAP ONLY 1S AND 0S
    def update(self, newSensorMap) -> int:
        '''
        Returns 0 if no display update
        Returns 1 if display update is needed
        Returns -1 for illegal move / error
        '''
        if not self.sensorMap: # if no old sensor data
            self.sensorMap = newSensorMap
            return 0
        
        newSensorValue = None
        changes = 0
        newCoord = None
        for i, layer in enumerate(newSensorMap):
            for j, e in enumerate(layer):
                if e != self.sensorMap[i][j]:
                    changes += 1
                    newCoord = (i, j)
                    newSensorValue = e

        

        #FAILS

       
        if changes == 0:
            return 0
        
         # more than one piece picked up
        if changes >= 2:
            return -1

        # more than 2 pieces in hand
        if (self.secondCoord) and (newSensorValue == 0):
            return -1
        
        # negative pieces in hand
        if (not self.firstCoord) and (newSensorValue == 1):
            return -1
        

        # HAND EDITING

        # pick up first piece
        if (not self.firstCoord) and (newSensorValue == 0):
            self.firstCoord = newCoord
            return 1
        
        # place first piece
        if self.firstCoord and (not self.secondCoord) and (newSensorValue == 1):
            # if same square
            if self.firstCoord == newCoord:
                self.firstCoord = None
                return 1
            # if new square
            else:
                move = (self.firstCoord, newCoord)
                if self.tutorial.checkLegal(move):
                    self.tutorial.makeMove(move)
                    self.boardState.updateState(move)
                    self.firstCoord = None
                    return 1
                else:
                    # TODO decide what to do with self.firstCoord
                    return -1
        
        # pick up second piece
        if (self.firstCoord) and (not self.secondCoord) and (newSensorValue == 0):
            self.secondCoord = newCoord
            return 0
        
        # capture
        if (self.firstCoord) and (self.secondCoord) and (newSensorValue == 1):
            if newCoord != self.secondCoord:
                return -1
            else:
                move = (self.firstCoord, self.secondCoord)
                if self.tutorial.checkLegal(move):
                    self.tutorial.makeMove(move)
                    self.boardState.updateState(move)
                    self.firstCoord = None
                    self.secondCoord = None
                    return 1
                else:
                    return -1
        



        


