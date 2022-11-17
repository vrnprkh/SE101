from pyfirmata import Arduino, util
from stateManagement import managerCombined
from tutorials import rookLevel
from interfacing import sensorProcessing
from gui import guiCombined
import pygame
import time
pygame.init()

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


game = managerCombined.BoardProcessor(boardState, rookLevel.allStates)
breadboard = Arduino('COM3')

iterator = util.Iterator(breadboard)
iterator.start()

input0 = breadboard.get_pin('a:0:i')
input1 = breadboard.get_pin('a:1:i')
input2 = breadboard.get_pin('a:2:i')
input3 = breadboard.get_pin('a:3:i')

while running:
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

    if game.csubState == 3:
        print("u win :)")
        break
    i0 = input0.read()
    i1 = input1.read()
    i2 = input2.read()
    i3 = input3.read()

    if (i0 and i1 and i2 and i3):
        #print(i0, i1, i2, i3)
        
        formattedMap = sensorProcessing.getSensorMap(i0, i1, i2, i3)

        result = game.update(formattedMap)
        print("sub")
        print(game.csubState)
        print("result")
        print(result)
        if result == 1:
            print("here")
            #guiCombined.displayGame(game.boardState.getState(), 1)
            guiCombined.displayGame(game.boardState, 2)
        elif result == -1:
            print("error :( user is dumb")
        elif result == 0:
            print("pass")
            pass


    
