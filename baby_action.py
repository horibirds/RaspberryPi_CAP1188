#!/paty/to/python
# -*- coding: utf-8 -*-
import os 
import smbus
import time
import subprocess
import pygame.mixer

pygame.mixer.init()
pygame.mixer.music.load("./sample.mp3")

i2c = smbus.SMBus(1)
address = 0x29

i2c.write_byte_data(address, 0x00, 0x00)
# Multiple Touch
i2c.write_byte_data(address, 0x2A, 0x0C)
# LED link
i2c.write_byte_data(address, 0x72, 0xff)
# sensitivity
# i2c.write_byte_data(address, 0x1F, 0x3f)
i2c.write_byte_data(address, 0x1F, 0x6f)
# (option) setting LED mode
i2c.write_byte_data(address, 0x81, 0x00)
i2c.write_byte_data(address, 0x82, 0x00)

while(1):
    i2c.write_byte_data(address, 0x00, 0x01)
    i2c.write_byte_data(address, 0x00, 0x00)
    touchval = i2c.read_byte_data(address,0x03)
    print(touchval)
    touch_list = []
    for i in range(8):
        if((touchval >>i) % 2 == 1):
            touch_list.append(i+1)
    print(touch_list)
    time.sleep(0.1)
    if(1 in touch_list):
        if(not pygame.mixer.music.get_busy()):
            pygame.mixer.music.play(1)
