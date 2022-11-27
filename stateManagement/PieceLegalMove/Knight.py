from Constants import MAX, MIN, enemy

def knightLegal(row, col, boardState):
    moves = []

    # if row + 1 <= MAX and col + 2 <= MAX and (boardState[row + 1][col + 2] == 0 or boardState[row + 1][col + 2] == enemy):
    if boardState[row + 1][col + 2] == 0 or boardState[row + 1][col + 2] == enemy:
        moves.append((row + 1, col + 2))

    # if row + 1 <= MAX and col - 2 >= MIN and (boardState[row + 1][col - 2] == 0 or boardState[row + 1][col - 2] == enemy):
    if boardState[row + 1][col - 2] == 0 or boardState[row + 1][col - 2] == enemy:
        moves.append((row + 1, col - 2))

    # if row - 1 >= MIN and col + 2 <= MAX and (boardState[row - 1][col + 2] == 0 or boardState[row - 1][col + 2] == enemy):
    if boardState[row - 1][col + 2] == 0 or boardState[row - 1][col + 2] == enemy:
        moves.append((row - 1, col + 2))

    # if row - 1 >= MIN and col - 2 >= MIN and (boardState[row - 1][col - 2] == 0 or boardState[row - 1][col - 2] == enemy):
    if boardState[row - 1][col - 2] == 0 or boardState[row - 1][col - 2] == enemy:
        moves.append((row - 1, col - 2))

    # if row + 2 <= MAX and col + 1 <= MAX and (boardState[row + 2][col + 1] == 0 or boardState[row + 2][col + 1] == enemy):
    if boardState[row + 2][col + 1] == 0 or boardState[row + 2][col + 1] == enemy:
        moves.append((row + 2, col + 1))

    # if row + 2 <= MAX and col - 1 >= MIN and (boardState[row + 2][col - 1] == 0 or boardState[row + 2][col - 1] == enemy):
    if boardState[row + 2][col - 1] == 0 or boardState[row + 2][col - 1] == enemy:
        moves.append((row + 1, col + 2))

    # if row - 2 >= MIN and col + 1 <= MAX and (boardState[row - 2][col + 1] == 0 or boardState[row - 2][col + 1] == enemy):
    if boardState[row - 2][col + 1] == 0 or boardState[row - 2][col + 1] == enemy:
        moves.append((row + 1, col + 2))

    # if row - 2 >= MIN and col - 1 >= MIN and (boardState[row - 2][col - 1] == 0 or boardState[row - 2][col - 1] == enemy):
    if boardState[row - 2][col - 1] == 0 or boardState[row - 2][col - 1] == enemy:
        moves.append((row - 2, col - 1))