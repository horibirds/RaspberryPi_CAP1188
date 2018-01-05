#!/paty/to/python
# -*- coding: utf-8 -*-
import smbus
import time

i2c = smbus.SMBus(1)
address = 0x29

i2c.write_byte_data(address, 0x00, 0x00)
time.sleep(0.2)
i2c.write_byte_data(address, 0x2A, 0x0C)
time.sleep(0.2)
i2c.write_byte_data(address, 0x72, 0xff)
time.sleep(0.2)
# (option) setting LED mode
# i2c.write_byte_data(address, 0x82, 0xff)
# time.sleep(0.2)
# i2c.write_byte_data(address, 0x81, 0x41)
# time.sleep(0.2)
