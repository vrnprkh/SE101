from Constants import MAX, MIN, enemy
from Rook import rookLegal
from Bishop import bishopLegal

def queenLegal(row, col, boardState):
    return rookLegal(row, col, boardState) + bishopLegal(row, col, boardState)