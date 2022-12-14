from .PieceLegalMoves import Constants
from .PieceLegalMoves import Pawn, Bishop, Knight, Rook, Queen, King

#from PieceLegalMove import Bishop, King, Knight, Pawn, Queen, Rook, Constants

# Tutorial data is substates
class LegalMoveProcessor:
    @staticmethod
    def isLegalTutorialMove(boardProcessor, move):
        i = 0
        for e in boardProcessor.tutorial.subStates[boardProcessor.csubState][1][0]:
            if e[0] == move[0] and e[1] == move[1]:
                boardProcessor.csubState = boardProcessor.tutorial.subStates[boardProcessor.csubState][1][1][i]
                print(i)
                print("csub " + str(boardProcessor.csubState))
                return True
            i += 1
            
        return False

    @staticmethod
    def isLegal(boardProcessor, move, piece):
        #print("hello i am runnigh :)))))))))))))))))))")
        if not boardProcessor.tutorial == None:
            return LegalMoveProcessor.isLegalTutorialMove(move)

        if piece == 1:
            return (move[1] in Pawn.pawnBlackLegal(move[0][0], move[0][1], boardProcessor.boardState.formatBoardState(piece)))

        if piece == 7:
            return (move[1] in Pawn.pawnWhiteLegal(move[0][0], move[0][1], boardProcessor.boardState.formatBoardState(piece)))

        if piece == 9 or piece == 3:
            return (move[1] in Knight.knightLegal(move[0][0], move[0][1], boardProcessor.boardState.formatBoardState(piece)))

        if piece == 4 or piece == 10:
            return (move[1] in Bishop.bishopLegal(move[0][0], move[0][1], boardProcessor.boardState.formatBoardState(piece)))

        if piece == 2 or piece == 8:
            return (move[1] in Rook.rookLegal(move[0][0], move[0][1], boardProcessor.boardState.formatBoardState(piece)))
        
        if piece == 5 or piece == 11:
            return (move[1] in Queen.queenLegal(move[0][0], move[0][1], boardProcessor.boardState.formatBoardState(piece)))

        if piece == 6 or piece == 12:
            return (move[1] in King.kingLegal(move[0][0], move[0][1], boardProcessor.boardState.formatBoardState(piece)))

        return False


#Class that will generate a list of legal moves
class Cell:
    def __init__(self) -> None:
        self.legalNextMove = False
        self.currentlyOccupied = False

