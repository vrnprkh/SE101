import pygame
import os

pygame.init() 
base_path = os.path.dirname(__file__)
images_path = os.path.join(base_path, "graphics")

# none = 0; black pawn = 1; black rook = 2; black knight = 3; black bishop = 4; black queen = 5; black king = 6
# white pawn = 7; white rook = 8; white knight = 9; white bishop = 10; white queen = 11; white king = 12

chessPieces = []
tutorialImages = []
for (dirpath, dirnames, filenames) in os.walk(images_path):
    for file in filenames:
        if 'txt' not in file and 'chosen' not in file and 'Move' not in file and 'Tutorial' not in file:
            chessPieces.append(os.path.join(images_path, file))
        if 'Tutorial' in file:
            tutorialImages.append(os.path.join(images_path, file))

    break

for file in chessPieces:
    if ".DS_Store" in file:
        chessPieces.remove(file)
        tutorialImages.remove(file)

        
chessPieces.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))
# print(chessPieces)
tutorialImages.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))


# returns the condition that determines whether the user's move is valid or invalid
def isValid(condtion = True):
    return condtion

def displayGame (gameState, pieceCoord, condition = True, substate = [], highlighted = []):

    screen = pygame.display.set_mode([1100, 800])
    pygame.display.set_caption('NandanLabs')

    if (pieceCoord is None): piece = 0
    else: piece = gameState[pieceCoord[0]] [pieceCoord[1]]

    # chessPieces = [images_path+"Pawn.png", images_path+"Rook.png", images_path+"Knight.png", images_path+"Bishop.png", images_path+"Queen.png", images_path+"King.png", images_path+"PawnW.png", path+"RookW.png", path+"KnightW.png", path+"BishopW.png", path+"QueenW.png", +"KingW.png"]
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
        screen.blit(chosenPieceImg, (812, 180))
        pieceTxt = pygame.image.load( os.path.join(images_path, pieceStr[piece-1]) ).convert_alpha()
        screen.blit(pieceTxt, (755, 310))
    
    if (isValid(condition)):
        isValidImg = pygame.image.load(os.path.join(os.path.dirname(__file__), "graphics", "validMove.png")).convert_alpha()
    else:
        isValidImg = pygame.image.load(os.path.join(os.path.dirname(__file__), "graphics", "invalidMove.png")).convert_alpha()
    
    screen.blit(isValidImg, (775, 400))

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

    
    # Highlights the possible squares the player can move their piece to
    # moves = substate[1]
    # for element in moves [0]:
    #     row = element [1][0]
    #     col = element [1][1]
    #     pygame.draw.rect(screen, (80, 155, 103), pygame.Rect(x+(160*row), y+(160*col), 160, 160))

    # # Displays the mini tutorial on the side
    if (piece > 6): tutorialNum = piece - 6
    elif (piece > 0): tutorialNum = piece
    
    if (piece != 0):
        tutorialImg = pygame.image.load(chessPieces[tutorialImages[tutorialNum] - 1]).convert_alpha()
        screen.blit(tutorialImg, (775, 500)) #edit: prob need to change the coords 
    
    # Draws the chess pieces onto the board
    for i in range(len(gameState)):
        for j in range(len(gameState[i])):
            if (gameState[i][j] != 0):
                img = pygame.image.load(chessPieces[gameState[i][j] - 1]).convert_alpha()
                screen.blit(img, (coords[i][j][0], coords[i][j][1]))

    
    pygame.display.flip()


