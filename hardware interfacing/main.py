from pyfirmata import *
import time

board = pyfirmata.Arduino('COM5')

while True:
    board.iterate()
    input7 = board.get_pin('d:7:i')
    while(input7.read() == 1):
        board.digital[13].write(1)
        time.sleep(1)
        board.digital[13].write(0)
        time.sleep(1)



"""




"""