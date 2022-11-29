from . import Constants

def pawnLegal(row, col, boardState):
    moves = []

    #if col + 1 <= MAX and (boardState[row][col + 1] == 0 or boardState[row][col + 1] == enemy):
    if boardState[row][col + 1] == 0 or boardState[row][col + 1] == Constants.enemy:
        moves.append((row, col + 1))

    #if row + 1 <= MAX and col + 1 <= MAX boardState[row + 1][col + 1] == enemy:
    if boardState[row + 1][col + 1] == Constants.enemy:
        moves.append((row + 1, col + 1))
    
    #if row - 1 >= MIN and col - 1 >= MIN boardState[row + 1][col + 1] == enemy:
    if boardState[row - 1][col + 1] == Constants.enemy:
        moves.append((row - 1, col + 1))
    
    return moves