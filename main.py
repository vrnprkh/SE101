from pyfirmata import Arduino, util
import stateManagement
#from stateManagement import managerCombined, illegalMove
from tutorials import rookLevel, bishopLevel, queenLevel
from interfacing import sensorProcessing
from gui import guiCombined
import pygame
import time
import random

#print("oh my god")

pygame.init()
MIN_THRESHOLD = 0.33
MAX_THRESHOLD = 0.66

running = True

randomLevel = random.choice([rookLevel, bishopLevel, queenLevel])

boardState =[
        [randomLevel.allStates[0][0][0][0], randomLevel.allStates[0][0][0][1],0,0],
        [randomLevel.allStates[0][0][1][0], randomLevel.allStates[0][0][1][1],0,0],
        [0,0,0,0],
        [0,0,0,0]
    ]
guiCombined.displayGame(boardState, 0)

#print("pleaseeeeeeeeeeeeeeeeeeeeeeeeee")

game = stateManagement.managerCombined.BoardProcessor(boardState, randomLevel.allStates)
breadboard = Arduino('COM3')

iterator = util.Iterator(breadboard)
iterator.start()

input0 = breadboard.get_pin('a:0:i')
input1 = breadboard.get_pin('a:1:i')
input2 = breadboard.get_pin('a:2:i')
input3 = breadboard.get_pin('a:3:i')

while running:
    result = -1
    time.sleep(1)
    print("here 0")
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
    print("here 1")

    if game.csubState == 3:
        print("u win :)")
        break
    
    print ("here 2")
    i0 = input0.read()
    i1 = input1.read()
    i2 = input2.read()
    i3 = input3.read()
    print("here3")

    if (result == 2) :
        guiCombined.displayGame(game.boardState.state, 8)
        print(result)
        continue

    if (i0 and i1 and i2 and i3):
        print(i0, i1, i2, i3)
        
        formattedMap = sensorProcessing.getSensorMap(i0, i1, i2, i3)
        result = game.update(formattedMap)
        print("sub")
        print(game.csubState)
        print("result")
        print(result)

        if result == 2:
            guiCombined.displayGame(game.boardState.state, 8)
            time.sleep(5)
            pygame.quit()
            break
        if result == 1:
            print("here")
            #guiCombined.displayGame(game.boardState.getState(), 1)
            guiCombined.displayGame(game.boardState.state, 8)
        elif result == -1:
            print("error :( user is dumb")
            guiCombined.displayGame(game.boardState.state, 8, False)


        elif result == 0:
            print("pass")
            pass

    
