import pygame
pygame.init() 
def isLegal (piece):
    legality = True
        
    return legality

def displayGame ():
    screen = pygame.display.set_mode([800, 800])
    path = './graphics/'

    # none = 0; pawn = 1; rook = 2; knight = 3; bishop = 4; queen = 5; king = 6
    gameState = [[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    chessPieces = [path+"Pawn.png", path+"Rook.png", path+"Knight.png", path+"Bishop.png", path+"Queen.png", path+"King.png"]

    coords = [[[0, 0], [200, 0], [400, 0], [600, 0], [800, 0]],
            [[0, 200], [200, 200], [400, 200], [600, 200], [800, 200]],
            [[0, 400], [200, 400], [400, 400], [600, 400], [800, 400]],
            [[0, 600], [200, 600], [400, 600], [600, 600], [800, 600]]]

    piece = 0

    # Run until the user asks to quit
    running = True
    while running:

        # Closes window
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        screen.fill((238, 237, 232))

        # Draw the chessboard
        gray = (175, 171, 157)
        cream = (232, 233, 222)
        x = 0
        y = 0
        for i in range (0, 4):
            for j in range (0, 4):
                if ((i%2 == 0 and j%2 == 0) or (i%2 != 0 and j%2 != 0)): colour = cream
                else: colour = gray
                pygame.draw.rect(screen, colour, pygame.Rect(x+(200*j), y+(200*i), 200, 200))

        for i in range(len(gameState)):
            for j in range(len(gameState[i])):
                    if (gameState[i][j] != 0):
                        img = pygame.image.load(chessPieces[gameState[i][j] - 1]).convert_alpha()
                        screen.blit(img, (coords[i][j][0], coords[i][j][1]))
                        
        pygame.display.flip()

    pygame.quit()

def main ():
    displayGame()
    
if __name__=="__main__":
    main()