class LegalMoves:
    def __init__(self, piece) -> None:
        self.size = Constants.BS #Basing the max size off of this but it's okay
        self.piece = piece
        self.theGrid = [ [Cell() for j in range(self.size)] for i in range(self.size) ]

    def PawnNextLegalMoves(self, state, position):
        for i in range(self.size):
            for j in range(self.size):
                self.theGrid[i][j].legalNextMove = False
                self.theGrid[i][j].currentlyOccupied = False if state[i][j] == Constants.enemy else True

        if position[1] + 1 < self.size and not self.theGrid[position[0]][position[1] + 1].currentlyOccupied:
            self.theGrid[position[0]][position[1] + 1].legalNextMove = True
        if position[0] + 1 < self.size and position[1] + 1 < self.size and self.theGrid[position[0]][position[1] + 1].currentlyOccupied:
            self.theGrid[position[0] + 1][position[1] + 1].legalNextMove = True
        if position[0] - 1 > -1 and position[1] + 1 < self.size and self.theGrid[position[0]][position[1] + 1].currentlyOccupied:
            self.theGrid[position[0] - 1][position[1] + 1].legalNextMove = True

        return self.theGrid.copy()

    def KnightNextLegalMoves(self, state, position):
        for i in range(self.size):
            for j in range(self.size):
                self.theGrid[i][j].legalNextMove = False
                self.theGrid[i][j].currentlyOccupied = False if state[i][j] == Constants.enemy else True

        self.theGrid[position[0] + 2][position[1] + 1].legalNextMove = True if position[0] + 2 < self.size and position[1] + 1 < self.size else False
        self.theGrid[position[0] + 2][position[1] - 1].legalNextMove = True if position[0] + 2 < self.size and position[1] + 1 < self.size else False
        self.theGrid[position[0] - 2][position[1] + 1].legalNextMove = True if position[0] - 2 > -1 and position[1] + 1 < self.size else False
        self.theGrid[position[0] - 2][position[1] - 1].legalNextMove = True if position[0] - 2 > -1 and position[1] - 1 > - 1 else False
        self.theGrid[position[0] + 1][position[1] + 2].legalNextMove = True if position[0] + 1 < self.size and position[1] + 2 < self.size else False
        self.theGrid[position[0] + 1][position[1] - 2].legalNextMove = True if position[0] + 1 < self.size and position[1] - 2 > -1 else False
        self.theGrid[position[0] - 1][position[1] + 2].legalNextMove = True if position[0] - 1 > -1 and position[1] + 2 < self.size else False
        self.theGrid[position[0] - 1][position[1] - 2].legalNextMove = True if position[0] - 1 > -1 and position[1] - 2 > -1 else False

        return self.theGrid.copy()

    def BishopNextLegalMoves(self, state, position):
        for i in range(self.size):
            for j in range(self.size):
                self.theGrid[i][j].legalNextMove = False
                self.theGrid[i][j].currentlyOccupied = False if state[i][j] == Constants.enemy else True

        pos = [position[0] + 1, position[1] + 1]
        while pos[0] < self.size:
            self.theGrid[pos[0]][pos[1]].legalNextMove = True
            if self.theGrid[pos[0]][pos[1]].currentlyOccupied == True:
                break
                
            pos[0] += 1
            pos[1] += 1

        pos = [position[0] - 1, position[1] + 1]
        while pos[0] > -1 and pos[1] < self.size:
            self.theGrid[pos[0]][pos[1]].legalNextMove = True
            if self.theGrid[pos[0]][pos[1]].currentlyOccupied == True:
                break

            pos[0] -= 1
            pos[1] += 1

        pos = [position[0] + 1, position[1] - 1]
        while pos[0] < self.size and pos[1] > -1:
            self.theGrid[pos[0]][pos[1]].legalNextMove = True
            if self.theGrid[pos[0]][pos[1]].currentlyOccupied == True:
                break

            pos[0] += 1
            pos[1] -= 1

        pos = [position[0] - 1, position[1] - 1]
        while pos[0] > -1 and pos[1] > -1:
            self.theGrid[pos[0]][pos[1]].legalNextMove = True
            if self.theGrid[pos[0]][pos[1]].currentlyOccupied == True:
                break

            pos[0] -= 1
            pos[1] -= 1 

        return self.theGrid.copy()

    def RookNextLegalMoves(self, state, position):
        for i in range(self.size):
            for j in range(self.size):
                self.theGrid[i][j].legalNextMove = False
                self.theGrid[i][j].currentlyOccupied = False if state[i][j] == Constants.enemy else True

        pos = [position[0] + 1, position[1]]
        while pos[0] < self.size:
            self.theGrid[pos[0]][pos[1]].legalNextMove = True
            if self.theGrid[pos[0]][pos[1]].currentlyOccupied == True:
                break

            pos[0] += 1

        pos = [position[0] - 1, position[1]]
        while pos[0] > -1:
            self.theGrid[pos[0]][pos[1]].legalNextMove = True
            if self.theGrid[pos[0]][pos[1]].currentlyOccupied == True:
                break

            pos[0] -= 1

        pos = [position[0], position[1] + 1]
        while pos[1] < self.size:
            self.theGrid[pos[0]][pos[1]].legalNextMove = True
            if self.theGrid[pos[0]][pos[1]].currentlyOccupied == True:
                break

            pos[1] += 1

        pos = [position[0], position[1] - 1]
        while pos[0] > -1:
            self.theGrid[pos[0]][pos[1]].legalNextMove = True
            if self.theGrid[pos[0]][pos[1]].currentlyOccupied == True:
                break
            
            pos[1] -= 1

        return self.theGrid.copy()


    def QueenNextLegalMoves(self, state, position):
        for i in range(self.size):
            for j in range(self.size):
                self.theGrid[i][j].legalNextMove = False
                self.theGrid[i][j].currentlyOccupied = False if state[i][j] == Constants.enemy else True

        rookMoves = self.RookNextLegalMoves(position)
        bishopMoves = self.BishopNextLegalMoves(position)

        for row in rookMoves:
            for col in row:
                self.theGrid[row][col].legalNextMove = rookMoves[row][col].legalNextMove

        for i in range(self.size):
            for col in range(self.size):
                self.theGrid[i][j].legalNextMove = bishopMoves[i][j].legalNextMove if bishopMoves[i][j].legalNextMove else self.theGrid[i][j].legalNextMove

        return self.theGrid.copy()

    def KingNextLegalMoves(self, state, position):
        for i in range(self.size):
            for j in range(self.size):
                self.theGrid[i][j].legalNextMove = False
                self.theGrid[i][j].currentlyOccupied = False if state[i][j] == Constants.enemy else True

        self.theGrid[position[0]][position[1] + 1].legalNextMove = True if position[1] + 1 < self.size else False
        self.theGrid[position[0]][position[1] - 1].legalNextMove = True if position[1] - 1 > -1 else False
        self.theGrid[position[0] + 1][position[1]].legalNextMove = True if position[0] + 1 < self.size else False
        self.theGrid[position[0] - 1][position[1]].legalNextMove = True if position[0] - 1 > -1 else False
        self.theGrid[position[0] + 1][position[1] + 1].legalNextMove = True if position[0] + 1 < self.size and position[1] + 1 < self.size else False
        self.theGrid[position[0] + 1][position[1] - 1].legalNextMove = True if position[0] + 1 < self.size and position[1] - 1 > -1 else False
        self.theGrid[position[0] - 1][position[1] + 1].legalNextMove = True if position[0] - 1 > -1 and position[1] + 1 < self.size else False
        self.theGrid[position[0] - 1][position[1] - 1].legalNextMove = True if position[0] - 1 > -1 and position[1] - 1 > -1 else False

        return self.theGrid.copy()