import pygame
import os
from .PieceLegalMoves import Pawn, Rook, Bishop, Knight, Queen, King, Constants
from .formatState import formatBoardState

# from ..stateManagement.PieceLegalMoves import Pawn, Bishop, Knight, Rook, Queen, King
# Pawn = importlib.import_module( os.path.abspath(os.path.join( os.path.dirname(__file__), "..", "stateManagement", "PieceLegalMoves", "Pawn.py")) )
# Bishop = importlib.import_module( os.path.abspath(os.path.join( os.path.dirname(__file__), "..", "stateManagement", "PieceLegalMoves", "Bishop.py")) )
# Knight = importlib.import_module( os.path.abspath(os.path.join( os.path.dirname(__file__), "..", "stateManagement", "PieceLegalMoves", "Knight.py")) )
# Rook = importlib.import_module( os.path.abspath(os.path.join( os.path.dirname(__file__), "..", "stateManagement", "PieceLegalMoves", "Rook.py")) )
# Queen = importlib.import_module( os.path.abspath(os.path.join( os.path.dirname(__file__), "..", "stateManagement", "PieceLegalMoves", "Quuen.py")) )
# King = importlib.import_module( os.path.abspath(os.path.join( os.path.dirname(__file__), "..", "stateManagement", "PieceLegalMoves", "King.py")) )


pygame.init() 
base_path = os.path.dirname(__file__)
images_path = os.path.join(base_path, "graphics")

# none = 0; black pawn = 1; black rook = 2; black knight = 3; black bishop = 4; black queen = 5; black king = 6
# white pawn = 7; white rook = 8; white knight = 9; white bishop = 10; white queen = 11; white king = 12

chessPieces = []
tutorialImages = []
for (dirpath, dirnames, filenames) in os.walk(images_path):
    for file in filenames:
        if 'txt' not in file and 'chosen' not in file and 'Move' not in file and 'Tutorial' not in file and 'Square' not in file:
            chessPieces.append(os.path.join(images_path, file))
        if 'Tutorial' in file:
            tutorialImages.append(os.path.join(images_path, file))

    break

for file in chessPieces:
    if ".DS_Store" in file:
        chessPieces.remove(file)
        tutorialImages.remove(file)

        
chessPieces.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
tutorialImages.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

# returns the condition that determines whether the user's move is valid or invalid
def isValid(condtion = True):
    return condtion

def displayGame (gameState, pieceCoord, condition = True, substate = [], highlighted = []):
    screen = pygame.display.set_mode([1100, 800])
    pygame.display.set_caption('NandanLabs')

    if (pieceCoord is None): piece = 0
    else: piece = gameState[pieceCoord[0]] [pieceCoord[1]]

    pieceStr = ["txtPawn.png", "txtRook.png", "txtKnight.png", "txtBishop.png", "txtQueen.png", "txtKing.png", "txtPawn.png", "txtRook.png", "txtKnight.png", "txtBishop.png", "txtQueen.png", "txtKing.png"]
    coords = [[[80, 80], [240, 80], [400, 80], [560, 80]],
            [[80, 240], [240, 240], [400, 240], [560, 240]],
            [[80, 400], [240, 400], [400, 400], [560, 400]],
            [[80, 560], [240, 560], [400, 560], [560, 560]]]

    running = True

    screen.fill((40, 43, 47))
    pygame.draw.rect(screen, (75, 79, 84), pygame.Rect(750, 70, 280, (160*4)+20), 2, 3)
    pygame.draw.rect(screen, (40, 43, 47), pygame.Rect(760, 80, 260, 360), 2)
    pygame.draw.rect(screen, (75, 79, 84), pygame.Rect(70, 70, (160*4)+20, (160*4)+20), 2, 3)

    chosenPieceTxt = pygame.image.load( os.path.join(os.path.dirname(__file__), "graphics", "chosenPiece.png") ).convert_alpha()
    screen.blit(chosenPieceTxt, (800, 70))
    if (piece != 0):
        chosenPieceImg = pygame.image.load(chessPieces[piece-1]).convert_alpha()
        chosenPieceImg = pygame.transform.scale(chosenPieceImg, (100, 120))
        screen.blit(chosenPieceImg, (840, 180))
        pieceTxt = pygame.image.load( os.path.join(images_path, pieceStr[piece-1]) ).convert_alpha()
        screen.blit(pieceTxt, (755, 280))
    
    if (pieceCoord is not None):
        if (isValid(condition)):
            isValidImg = pygame.image.load(os.path.join(os.path.dirname(__file__), "graphics", "validMove.png")).convert_alpha()
        else:
            isValidImg = pygame.image.load(os.path.join(os.path.dirname(__file__), "graphics", "invalidMove.png")).convert_alpha()
    
        screen.blit(isValidImg, (775, 360))

    # Draw the chessboard
    gray = (175, 171, 157)
    cream = (232, 233, 222)
    x = 80
    y = 80
    for i in range (0, 4):
        for j in range (0, 4):
            if ((i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0)): colour = cream
            else: colour = gray
            pygame.draw.rect(screen, colour, pygame.Rect(x+(160*j), y+(160*i), 160, 160))

    if pieceCoord is not None:
        colourSquares(pieceCoord, formatBoardState(gameState, piece), x, y, screen)

    # Displays the mini tutorial on the side
    if piece > 6: tutorialNum = piece - 6
    elif(piece > 0): tutorialNum = piece
    
    if (piece != 0):
        tutorialImg = pygame.image.load(tutorialImages[tutorialNum-1]).convert_alpha()
        tutorialImg = pygame.transform.scale(tutorialImg, (160, 140))
        screen.blit(tutorialImg, (820, 530)) #edit: prob need to change the coords 
        
    
    # Draws the chess pieces onto the board
    for i in range(len(gameState)):
        for j in range(len(gameState[i])):
            if (gameState[i][j] != 0):
                img = pygame.image.load(chessPieces[gameState[i][j] - 1]).convert_alpha()
                screen.blit(img, (coords[i][j][0], coords[i][j][1]))

    
    pygame.display.flip()


def colourSquares(pieceCoord, gameState, x, y, screen):
    row, col = pieceCoord
    piece = gameState[row][col]

    possibleMoves = None
    if piece == 1:
        possibleMoves = Pawn.pawnBlackLegal(row, col, gameState)
    if piece == 7:
        possibleMoves = Pawn.pawnWhiteLegal(row, col, gameState)
    elif piece == 2 or piece == 8:
        possibleMoves = Rook.rookLegal(row, col, gameState)
    elif piece == 3 or piece == 9:
        possibleMoves = Knight.knightLegal(row, col, gameState)
    elif piece == 4 or piece == 10:
        possibleMoves = Bishop.bishopLegal(row, col, gameState)
    elif piece == 5 or piece == 11:
        possibleMoves = Queen.queenLegal(row, col, gameState)
    elif piece == 6 or piece == 12:
        possibleMoves = King.kingLegal(row, col, gameState)

    # Highlights the possible squares the player can move their piece to
    if possibleMoves == None:
        return
        
    for element in possibleMoves:
        row = element [0]
        col = element [1]
        if gameState[row][col] == Constants.enemy:
            pygame.draw.rect(screen, (25, 150, 25), pygame.Rect(x+(160*col), y+(160*row), 160, 160))
        else:
            square = pygame.image.load(os.path.join(os.path.dirname(__file__), "graphics", "validSquare.png")).convert_alpha()
            screen.blit(square, (x+(160*col), y+(160*row)))
