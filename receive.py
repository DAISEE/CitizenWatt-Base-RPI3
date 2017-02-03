#!/usr/bin/env python3

import sys
import time
from pySmartPlugSmpB16 import SmartPlug, btle

addr = "" #to update

# connect to the plug (BLE connect)
try:
    plug = SmartPlug(addr)
except btle.BTLEException as err:
    sys.exit('error when connect to %s (code %d)' % (addr, err.code))

# file storing data
filename = '/tmp/sensor.log'

while True:

    try:
        (state, power, voltage) = plug.status_request()
    except btle.BTLEException as err:
        sys.exit('error when requesting stat to plug %s (code %d)' % (addr, err.code))
    print('plug power   = %d W' % power)

    # for debug
    # print(size, ''.join('{:02x}'.format(x) for x in receive_payload))
    # print(receive_payload)
    # print('')
    FileTemp = open(filename, 'w')
    FileTemp.write(str(power) + ',' + str(time.time()))
    FileTemp.close()
