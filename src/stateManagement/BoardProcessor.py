from . import BoardState, TutorialLevel
from . import illegalMove

import functools

class BoardProcessor:
    def __init__(self, state, tutorialData = None):
        self.boardState = BoardState.BoardState(state)
        self.tutorial = TutorialLevel.TutorialLevel(tutorialData) if not tutorialData == None else None
        self.sensorMap = None
        
        self.firstCoord = None
        self.secondCoord = None
        self.csubState = 0
        # self.l = [1, 2, 3, 4]

    def onePieceLeft(self) -> bool:
        numPieces = []
        for row in self.boardState:
            for col in row:
                if self.boardState[row][col] > 0:
                    numPieces.append(self.boardState[row][col])

        numPawns = functools.reduce(lambda x, y: x + y if (y == 1 or y == 7) else y, numPieces, 0)
        numPieces = len(numPieces) - numPawns

        return numPieces <= 0

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
        # piece = None
        print("self:")
        print(self.sensorMap)
        print("new:")
        print(newSensorMap)
        print("board state")
        print(self.boardState.state)
        for i, layer in enumerate(newSensorMap):
            for j, e in enumerate(layer):
                if e != self.sensorMap[i][j]:
                    changes += 1
                    newCoord = (i, j)
                    newSensorValue = e

        #FAILS

        print("changes: " + str(changes))
        print("new val: " + str(newSensorValue))

        # no changes to board state
        if changes == 0:
            return 0
        
         # more than one piece picked up 
        if changes >= 2:
            print("error 1")
            return -1
        
        # more than 2 pieces in hand
        if (type(self.secondCoord) is tuple) and (newSensorValue == 0):
            print("e2")
            return -1
        
        # negative pieces in hand FIXME
        # HAND EDITING

        # pick up first piece
        if (self.firstCoord == None) and (newSensorValue == 0):

            self.firstCoord = newCoord
            self.sensorMap = newSensorMap
            print("picked up")
            return 1
        
        # place first piece
        if (type(self.firstCoord) is tuple) and (self.secondCoord == None) and (newSensorValue == 1):
            # if same square
            # print("bawls")
            if self.firstCoord == newCoord:
                self.firstCoord = None
                #print("same square put")
                self.sensorMap = newSensorMap
                return 1
                
            # if new square
            else:
                move = (self.firstCoord, newCoord)
                # print("move")
                print(move)

                #print(self.tutorial.subStates[self.csubState])
                
                legal = illegalMove.LegalMoveProcessor.isLegal(self, move, self.boardState.state[self.firstCoord[0]][self.firstCoord[1]]) #XXX
                print(legal)
                if legal:
                    #self.tutorial.makeMove(move)
                    print("old state:")
                    print(self.boardState.state)
                    self.boardState.updateState(move)
                    print("new state:")
                    print(self.boardState.state)
                    self.firstCoord = None
                    self.sensorMap = newSensorMap
                    return 1
                else:
                    # TODO decide what to do with self.firstCoord
                    print("e6")
                    return -1
        
        
        # pick up second piece
        if type(self.firstCoord) is tuple and (self.secondCoord == None) and (newSensorValue == 0):
            # print("hello i am here!!!!!!!!!!!!!!!!!!!!!!!")
            self.secondCoord = newCoord
            self.sensorMap = newSensorMap 
            return 0
        
        # capture
        if type(self.firstCoord) is tuple and type(self.secondCoord) is tuple and (newSensorValue == 1): #XXX
            if newCoord != self.secondCoord:
                print("e4")
                return -1
            else:
                move = (self.firstCoord, self.secondCoord)
                self.boardState.updateState(move)
                if self.onePieceLeft(): #If one piece is left, we want the main function to stop execution
                    return 3
                else: #if more than one piece left, we want the main function to stop execution
                    return 2
