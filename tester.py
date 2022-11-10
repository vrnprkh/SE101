from pyfirmata import Arduino, util
import time
board = Arduino('COM3')

iterator = util.Iterator(board)
iterator.start()

input0 = board.get_pin('a:0:i')
input1 = board.get_pin('a:1:i')
input2 = board.get_pin('a:2:i')
input3 = board.get_pin('a:3:i')


while True:
    i0 = input0.read()
    i1 = input1.read()
    i2 = input2.read()
    i3 = input3.read()
    board.digital[10].write(0)
    board.digital[11].write(0)
    board.digital[12].write(0)
    board.digital[13].write(0)
    if (i0 and i1 and i2 and i3)
        if abs(0.5 - i0) > 0.2:
            board.digital[10].write(1)
        if abs(0.5 - i1) > 0.2:
            board.digital[11].write(1)
        if abs(0.5 - i2) > 0.2:
            board.digital[12].write(1)
        if abs(0.5 - i3) > 0.2:
            board.digital[13].write(1)
