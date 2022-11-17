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

class BoardState:
    def __init__(self, state):
        self.state = state
    # move from (y1, x1) -> (y2, x2)
    # in the form ((y1, x1), (y2, x2))
    def updateState(self, move):
        coord1 = move[0]
        coord2 = move[1]
        self.state[coord1[0]][coord1[1]] = self.state[coord2[0]][coord2[1]] 
    
    @property
    def state(self):
        return self.state

# Tutorial data is substates
class BoardProcessor:
    def __init__(self, state, tutorialData):
        self.boardState = BoardState(state)
        self.tutorial = TutorialLevel(tutorialData)
        # self.substates = tutorialData
        self.sensorMap = None
        
        self.firstCoord = None
        self.secondCoord = None
        self.csubState = 0
        # self.l = [1, 2, 3, 4]

    @property
    def csubstate(self):
        return self.csubState
    
    @property
    def firstCoord(self):
        return self.firstCoord
    
    @property
    def boardState(self):
        return self.boardState

    def isLegal(self, move):
        #print("hello i am runnigh :)))))))))))))))))))")
        i = 0
        for e in self.tutorial.subStates[self.csubState][1][0]:
            if e[0] == move[0] and e[1] == move[1]:
                self.csubState = self.substates[self.csubState][1][1][i]
                print(i)
                print("csub " + str(self.csubState))
                return True
            i += 1
            
        return False

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
        print("self:")
        print(self.sensorMap)
        print("new:")
        print(newSensorMap)
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
        
         # more than one piece picked up FIXME
        if changes >= 2:
            print("error 1")
            return -1
        
        # more than 2 pieces in hand
        if (self.secondCoord) and (newSensorValue == 0):
            print("e2")
            return -1
        
        # negative pieces in hand FIXME
        if (not self.firstCoord) and (newSensorValue == 1):
            print("e3")
            return -1
        
        #print("new s val " + str(newSensorValue))
        #print("new coord " + str(newCoord))
        # HAND EDITING

        # pick up first piece
        if (not self.firstCoord) and (newSensorValue == 0):
        # if (newSensorValue == 0):
            self.firstCoord = newCoord
            self.sensorMap = newSensorMap
            #print("picked up")
            return 1
        
        # place first piece
        if self.firstCoord and (not self.secondCoord) and (newSensorValue == 1):
            # if same square
            if self.firstCoord == newCoord:
                self.firstCoord = None
                #print("same square put")
                self.sensorMap = newSensorMap
                return 1
                
            # if new square
            else:
                move = (self.firstCoord, newCoord)
                print("move")
                print(move)
                #n = self.tutorial.checkLegal(move)
                #print("legality:")
                #print(n)
                #if (n):
                print("moves idk")
                print(self.tutorial.subStates[self.csubState])
                #if self.tutorial.checkLegal(move):
                
                # if move in self.tutorial.subStates[self.subState][1]:
                #     index = self.tutorial.subStates[self.subState][]
                #     self.subState = self.tutorial.subStates[self.subState][1]
                
                legal = self.isLegal(move)
                print(legal)
                if legal:
                    #self.tutorial.makeMove(move)
                    print(self.boardState.state)
                    self.boardState.updateState(move)
                    print(self.boardState.state)
                    self.firstCoord = None
                    self.sensorMap = newSensorMap
                    return 1
                else:
                    # TODO decide what to do with self.firstCoord
                    print("e6")
                    return -1
        
        
        # pick up second piece
        if (self.firstCoord) and (not self.secondCoord) and (newSensorValue == 0):
            self.secondCoord = newCoord
            return 0
        
        # capture
        if (self.firstCoord) and (self.secondCoord) and (newSensorValue == 1):
            if newCoord != self.secondCoord:
                print("e4")
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
                    print("e5")
                    return -1
        