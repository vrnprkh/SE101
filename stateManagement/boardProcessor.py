from boardState import BoardState
from tutorial import TutorialLevel

# Tutorial data is substates
class BoardProcessor:
    def __init__(self, state, tutorialData):
        self.boardState = BoardState(state)
        self.tutorial = TutorialLevel(tutorialData)
        self.sensorMap = None
    

    


