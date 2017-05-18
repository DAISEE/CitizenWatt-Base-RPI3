#!/usr/bin/env python3

import time
import serial

serialArduino = serial.Serial('/dev/ttyACM0', 9600)

# file storing data
filename = '/tmp/sensor.log'

while True:

    # verification if data are received from serial
    while serialArduino.inWaiting() == 0:
        pass

    valueRead = serialArduino.readline()
    valueRead = valueRead.decode("utf-8")
    print(valueRead)

    FileTemp = open(filename, 'w')
    FileTemp.write(valueRead + ',' + str(time.time()))
    FileTemp.close()

    time.sleep(8)
