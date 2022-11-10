import pygame
import globals
import test
import os,sys
import re

pygame.init() 
def isLegal (piece):
    legality = True

    return legality



def displayGame ():
    pygame.font.init() 
    my_font = pygame.font.SysFont('Helvectia Nue Bold', 60)
    screen = pygame.display.set_mode([1100, 800])
    pygame.display.set_caption('NandanLabs')

    base_path = os.path.dirname(__file__)
    images_path = os.path.join(base_path, "graphics")

    # none = 0; black pawn = 1; black rook = 2; black knight = 3; black bishop = 4; black queen = 5; black king = 6
    # white pawn = 7; white rook = 8; white knight = 9; white bishop = 10; white queen = 11; white king = 12
    globals.init()
    test.change()
    gameState = globals.gameState

    chessPieces = []
    for (dirpath, dirnames, filenames) in os.walk(images_path):
        for file in filenames:
            if 'txt' not in file and 'chosen' not in file:
                chessPieces.append(os.path.join(images_path, file))

        break

    for file in chessPieces:
        if ".DS_Store" in file:
            chessPieces.remove(file)
        


    # chessPieces = [images_path+"Pawn.png", images_path+"Rook.png", images_path+"Knight.png", images_path+"Bishop.png", images_path+"Queen.png", images_path+"King.png", images_path+"PawnW.png", path+"RookW.png", path+"KnightW.png", path+"BishopW.png", path+"QueenW.png", +"KingW.png"]
    pieceStr = ["txtPawn.png", "txtRook.png", "txtKnight.png", "txtBishop.png", "txtQueen.png", "txtKing.png", "txtPawn.png", "txtRook.png", "txtKnight.png", "txtBishop.png", "txtQueen.png", "txtKing.png"]
    coords = [[[80, 80], [240, 80], [400, 80], [560, 80]],
            [[80, 240], [240, 240], [400, 240], [560, 240]],
            [[80, 400], [240, 400], [400, 400], [560, 400]],
            [[80, 560], [240, 560], [400, 560], [560, 560]]]

    piece = 6

    # Run until the user asks to quit
    running = True
    while running:
        
        # Closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        screen.fill((40, 43, 47))
        pygame.draw.rect(screen, (75, 79, 84), pygame.Rect(750, 70, 280, (160*4)+20), 2, 3)

        pygame.draw.rect(screen, (40, 43, 47), pygame.Rect(760, 80, 260, 360), 2)
        
        pygame.draw.rect(screen, (75, 79, 84), pygame.Rect(70, 70, (160*4)+20, (160*4)+20), 2, 3)

        chosenPieceTxt = pygame.image.load('./gui/graphics/chosenPiece.png').convert_alpha()
        screen.blit(chosenPieceTxt, (800, 70))
        chosenPieceImg = pygame.image.load(chessPieces[piece]).convert_alpha()
        screen.blit(chosenPieceImg, (815, 180))
        pieceTxt = pygame.image.load( os.path.join(images_path, pieceStr[piece]) ).convert_alpha()
        screen.blit(pieceTxt, (755, 310))
       

    
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

        for i in range(len(gameState)):
            for j in range(len(gameState[i])):
                if (gameState[i][j] != 0):
                    img = pygame.image.load(chessPieces[gameState[i][j] - 1]).convert_alpha()
                    screen.blit(img, (coords[i][j][0], coords[i][j][1]))

          
        pygame.display.flip()

    pygame.quit()