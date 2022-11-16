from pyfirmata import Arduino, util
import stateManagement
from tutorials import rookLevel
from interfacing import sensorProcessing
from gui import guiCombined


MIN_THRESHOLD = 0.33
MAX_THRESHOLD = 0.66

running = True

boardState =[
        [rookLevel.allStates[0][0][0][0], rookLevel.allStates[0][0][0][1],0,0],
        [rookLevel.allStates[0][0][1][0], rookLevel.allStates[0][0][1][1],0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
guiCombined.displayGame(boardState, 2)



while running:
    input0 = float(input("a0"))
    input1 = float(input("a1"))
    input2 = float(input("a2"))
    input3 = float(input("a3"))


    
