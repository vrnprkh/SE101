from . import Constants

def rookLegal(row, col, boardState):
    moves = []
    r = row
    while r <= Constants.MAX:
        r += 1
        if boardState[r][col] != 0 and boardState[r][col] != Constants.enemy:
            break
        moves.append((r, col))
    
    r = row
    while r >= Constants.MIN:
        r -= 1
        if boardState[r][col] != 0 and boardState[r][col] != Constants.enemy:
            break
        moves.append((r, col))
    
    c = col
    while c <= Constants.MAX:
        c += 1
        if boardState[row][c] != 0 and boardState[row][c] != Constants.enemy:
            break
        moves.append((row, c))
    
    c = col
    while c >= Constants.MIN:
        c -= 1
        if boardState[row][c] != 0 and boardState[row][c] != Constants.enemy:
            break
        moves.append((row, c))
    
    return moves