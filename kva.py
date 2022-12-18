import pygame
from random import randint

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
xx, yy = 100, 100 # вставить реальные значения

def kvadratic_blik(x, y, a, i):
    ''' i - номер в массиве, который зависит от уровня
    и x пусть меняется от xx до xx+ширина игрового окна
    '''
    if y>=yy:
        colors = COLORS[i]
        pygame.draw.rect(screen, colors[randint(0,1)], (x, y, a, a))
        pygame.draw.rect(screen, BLACK, (x, y, a, a), 5)
        pygame.draw.rect(screen, WHITE, (x+a/10+5, y+a/10+5, a/10, a/10))
        pygame.draw.rect(screen, WHITE, (x+2*a/10+5, y+a/10+5, a/10, a/10))
        pygame.draw.rect(screen, WHITE, (x+a/10+5, y+2*a/10+5, a/10, a/10))
        pygame.draw.rect(screen, WHITE, (x+5, y+5, a/10, a/10))
    elif yy>y>(yy-a):
        colors = COLORS[i]
        pygame.draw.rect(screen, colors[randint(0, 1)], (x, yy, a, a-(yy-y)))
        pygame.draw.rect(screen, BLACK, (x, y, a, a), 5)
        if y>=yy-a/10:
            pygame.draw.rect(screen, WHITE, (x + 5, y + 5, a / 10, a / 10))
        pygame.draw.rect(screen, WHITE, (x + a / 10 + 5, y + a / 10 + 5, a / 10, a / 10))
        pygame.draw.rect(screen, WHITE, (x + 2 * a / 10 + 5, y + a / 10 + 5, a / 10, a / 10))
        pygame.draw.rect(screen, WHITE, (x + a / 10 + 5, y + 2 * a / 10 + 5, a / 10, a / 10))
        pygame.draw.rect(screen, WHITE, (x + 5, y + 5, a / 10, a / 10))
def kvadratic_bigblik(x, y, a, i):
    ''' i - номер в массиве, который зависит от уровня'''
    colors = COLORS[i]
    pygame.draw.rect(screen, colors[0], (x, y, a, a))
    pygame.draw.rect(screen, BLACK, (x, y, a, a), 5)
    pygame.draw.rect(screen, WHITE, (x + a / 10 + 5, y + a / 10 + 5, a - a / 5 - 10, a - a / 5 - 10))
    pygame.draw.rect(screen, WHITE, (x + 5, y + 5, a / 10, a / 10))