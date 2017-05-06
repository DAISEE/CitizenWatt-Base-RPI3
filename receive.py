#!/usr/bin/env python3

from ina219 import INA219
from ina219 import DeviceRangeError
import time


# file storing data
filename = '/tmp/sensor.log'

SHUNT_OHMS = 0.1
ina = INA219(SHUNT_OHMS)
ina.configure()

while True:

    print("Bus Voltage: %.3f V" % ina.voltage())
    try:
        power = ina.power() / 1000
    except DeviceRangeError as e:
        print(e)
        power = 0
    else:
        print("Power: %.2f W" % power)
        print('')
        FileTemp = open(filename, 'w')
        FileTemp.write(str(power) + ',' + str(time.time()))
        FileTemp.close()

    time.sleep(8)
