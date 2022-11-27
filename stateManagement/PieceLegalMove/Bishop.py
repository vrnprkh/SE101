from Constants import MAX, MIN, enemy

def bishopLegal(row, col, boardState):
    moves = []
    r = row
    c = col
    while r <= MAX and c <= MAX:
        r += 1
        c += 1
        if boardState[r][c] != 0 and boardState[r][c] != enemy:
            break
        moves.append((r, c))

    r = row
    c = col

    while r <= MAX and c >= MIN:
        r += 1
        c -= 1
        if boardState[r][c] != 0 and boardState[r][c] != enemy:
            break
        moves.append((r, c))

    r = row
    c = col

    while r >= MIN and c <= MAX:
        r -= 1
        c += 1
        if boardState[r][c] != 0 and boardState[r][c] != enemy:
            break
        moves.append((r, c))

    r = row
    c = col

    while r >= MIN and c >= MIN:
        r -= 1
        c -= 1
        if boardState[r][c] != 0 and boardState[r][c] != enemy:
            break
        moves.append((r, c))
    
    return moves