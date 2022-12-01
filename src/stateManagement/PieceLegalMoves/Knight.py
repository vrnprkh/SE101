from . import Constants

# from Constants import MAX, MIN, enemy

def knightLegal(row, col, boardState):
    moves = []

    if row + 1 <= Constants.MAX and col + 2 <= Constants.MAX and (boardState[row + 1][col + 2] == 0 or boardState[row + 1][col + 2] == Constants.enemy):
    # if boardState[row + 1][col + 2] == 0 or boardState[row + 1][col + 2] == enemy:
        moves.append((row + 1, col + 2))

    if row + 1 <= Constants.MAX and col - 2 >= Constants.MIN and (boardState[row + 1][col - 2] == 0 or boardState[row + 1][col - 2] == Constants.enemy):
    # if boardState[row + 1][col - 2] == 0 or boardState[row + 1][col - 2] == enemy:
        moves.append((row + 1, col - 2))

    if row - 1 >= Constants.MIN and col + 2 <= Constants.MAX and (boardState[row - 1][col + 2] == 0 or boardState[row - 1][col + 2] == Constants.enemy):
    # if boardState[row - 1][col + 2] == 0 or boardState[row - 1][col + 2] == enemy:
        moves.append((row - 1, col + 2))

    if row - 1 >= Constants.MIN and col - 2 >= Constants.MIN and (boardState[row - 1][col - 2] == 0 or boardState[row - 1][col - 2] == Constants.enemy):
    # if boardState[row - 1][col - 2] == 0 or boardState[row - 1][col - 2] == enemy:
        moves.append((row - 1, col - 2))

    if row + 2 <= Constants.MAX and col + 1 <= Constants.MAX and (boardState[row + 2][col + 1] == 0 or boardState[row + 2][col + 1] == Constants.enemy):
    # if boardState[row + 2][col + 1] == 0 or boardState[row + 2][col + 1] == enemy:
        moves.append((row + 2, col + 1))

    if row + 2 <= Constants.MAX and col - 1 >= Constants.MIN and (boardState[row + 2][col - 1] == 0 or boardState[row + 2][col - 1] == Constants.enemy):
    # if boardState[row + 2][col - 1] == 0 or boardState[row + 2][col - 1] == enemy:
        moves.append((row + 1, col + 2))

    if row - 2 >= Constants.MIN and col + 1 <= Constants.MAX and (boardState[row - 2][col + 1] == 0 or boardState[row - 2][col + 1] == Constants.enemy):
    # if boardState[row - 2][col + 1] == 0 or boardState[row - 2][col + 1] == enemy:
        moves.append((row + 1, col + 2))

    if row - 2 >= Constants.MIN and col - 1 >= Constants.MIN and (boardState[row - 2][col - 1] == 0 or boardState[row - 2][col - 1] == Constants.enemy):
    # if boardState[row - 2][col - 1] == 0 or boardState[row - 2][col - 1] == enemy:
        moves.append((row - 2, col - 1))

    return moves