from Constants import MAX, MIN, enemy

def kingLegal(row, col, boardState):
    moves = []
    if boardState[row + 1][col] == 0 or boardState[row + 1][col] == enemy:
        moves.append((row + 1, col))

    if boardState[row - 1][col] == 0 or boardState[row - 1][col] == enemy:
        moves.append((row - 1, col))
    
    if boardState[row][col + 1] == 0 or boardState[row][col + 1] == enemy:
        moves.append((row, col + 1))

    if boardState[row][col - 1] == 0 or boardState[row][col - 1] == enemy:
        moves.append((row, col - 1))

    if boardState[row + 1][col + 1] == 0 or boardState[row + 1][col + 1] == enemy:
        moves.append((row + 1, col + 1))
    
    if boardState[row + 1][col - 1] == 0 or boardState[row + 1][col - 1] == enemy:
        moves.append((row + 1, col - 1))
    
    if boardState[row - 1][col + 1] == 0 or boardState[row - 1][col + 1] == enemy:
        moves.append((row - 1, col + 1))
    
    if boardState[row - 1][col - 1] == 0 or boardState[row - 1][col - 1] == enemy:
        moves.append((row - 1, col - 1))
    
    return moves