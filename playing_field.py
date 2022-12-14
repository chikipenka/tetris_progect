import pygame
from pygame.draw import *

pygame.init()

w = 400
h = 600

FPS = 30
screen = pygame.display.set_mode((w, h))
rect(screen, (235, 235, 235), (180 / 405 * w, 125 / 630 * h, 220 / 405 * w, 440 / 630 * h), 5)  # feild
rect(screen, (235, 235, 235), (180 / 405 * w, 70 / 630 * h, 108 / 405 * w, 52.5 / 630 * h), 4)  # LINE
rect(screen, (235, 235, 235), (291 / 405 * w, 70 / 630 * h, 108 / 405 * w, 52.5 / 630 * h), 4)  # next figure
rect(screen, (235, 235, 235), (185 / 405 * w, 5 / 630 * h, 210 / 405 * w, 62.5 / 630 * h), 4)  # score
rect(screen, (235, 235, 235), (105 / 405 * w, 420 / 630 * h, 70 / 405 * w, 60 / 630 * h), 4)  # level
rect(screen, (235, 235, 235), (80 / 405 * w, 485 / 630 * h, 95 / 405 * w, 70 / 630 * h), 4)  # TRT
rect(screen, (235, 235, 235), (180 / 405 * w, 570 / 630 * h, 220 / 405 * w, 55 / 630 * h), 4)  # Nickname
rect(screen, (235, 235, 235), (80 / 405 * w, 560 / 630 * h, 95 / 405 * w, 65 / 630 * h), 4)  # Flag
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
