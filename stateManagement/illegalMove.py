from boardProcessor import BoardProcessor

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
    def isLegal(boardProcessor: BoardProcessor, move):
        #print("hello i am runnigh :)))))))))))))))))))")
        if not boardProcessor.tutorial == None:
            return LegalMoveProcessor.isLegalTutorialMove(move);

        
        return False