from Constants import MAX, MIN, enemy

def pawnLegal(row, col, boardState):
    if boardState[row][col + 1] == 0 or boardState[row][col + 1] == enemy: