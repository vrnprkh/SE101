from pyfirmata import Arduino, util
import time


breadboard = Arduino('COM3')

input0 = breadboard.get_pin('a:0:i')

data = [0,0,0,0]
breadboard.digital[12].write(0)
while True:
    breadboard.digital[10].write(0)
    breadboard.digital[11].write(0)
    time.sleep(0.1)
    data[0] = input0.read()


    breadboard.digital[10].write(1)
    breadboard.digital[11].write(0)
    time.sleep(0.1)
    data[1] = input0.read()

    breadboard.digital[10].write(0)
    breadboard.digital[11].write(1)
    time.sleep(0.1)
    data[2] = input0.read()

    breadboard.digital[10].write(1)
    breadboard.digital[11].write(1)
    time.sleep(0.1)
    data[3] = input0.read()

    print(data)
    time.sleep(.6)