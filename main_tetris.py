import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 100

width = 1200
height = 800
screen = pygame.display.set_mode((width, height))

BLUE = (65, 105, 225)
RED = (139, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (102, 11, 171)
DPURPLE = (90, 1, 90)
YELLOW = (219, 165, 38)
BLUWUE = (91, 221, 230)
GREN = (4, 115, 15)
GREENY = (125, 223, 96)
PINK = (245, 125, 245)
GREEN = (0, 255, 26)
FGREN = (35, 185, 105)
MALINA = (185, 35, 130)
COLORS = [[BLUE, RED], [PURPLE, DPURPLE], [RED, YELLOW], [BLUWUE, BLUE], [GREN, GREENY], [PURPLE, PINK], [BLUE, GREEN], [MALINA, FGREN]]
xx, yy = 100, 100 # вставить реальные значения координат левого верхнего угла игрового поля

types = ['square', 'left_z_figure', 'right_z_figure', 'left_l_figure', 'right_l_figure', 't_figure', 'stick']
orientation = ['straight', 'left', 'right', 'bottom']


class figures:
    def __init__(self, type, left_side):
        if type == 'square':
            self.coordinates = [[left_side, -1], [left_side + 1, -1], [left_side, 0], [left_side + 1, 0]]
        if type == 'left_z_figure':
            self.coordinates = [[left_side, -1], [left_side + 1, -1], [left_side + 1, 0], [left_side + 2, 0]]
        if type == 'right_z_figure':
            self.coordinates = [[left_side, 0], [left_side + 1, 0], [left_side + 1, -1], [left_side + 2, -1]]
        if type == 'left_l_figure':
            self.coordinates = [[left_side, 0], [left_side + 1, 0], [left_side + 1, -1], [left_side + 1, -2]]
        if type == 'right_l_figure':
            self.coordinates = [[left_side, 0], [left_side + 1, 0], [left_side, -1], [left_side, -2]]
        if type == 't_figure':
            self.coordinates = [[left_side, -1], [left_side + 1, -1], [left_side + 2, -1], [left_side + 1, 0]]
        if type == 'stick':
            self.coordinates = [[left_side, -3], [left_side, -2], [left_side, -1], [left_side, 0]]

    def __move__(self):
        for i in range(len(self.coordinates)):
            if self.coordinates[i][1] < 19:
                self.coordinates[i][1] += 1

    def __move_right__(self):
        for i in range(len(self.coordinates)):
            if self.coordinates[i][0] < 9:
                self.coordinates[i][0] += 1

    def __move_left__(self):
        for i in range(len(self.coordinates)):
            if self.coordinates[i][0] > 0:
                self.coordinates[i][0] += 1


def kvadratic_blik(x, y, a, i):
    ''' i - номер в массиве, который зависит от уровня
    и x пусть меняется от xx до xx+ширина игрового поля
    y строго от yy
    '''
    colors = COLORS[i]
    pygame.draw.rect(screen, colors[randint(0,1)], (x, y, a, a))
    pygame.draw.rect(screen, BLACK, (x, y, a, a), 5)
    pygame.draw.rect(screen, WHITE, (x+a/10+5, y+a/10+5, a/10, a/10))
    pygame.draw.rect(screen, WHITE, (x+2*a/10+5, y+a/10+5, a/10, a/10))
    pygame.draw.rect(screen, WHITE, (x+a/10+5, y+2*a/10+5, a/10, a/10))
    pygame.draw.rect(screen, WHITE, (x+5, y+5, a/10, a/10))

def kvadratic_bigblik(x, y, a, i):
    ''' i - номер в массиве, который зависит от уровня'''
    colors = COLORS[i]
    pygame.draw.rect(screen, colors[0], (x, y, a, a))
    pygame.draw.rect(screen, BLACK, (x, y, a, a), 5)
    pygame.draw.rect(screen, WHITE, (x + a / 10 + 5, y + a / 10 + 5, a - a / 5 - 10, a - a / 5 - 10))
    pygame.draw.rect(screen, WHITE, (x + 5, y + 5, a / 10, a / 10))


# a - ребро квадратика, нужно будет определить и поменять
# xx, yy - координаты  левого верхнего угла игрового окнa
def kvadratic(n, m, a):
    """ xx, yy - координаты левого верхнего угла игрового поля,
     n, m - координаты квадратика в игровом поле, выраженные через число квадратиков
     x, y - координаты квадратика в игровом окне"""
    x = xx + n*a
    y = yy + m*a

    return x, y

print('Huy')
pygame.quit()
