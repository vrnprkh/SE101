from Constants import MAX, MIN, enemy

def rookLegal(row, col, boardState):
    moves = []
    r = row
    while r <= MAX:
        r += 1
        if boardState[r][col] != 0 and boardState[r][col] != enemy:
            break
        moves.append((r, col))
    
    r = row
    while r >= MIN:
        r -= 1
        if boardState[r][col] != 0 and boardState[r][col] != enemy:
            break
        moves.append((r, col))
    
    c = col
    while c <= MAX:
        c += 1
        if boardState[row][c] != 0 and boardState[row][c] != enemy:
            break
        moves.append((row, c))
    
    c = col
    while c >= MIN:
        c -= 1
        if boardState[row][c] != 0 and boardState[row][c] != enemy:
            break
        moves.append((row, c))
    
    return moves