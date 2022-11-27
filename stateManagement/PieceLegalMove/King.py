from Constants import MAX, MIN, enemy

def kingLegal(row, col, boardState):
    moves = []
    # if row + 1 <= MAX and (boardState[row + 1][col] == 0 or boardState[row + 1][col] == enemy):
    if boardState[row + 1][col] == 0 or boardState[row + 1][col] == enemy:
        moves.append((row + 1, col))

    # if row - 1 >= MIN and (boardState[row - 1][col] == 0 or boardState[row - 1][col] == enemy):
    if boardState[row - 1][col] == 0 or boardState[row - 1][col] == enemy:
        moves.append((row - 1, col))
    
    # if col + 1 <= MAX and (boardState[row][col + 1] == 0 or boardState[row][col + 1] == enemy):
    if boardState[row][col + 1] == 0 or boardState[row][col + 1] == enemy:
        moves.append((row, col + 1))

    # if col - 1 >= MIN and (boardState[row][col - 1] == 0 or boardState[row][col - 1] == enemy):
    if boardState[row][col - 1] == 0 or boardState[row][col - 1] == enemy:
        moves.append((row, col - 1))

    # if row + 1 <= MAX and col + 1 <= MAX and (boardState[row + 1][col + 1] == 0 or boardState[row + 1][col + 1] == enemy):
    if boardState[row + 1][col + 1] == 0 or boardState[row + 1][col + 1] == enemy:
        moves.append((row + 1, col + 1))
    
    # if row + 1 <= MAX and col - 1 >= MIN and (boardState[row + 1][col - 1] == 0 or boardState[row + 1][col - 1] == enemy):
    if boardState[row + 1][col - 1] == 0 or boardState[row + 1][col - 1] == enemy:
        moves.append((row + 1, col - 1))
    
    # if row - 1 >= MIN and col + 1 <= MAX and (boardState[row - 1][col + 1] == 0 or boardState[row - 1][col + 1] == enemy):
    if boardState[row - 1][col + 1] == 0 or boardState[row - 1][col + 1] == enemy:
        moves.append((row - 1, col + 1))
    
    # if row - 1 >= MIN and col - 1 >= MIN and (boardState[row - 1][col - 1] == 0 or boardState[row - 1][col - 1] == enemy):
    if boardState[row - 1][col - 1] == 0 or boardState[row - 1][col - 1] == enemy:
        moves.append((row - 1, col - 1))
    
    return moves