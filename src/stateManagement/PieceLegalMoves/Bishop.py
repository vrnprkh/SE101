from . import Constants

def bishopLegal(row, col, boardState):
    moves = []
    r = row
    c = col
    while r < Constants.MAX and c < Constants.MAX:
        r += 1
        c += 1
        if boardState[r][c] != 0 and boardState[r][c] != Constants.enemy:
            break
        moves.append((r, c))

    r = row
    c = col

    while r < Constants.MAX and c > Constants.MIN:
        r += 1
        c -= 1
        if boardState[r][c] != 0 and boardState[r][c] != Constants.enemy:
            break
        moves.append((r, c))

    r = row
    c = col

    while r > Constants.MIN and c < Constants.MAX:
        r -= 1
        c += 1
        if boardState[r][c] != 0 and boardState[r][c] != Constants.enemy:
            break
        moves.append((r, c))

    r = row
    c = col

    while r > Constants.MIN and c > Constants.MIN:
        r -= 1
        c -= 1
        if boardState[r][c] != 0 and boardState[r][c] != Constants.enemy:
            break
        moves.append((r, c))
    
    return moves