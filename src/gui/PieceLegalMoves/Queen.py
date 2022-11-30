from . import Rook, Bishop

def queenLegal(row, col, boardState):
    return Rook.rookLegal(row, col, boardState) + Bishop.bishopLegal(row, col, boardState)