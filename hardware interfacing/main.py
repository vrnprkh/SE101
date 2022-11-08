from pyfirmata import Arduino, util

board = Arduino('COM5')
iterator = util.Iterator(board)

iterator.start

board.analog[10].read()
while(True):
    board