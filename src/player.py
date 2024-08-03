from src.conf import *
import pygame

class Player:
    def __init__(self):
        self.x       = ((WINDOW_WIDTH / 2) / 2) / 2
        self.y       = (WINDOW_HEIGHT / 2) / 2
        self.angle   = math.pi
        self.rad     = 8

    def draw(self, window):
        pygame.draw.circle(window, 'red', (self.x, self.y), self.rad)