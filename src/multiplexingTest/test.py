from pyfirmata import Arduino, util
import time
import itertools



breadboard = Arduino('COM5')
iterator = util.Iterator(breadboard)
iterator.start()
input0 = breadboard.get_pin('a:0:i')
input1 = breadboard.get_pin('a:1:i')

data0 = [0,0,0,0,0,0,0,0]
data1 = [0,0,0,0,0,0,0,0]

list(itertools.product([0, 1], repeat=3))

while True:
    print("data 0", data0)
    print("data 1", data1)

    time.sleep(.4)
    for i, el in enumerate(list(itertools.product([0, 1], repeat=3))): #list of all combinations of 3 bits
        #print(el)
        breadboard.digital[5].write(el[2])
        breadboard.digital[6].write(el[1])
        breadboard.digital[7].write(el[0]) 

        breadboard.digital[10].write(el[2])
        breadboard.digital[11].write(el[1])
        breadboard.digital[12].write(el[0]) 
        time.sleep(0.2)
        data1[i] = input1.read()
        data0[i] = input0.read()

        

        

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


    #print(data)
    