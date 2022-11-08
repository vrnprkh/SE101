from pyfirmata import Arduino, util
import time

board = Arduino('COM3')

iterator = util.Iterator(board)
iterator.start()

testInput = board.get_pin('a:0:i')
while(True):
    i = testInput.read()
    board.digital[13].write(0)
    board.digital[12].write(0)
    if i:
        if i > 0.7:
            board.digital[13].write(1)
        if i < 0.3:
            board.digital[12].write(1)
     
