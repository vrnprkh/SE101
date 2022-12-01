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

    def formatBoardState(self, piece):
        #We will consider any black pieces as being the opponent 
            #White pieces have a value in the range [7...12]
        copy_state = [ [i for i in row] for row in self.state ]
        print(copy_state)

        colour = ""
        if piece in [7, 8, 9, 10, 11, 12]:
            colour = "white"
        elif piece in [1, 2, 3, 4, 5, 6]:
            colour = "black"

        for i, row in enumerate(copy_state):
            for j, col in enumerate(row):
                if colour == "white" and col in [1, 2, 3, 4, 5, 6]:
                    copy_state[i][j] = Constants.enemy
                elif colour == "black" and col in [7, 8, 9, 10, 11, 12]:
                    copy_state[i][j] = Constants.enemy

        return copy_state