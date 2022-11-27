from pyfirmata import Arduino, util
import time
import itertools

breadboard = Arduino('COM3')
iterator = util.Iterator(board)
iterator.start()

input0 = breadboard.get_pin('a:0:i')

data = [0, 0, 0, 0, 0, 0, 0]

list(itertools.product([0, 1], repeat=3))

while True:
    for i, el in enumerate(list(itertools.product([0, 1], repeat=3))): #list of all combinations of 3 bits
        breadboard.digital[10], breadboard.digital[11], breadboard.digital[12] = el
        time.sleep(0.1)
        data[i] = input0.read()

    # breadboard.digital[10].write(0)
    # breadboard.digital[11].write(0)
    # breadboard.digital[12].write(0)
    # time.sleep(0.1)
    # data[0] = input0.read()

    # breadboard.digital[10].write(1)
    # breadboard.digital[11].write(0)
    # breadboard.digital[12].write(0)
    # time.sleep(0.1)
    # data[1] = input0.read()

    # breadboard.digital[10].write(1)
    # breadboard.digital[11].write(1)
    # breadboard.digital[12].write(0)
    # time.sleep(0.1)
    # data[2] = input0.read()

    # breadboard.digital[10].write(1)
    # breadboard.digital[11].write(1)
    # breadboard.digital[12].write(1)
    # time.sleep(0.1)
    # data[3] = input0.read()

    # breadboard.digital[10].write(0)
    # breadboard.digital[11].write(0)
    # breadboard.digital[12].write(0)
    # time.sleep(0.1)
    # data[0] = input0.read()


    # breadboard.digital[10].write(1)
    # breadboard.digital[11].write(0)
    # breadboard.digital[12].write(0)
    # time.sleep(0.1)
    # data[1] = input0.read()

    # breadboard.digital[10].write(1)
    # breadboard.digital[11].write(1)
    # breadboard.digital[12].write(0)
    # time.sleep(0.1)
    # data[2] = input0.read()

    # breadboard.digital[10].write(1)
    # breadboard.digital[11].write(1)
    # breadboard.digital[12].write(1)
    # time.sleep(0.1)
    # data[3] = input0.read()


    print(data)
    time.sleep(.6)