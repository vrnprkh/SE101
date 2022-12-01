from .PieceLegalMoves import Constants

def formatBoardState(gameState, piece):
    #We will consider any black pieces as being the opponent 
        #White pieces have a value in the range [7...12]
    copy_state = [ [i for i in row] for row in gameState ]
    print(copy_state)

    colour = ""
    if piece in [7, 8, 9, 10, 11, 12]:
        colour = "white"
    elif piece in [1, 2, 3, 4, 5, 6]:
        colour = "black"

    for i, row in enumerate(copy_state):
        for j, col in enumerate(row):
            if colour == "white" and copy_state[i][j] in [1, 2, 3, 4, 5, 6]:
                copy_state[i][j] = Constants.enemy
            elif colour == "black" and copy_state[i][j] in [7, 8, 9, 10, 11, 12]:
                copy_state[i][j] = Constants.enemy

    return copy_state