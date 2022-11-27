enemy = -1
MAX = 3
MIN = 0

def isLegal(piece, move, boardState):
    if (piece == "king") and move[1] in kingLegal(move[0][0], move[0][1], boardState):
        return True
    elif (piece == "queen") and move[1] in queenLegal(move[0][0], move[0][1], boardState):
        return True
    elif (piece == "bishop") and move[1] in bishopLegal(move[0][0], move[0][1], boardState):
        return True
    elif (piece == "rook") and move[1] in rookLegal(move[0][0], move[0][1], boardState):
        return True
    elif (piece == "pawn") and move[1] in pawnLegal(move[0][0], move[0][1], boardState):
        return True
    elif (piece == "knight") and move[1] in knightLegal(move[0][0], move[0][1], boardState):
        return True
    else:
        return False

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

def queenLegal(row, col, boardState):
    return rookLegal(row, col, boardState) + bishopLegal(row, col, boardState)
    


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

    while r >= MAX and c <= MAX:
        r -= 1
        c += 1
        if boardState[r][c] != 0 and boardState[r][c] != enemy:
            break
        moves.append((r, c))

    r = row
    c = col

    while r >= MAX and c >= MAX:
        r -= 1
        c -= 1
        if boardState[r][c] != 0 and boardState[r][c] != enemy:
            break
        moves.append((r, c))
    
    return moves

def pawnLegal(row, col, boardState):
    moves = []
    if boardState[row][col + 1] == 0 or boardState[row][col + 1] == enemy:
        moves.append((row, col + 1))

    if boardState[row + 1][col + 1] == enemy:
        moves.append((row + 1, col + 1))
    
    if boardState[row - 1][col + 1] == enemy:
        moves.append((row - 1, col + 1))
    
    return moves