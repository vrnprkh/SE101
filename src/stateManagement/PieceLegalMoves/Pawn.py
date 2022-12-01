from . import Constants

def pawnLegal(row, col, boardState):
    moves = []

    if row + 1 <= Constants.MAX and (boardState[row + 1][col] == 0 or boardState[row + 1][col] == Constants.enemy):
    # if boardState[row + 1][col] == 0 or boardState[row][col + 1] == Constants.enemy:
        moves.append((row + 1, col))

    if row + 1 <= Constants.MAX and col + 1 <= Constants.MAX and boardState[row + 1][col + 1] == Constants.enemy:
    # if boardState[row - 1][col + 1] == Constants.enemy:
        moves.append((row + 1, col + 1))
    
    if row + 1 <= Constants.MAX and col - 1 >= Constants.MIN and boardState[row - 1][col - 1] == Constants.enemy:
    # if boardState[row - 1][col - 1] == Constants.enemy:
        moves.append((row + 1, col - 1))
    
    return moves