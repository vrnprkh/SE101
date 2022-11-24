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
        # print("hellooooooooooooooooooo")
        coord1 = move[0]
        coord2 = move[1]
        # self.state[coord1[0]][coord1[1]] = self.state[coord2[0]][coord2[1]]
        self.state[coord2[0]][coord2[1]] = self.state[coord1[0]][coord1[1]]
        self.state[coord1[0]][coord1[1]] = 0
         
    
    #@property
    #def state(self):
        #return self.state

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
        self.mustReset = False
        # self.l = [1, 2, 3, 4]


    def isLegal(self, move):
        #print("hello i am runnigh :)))))))))))))))))))")
        i = 0
        for e in self.tutorial.subStates[self.csubState][1][0]:
            if e[0] == move[0] and e[1] == move[1]:
                self.csubState = self.tutorial.subStates[self.csubState][1][1][i]
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

        if self.mustReset:
            if not self.resetBoard(newSensorMap):
                return -1
        
        newSensorValue = None
        changes = 0
        newCoord = None
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
        
        # if (self.firstCoord == None) and (newSensorValue == 1):
        #     print("e3")
        #     return -1
        
        #print("new s val " + str(newSensorValue))
        #print("new coord " + str(newCoord))
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
            print("bawls")
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
                #n = self.tutorial.checkLegal(move)
                #print("legality:")
                #print(n)
                #if (n):
                # print("moves idk")
                print(self.tutorial.subStates[self.csubState])
                #if self.tutorial.checkLegal(move):
                
                # if move in self.tutorial.subStates[self.subState][1]:
                #     index = self.tutorial.subStates[self.subState][]
                #     self.subState = self.tutorial.subStates[self.subState][1]
                
                legal = self.isLegal(move)
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
                self.mustReset = True
                print("e4")
                return -1
            else:
                move = (self.firstCoord, self.secondCoord)
                self.boardState.updateState(move)
                return 2
                # if self.tutorial.checkLegal(move):
                #     self.tutorial.makeMove(move)
                #     self.boardState.updateState(move)
                #     self.firstCoord = None
                #     self.secondCoord = None
                #     return 2
                # else:
                #     print("e5")
                #     return -1

    
    def resetBoard(self, newSensorMap) -> bool:
        for e in range(len(self.sensorMap)):
            for j in range(len(self.sensorMap)):
                if self.sensorMap[e][j] != newSensorMap[e][j]:
                    return False
        
        self.mustReset = False
        return True
