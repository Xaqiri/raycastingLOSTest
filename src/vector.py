import pygame as p 
from math import * 

class Vector(): 
    def __init__(self, x, y, range, direction=(1, 0)): 
        self.start = (x, y) 
        self.direction = direction 
        self.range = range 
        self.end = (self.direction[0]*self.range, self.direction[1]*self.range) 
        self.length = sqrt((self.end[0]-self.start[0])**2 + (self.end[1]-self.start[1])**2) 

    def update(self, start): 
        self.start = start 

    def render(self, SCREEN, color): 
        p.draw.line(SCREEN, color, self.start, 
        (self.start[0]+self.end[0], self.start[1]+self.end[1]), 2) 
