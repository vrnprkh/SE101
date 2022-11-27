from managerCombined import BoardProcessor, BoardState
from PieceLegalMove import Bishop, King, Knight, Pawn, Queen, Rook

# Tutorial data is substates
class LegalMoveProcessor:
    @staticmethod
    def isLegalTutorialMove(boardProcessor: BoardProcessor, move):
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
    def isLegal(boardProcessor: BoardProcessor, move, piece: str):
        #print("hello i am runnigh :)))))))))))))))))))")
        if not boardProcessor.tutorial == None:
            return LegalMoveProcessor.isLegalTutorialMove(move);

        if piece == "pawn":
            return Pawn.pawnLegal(move[0], move[1], boardProcessor.boardState)

        if piece == "knight":
            # return Knight.knightLegal(move[0], move[1], boardProcessor.boardState)
            return True

        if piece == "bishop":
            return Bishop.bishopLegal(move[0], move[1], boardProcessor.boardState)

        if piece == "rook":
            return Rook.rookLegal(move[0], move[1], boardProcessor.boardState)
        
        if piece == "queen":
            return Queen.queenLegal(move[0], move[1], boardProcessor.boardState)

        if piece == "king":
            return King.kingLegal(move[0], move[1], boardProcessor.boardState)

        return False

    # @staticmethod
    # def generateLegalMoves(piece: str, row, col, boardState: BoardState):
    #     if piece == "pawn":
    #         return 


"""
class Cell:
    def __init__(self) -> None:
        self.legalNextMove = False
        self.currentlyOccupied = False

class LegalMoves:
    def __init__(self, piece) -> None:
        self.size = 4
        self.piece = piece
        self.theGrid = [ [Cell() for j in range(self.size)] for i in range(self.size) ]

    def MarkNextLegalMoves(self, piece, position) -> None:
        #Step 1 - clear all previoous legal moves
        for i in range(self.size):
            for j in range(self.size):
                self.theGrid[i][j].legalNextMove = False
                self.theGrid[i][j].currentlyOccupied = False

        #Step 2 - find all legal moves and mark the cells as "legal"
        if piece == "Pawn":
            self.theGrid[position[0]][position[1] + 1].legalNextMove = True
            self.theGrid[position[0] + 1][position[1] + 1].legalNextMove = True
            self.theGrid[position[0] - 1][position[1] + 1].legalNextMove = True
            return

        if piece == "Knight":
            self.theGrid[position[0] + 2][position[1] + 1].legalNextMove = True
            self.theGrid[position[0] + 2][position[1] - 1].legalNextMove = True
            self.theGrid[position[0] - 2][position[1] + 1].legalNextMove = True
            self.theGrid[position[0] - 2][position[1] - 1].legalNextMove = True
            self.theGrid[position[0] + 1][position[1] + 2].legalNextMove = True
            self.theGrid[position[0] + 1][position[1] - 2].legalNextMove = True
            self.theGrid[position[0] - 1][position[1] + 2].legalNextMove = True
            self.theGrid[position[0] - 1][position[1] - 2].legalNextMove = True
            return

        if piece == "King":
            self.theGrid[position[0]][position[1] + 1].legalNextMove = True
            self.theGrid[position[0]][position[1] - 1].legalNextMove = True
            self.theGrid[position[0] + 1][position[1]].legalNextMove = True
            self.theGrid[position[0] - 1][position[1]].legalNextMove = True
            self.theGrid[position[0] + 1][position[1] + 1].legalNextMove = True
            self.theGrid[position[0] + 1][position[1] - 1].legalNextMove = True
            self.theGrid[position[0] - 1][position[1] + 1].legalNextMove = True
            self.theGrid[position[0] - 1][position[1] - 1].legalNextMove = True
            return

        if piece == "Rook":
            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] += 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] -= 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[1] += 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[1] -= 1

            return

        if piece == "Bishop":
            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] += 1
                pos[1] += 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] -= 1
                pos[1] += 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] += 1
                pos[1] -= 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] -= 1
                pos[1] -= 1        
            
            return

        if piece == "Queen":
            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] += 1
                pos[1] += 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] -= 1
                pos[1] += 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] += 1
                pos[1] -= 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] -= 1
                pos[1] -= 1   

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] += 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[0] -= 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[1] += 1

            pos = [position[0] + 1, position[1] + 1]
            while pos[0] < self.size:
                self.theGrid[pos[0]][pos[1]].legalNextMove = True
                pos[1] -= 1    

            return

        return
"""