from Constants import MAX, MIN, enemy

def knightLegal(row, col, boardState):
    moves = []
    if boardState[row + 1][col + 2] == 0 or boardState[row + 1][col + 2] == enemy:
        moves.append((row + 1, col + 2))

    if boardState[row + 1][col - 2] == 0 or boardState[row + 1][col - 2] == enemy:
        moves.append((row + 1, col - 2))

    if boardState[row - 1][col + 2] == 0 or boardState[row - 1][col + 2] == enemy:
        moves.append((row - 1, col + 2))

    if boardState[row - 1][col - 2] == 0 or boardState[row - 1][col - 2] == enemy:
        moves.append((row - 1, col - 2))

    if boardState[row + 2][col + 1] == 0 or boardState[row + 2][col + 1] == enemy:
        moves.append((row + 2, col + 1))

    if boardState[row + 2][col - 1] == 0 or boardState[row + 2][col - 1] == enemy:
        moves.append((row + 1, col + 2))

    if boardState[row - 2][col + 1] == 0 or boardState[row - 2][col + 1] == enemy:
        moves.append((row + 1, col + 2))

    if boardState[row - 2][col - 1] == 0 or boardState[row - 2][col - 1] == enemy:
        moves.append((row - 2, col - 1))