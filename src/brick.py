import pygame as p 

class Brick(): 
    def __init__(self, pos, size, color, font): 
        self.pos = pos 
        self.size = size 
        self.color = color 
        self.icon = '#' if self.color == (100, 100, 100) else '.' 
        self.font = font 
        self.id = 'wall' if self.icon == '#' else 'floor' 
        self.revealed = False 
        
    def render(self, SCREEN, render_mode): 
        if render_mode: 
            p.draw.rect(SCREEN, self.color, (self.pos, self.size)) 
        else: 
            SCREEN.blit(self.font.render(self.icon, 1, self.color), (self.pos, self.size)) 