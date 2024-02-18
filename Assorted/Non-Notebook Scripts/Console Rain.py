#!/usr/bin/env python

'''
    This is a console-based application to replicate rain drops in Python
'''

import time
from random import random as rd
import os

RAIN_WIDTH = 27
RAIN_HEIGHT = 45
zdrops = [[' '*5 for _ in range(RAIN_WIDTH)] for _ in range(RAIN_HEIGHT)]

def rain(drops):
    '''
    Shift the existin rain down
    '''
    for i in range(len(drops)-1,0,-1):
        drops[i] = drops[i-1]
    drops[0] = add_rain()
    return drops

def add_rain():
    '''
    Create a new series of the rain (top line)
    '''
    rain_line = [[' ' for x in range(5)] for y in range(RAIN_WIDTH)]
    for i in range(len(rain_line)):
        rain_line[i][round(rd()*4)] = '/'
    for i in range(len(rain_line)):
        rain_line[i] = ''.join(rain_line[i])
    return rain_line

def displays(drops):
    '''
    Displays the rain based on the values in `drops`
    '''
    for i in range(len(drops)):
        print(''.join(drops[i]))

while True:
    os.system('clear')
    zdrops = rain(zdrops)
    displays(zdrops)
    time.sleep(0.1)
