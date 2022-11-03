
class Board:
    def __init__(self, state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]):
        # state is 4x4 grid of pieces by default
        self.state = state

        #sensor map is 4x4 grid of 0s and 1s, which is the current sensor state.
        self.sensorMap = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        for i, layer in enumerate(state):
            for j, e in enumerate(layer):
                if e != 0:
                    self.sensorMap[i][j] == 1
        self.firstCoord = None
        self.secondCoord = None

    #note a move is nested tuple ((y1, x1), (y1, x1))
    def checkValidMove(self, move):
        return True
    

    # moves without checking legality
    def rawMove(self, move):
        self.state[move[1][0]][move[1][1]] = self.state[move[0][0]][move[0][1]]
        self.state[move[0][0]][move[0][1]] = 0


    # returns 1 if successful, 0 if likely user error, - 1 if likely code error?, -2 if somehow nothing runs?

    # takes the new sensor map, if it is different, update the board.
    # note that self.state is not updated until a move is completed.
    def processSensors(self, newSensorMap):
        count = 0
        for i, layer in enumerate(newSensorMap):
            for j, e in enumerate(layer):
                if self.state[i][j] != e:
                    count += 1
                    y = i
                    x = j

        # no update
        if count == 0:
            return 1
        newSensor = newSensorMap[y][x]
        
        # fails
        if count >= 2: # more than 1 update
            return 0
        if (self.secondCoord != None) and (newSensor == 1): # 
            return 0
        if (self.firstCoord == None) and (newSensor == 1):
            return -1
        


        # pick up first piece
        if (self.firstCoord == None) and (newSensor == 0):
            self.firstCoord = (y, x)
            self.firstPiece = self.state[y][x]
            return 1
        # place first piece on own square
        if (self.firstCoord != None) and (newSensor == 1) and (self.firstCoord == (y, x)):
            self.firstCoord = None
            return 1
        
        

        # place first piece on new sqaure
        if (self.firstCoord != None) and (newSensor == 1) and (self.secondCoord == None):
            if self.checkValidMove((self.firstCoord, (y, x))):
                self.rawMove(((self.firstCoord, (y, x))))
                self.firstCoord = None
                return 1
            else:
                return 0

        # pick up second piece for capture
        if (self.firstCoord != None) and (newSensor == 0) and (self.secondCoord == None):
            self.secondCoord = (y, x)
            return  1
        
        # capture second piece
        if (self.firstCoord != None) and (newSensor == 1) and (self.secondCoord != None):
            if self.checkValidMove(self.firstCoord, (y, x)):
                self.state[self.secondCoord[0]][self.secondCoord[1]] = 0 # nessesary in case we add enpassant
                self.rawMove(self.firstCoord, (y, x))
                self.firstCoord = None
                self.secondCoord = None
                return 1
            else:
                return 0
            
            
        return -2 # nothing ran some how????? this should never excute unless i'm low.