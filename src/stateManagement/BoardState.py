from .PieceLegalMoves import Constants

class BoardState:
    def __init__(self, state):
        self.state = state
    # move from (y1, x1) -> (y2, x2)
    # in the form ((y1, x1), (y2, x2))
    def updateState(self, move):
        # print("hellooooooooooooooooooo")
        coord1 = move[0]
        coord2 = move[1]
        self.state[coord2[0]][coord2[1]] = self.state[coord1[0]][coord1[1]]
        self.state[coord1[0]][coord1[1]] = 0

    def formatBoardState(self):
        #We will consider any black pieces as being the opponent 
            #White pieces have a value in the range [7...12]
        copy_state = [ [i for i in row] for row in self.state ]
        
        for row in copy_state:
            for col in row:
                if col in [7, 8, 9, 10, 11, 12]:
                    copy_state[row][col] = Constants.enemy

        return copy_state