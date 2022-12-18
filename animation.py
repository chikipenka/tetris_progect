import sys

import pygame
from pygame.constants import QUIT, K_ESCAPE, KEYDOWN


pygame.init()

FPS = 100

width = 1200
height = 800
screen = pygame.display.set_mode((width, height))



def animation(w1, h1, k, name, position):
    # список для хранения кадров и таймер
    frames = []
    timer = pygame.time.Clock()



