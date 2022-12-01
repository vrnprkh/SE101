from pyfirmata import Arduino, util
from stateManagement import BoardProcessor
from tutorials import rookLevel, bishopLevel, queenLevel

from interfacing import sensorProcessing
from gui import guiCombined

import pygame
import time
import random
import itertools

pygame.init()
MIN_THRESHOLD = 0.33
MAX_THRESHOLD = 0.66

running = True

randomLevel = random.choice([rookLevel, bishopLevel, queenLevel])



# boardState =[
#         [randomLevel.allStates[0][0][0][0], randomLevel.allStates[0][0][0][1],0,0],
#         [randomLevel.allStates[0][0][1][0], randomLevel.allStates[0][0][1][1],0,0],
#         [0,0,0,0],
#         [0,0,0,0]
#     ]

boardState = [
    [7,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]

]
print(boardState)
guiCombined.displayGame(boardState, None)

#print("pleaseeeeeeeeeeeeeeeeeeeeeeeeee")

#game = BoardProcessor.BoardProcessor(boardState, randomLevel.allStates)
game = BoardProcessor.BoardProcessor(boardState)
breadboard = Arduino('COM3')
iterator = util.Iterator(breadboard)
iterator.start()
input0 = breadboard.get_pin('a:0:i')
input1 = breadboard.get_pin('a:1:i')

data0 = [0,0,0,0,0,0,0,0]
data1 = [0,0,0,0,0,0,0,0]

list(itertools.product([0, 1], repeat=3))

while running:
    result = -1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False


    if game.csubState == 3:
        print("u win :)")
        break
    
    print("data 0", data0)
    print("data 1", data1)

    time.sleep(.1)
    for i, el in enumerate(list(itertools.product([0, 1], repeat=3))): #list of all combinations of 3 bits
        #print(el)
        breadboard.digital[5].write(el[2])
        breadboard.digital[6].write(el[1])
        breadboard.digital[7].write(el[0]) 

        breadboard.digital[10].write(el[2])
        breadboard.digital[11].write(el[1])
        breadboard.digital[12].write(el[0]) 
        time.sleep(0.1)
        data1[i] = input1.read()
        data0[i] = input0.read()

    if (result == 2) :
        guiCombined.displayGame(game.boardState.state, game.firstCoord)
        print(result)
        continue
    
    formattedMap = sensorProcessing.getSensorMap(data0, data1)
    result = game.update(formattedMap)
    print("sub")
    print(game.csubState)
    print("result")
    print(result)

    if result == 2:
        
        guiCombined.displayGame(game.boardState.state, game.firstCoord)
        time.sleep(5)
        pygame.quit()
        break
    if result == 1:
        print("here")
        #guiCombined.displayGame(game.boardState.getState(), 1)
        guiCombined.displayGame(game.boardState.state, game.firstCoord)
    elif result == -1:
        print("error :( user is dumb")
        guiCombined.displayGame(game.boardState.state, game.firstCoord, False)


    elif result == 0:
        print("pass")
        pass

    
