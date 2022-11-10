from pyfirmata import Arduino, util

board = Arduino('COM3')

iterator = util.Iterator(board)
iterator.start()

input1 = board.get_pin('a:0:i')
input2 = board.get_pin('a:1:i')
input3 = board.get_pin('a:2:i')
input4 = board.get_pin('a:3:i')


while(True):
    i = input1.read()
    print(i)
    board.digital[13].write(0)
    #board.digital[12].write(0)
    if i:
        if i > 0.7:
            board.digital[13].write(1)
        #if i < 0.3:
            #board.digital[12].write(1)

