import time
from random import *

import keyboard
import pygame
from pygame.draw import *
from pathlib import Path

pygame.init()
FPS = 30
# initializing pygame
pygame.font.init()
# check whether font is initialized
# or not
pygame.font.get_init()
# display window parameters
width = 400
height = 600
# border shift parameters
x1 = 4
x2 = 2
y1 = 6
y2 = 2
# variable texts (start value)
score = 0
LVL = 0
TRT = 0
Line = 0
# Nickname
print("Please enter your nickname:")
nick_n = 'huy'
# main(first) border colour
clr1 = (105, 235, 175)
# second border colour
clr2 = (35, 35, 35)
# Texts colour
clr3 = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
square_side = 21 / 405 * width
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
GREY = (47,79,79)

COLORS = [[BLUE, RED], [PURPLE, DPURPLE], [RED, YELLOW], [BLUWUE, BLUE], [GREN, GREENY], [PURPLE, PINK], [BLUE, GREEN],
          [MALINA, FGREN]]
types = ['square', 'left_z_figure', 'right_z_figure', 'left_l_figure', 'right_l_figure', 't_figure', 'stick']
orientation = ['straight', 'left', 'right', 'bottom']
print(choice(types))
# texts
# add background color using RGB values
screen.fill((15, 10, 30))
# Create a font file by passing font file
# and size of the font
font1 = pygame.font.SysFont("Courier New", 24, bold=True)
font2 = pygame.font.SysFont("Courier New", 28, bold=True)

#menu
path = Path('dog.jpg')
dog_surf = pygame.image.load(path)
dog_surf = pygame.transform.scale(dog_surf, (400, 600))
dog_rect = dog_surf.get_rect(
    bottomright=(width, height))

buttons_list = []
a = 120
c = int(a/2)
d = 5
width2 = int(width/2)
height2 = int(height/2)
buttons_list.append(('start', (width2-c, height2, a, c), DPURPLE, PURPLE))
buttons_list.append(('quit', ((width2)-c, height2 + a, a, c), DPURPLE, PURPLE))

def draw_button(lict, mouz):
    for but in lict:
        if dead_inside(but[1], mouz):
            pygame.draw.rect(screen, but[3], but[1])
            pygame.draw.rect(screen, WHITE, (but[1][0]-d, but[1][1] - d, a+2*d, c+2*d), d)
        else:
            pygame.draw.rect(screen, but[2], but[1])
            pygame.draw.rect(screen, WHITE, (but[1][0] - d, but[1][1] - d, a + 2 * d, c + 2 * d), d)
        font = pygame.font.SysFont('lobster', 55)
        text = font.render(but[0], False, (0, 0, 0))

        screen.blit(text, (but[1][0]+a/8, but[1][1]+a/10))


def dead_inside(tup, mouz):
    if tup[0] < mouz[0] < tup[0] + tup[2] and tup[1] < mouz[1] < tup[1] + tup[3]:
        return True
    return False

class figures:
    def __init__(self, type, left_side):
        if type == 'square':
            self.type = 'square'
            self.coordinates = [[left_side, -1], [left_side + 1, -1], [left_side, 0], [left_side + 1, 0]]
            self.orientation = 0
        if type == 'left_z_figure':
            self.type = 'left_z_figure'
            self.coordinates = [[left_side, -1], [left_side + 1, -1], [left_side + 1, 0], [left_side + 2, 0]]
            self.orientation = 0
        if type == 'right_z_figure':
            self.type = 'right_z_figure'
            self.coordinates = [[left_side, 0], [left_side + 1, 0], [left_side + 1, -1], [left_side + 2, -1]]
            self.orientation = 0
        if type == 'left_l_figure':
            self.type = 'left_l_figure'
            self.coordinates = [[left_side, -1], [left_side + 1, -1], [left_side + 2, -1], [left_side + 2, 0]]
            self.orientation = 0
        if type == 'right_l_figure':
            self.type = 'right_l_figure'
            self.coordinates = [[left_side, 0], [left_side, -1], [left_side + 1, -1], [left_side + 2, -1]]
            self.orientation = 0
        if type == 't_figure':
            self.type = 't_figure'
            self.coordinates = [[left_side, -1], [left_side + 1, -1], [left_side + 2, -1], [left_side + 1, 0]]
            self.orientation = 0
        if type == 'stick':
            self.type = 'stick'
            self.coordinates = [[left_side, 0], [left_side + 1, 0], [left_side + 2, 0], [left_side + 3, 0]]
            self.orientation = 0

    def __move__(self):
        for i in range(len(self.coordinates)):
            if self.coordinates[i][1] < 19:
                self.coordinates[i][1] += 1

    def __move_right__(self):
        right_move_trigger = True
        for elem in (self.coordinates):
            if elem[0] >= 9:
                right_move_trigger = False
        if right_move_trigger:
            for elem in (self.coordinates):
                elem[0] += 1

    def __move_left__(self):
        left_move_trigger = True
        for elem in (self.coordinates):
            if elem[0] <= 0:
                left_move_trigger = False
        if left_move_trigger:
            for elem in (self.coordinates):
                elem[0] -= 1

    def __move_down__(self):
        for elem in self.coordinates:
            elem[1] += 1


def rotate():
    if event.key == pygame.K_n:
        right_rotate_trigger = True
        if figure_list[-1][0].type == 'stick':
            if figure_list[-1][0].orientation % 4 == 1:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0] + 2][
                    figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 0:
                print(figure_list[-1][0].coordinates[0][0] + 3)
                if collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0]][
                    figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0]][
                    figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0] + 2][
                    figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]

        if figure_list[-1][0].type == 'right_l_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 1][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 1][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0],
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                            figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0]][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0]][
                            figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0],
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0]][
                            figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
        if figure_list[-1][0].type == 'left_l_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[3][0] - 1][
                    figure_list[-1][0].coordinates[3][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0]][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[0][0] + 2][
                            figure_list[-1][0].coordinates[0][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 1,
                                                         figure_list[-1][0].coordinates[0][1] - 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] - 1,
                                                         figure_list[-1][0].coordinates[2][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 2,
                                                         figure_list[-1][0].coordinates[3][1]]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 2][
                    figure_list[-1][0].coordinates[0][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0]][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 1][
                            figure_list[-1][0].coordinates[3][1] - 2] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 1,
                                                         figure_list[-1][0].coordinates[0][1] + 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] - 1,
                                                         figure_list[-1][0].coordinates[2][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0],
                                                         figure_list[-1][0].coordinates[3][1] - 2]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 2][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 3][
                            figure_list[-1][0].coordinates[3][1]] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 1,
                                                         figure_list[-1][0].coordinates[0][1] + 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] + 1,
                                                         figure_list[-1][0].coordinates[2][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 2,
                                                         figure_list[-1][0].coordinates[3][1]]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[0][0]][
                    figure_list[-1][0].coordinates[0][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 2][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 1][
                            figure_list[-1][0].coordinates[3][1] + 2] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 1,
                                                         figure_list[-1][0].coordinates[0][1] - 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] + 1,
                                                         figure_list[-1][0].coordinates[2][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0],
                                                         figure_list[-1][0].coordinates[3][1] + 2]
        if figure_list[-1][0].type == 't_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    t = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = [t[0] - 1, t[1] - 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1]] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    t = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = [t[0] + 1, t[1] - 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    t = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = [t[0] + 1, t[1] + 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1]] == 1:
                    right_rotate_trigger = False
                if right_rotate_trigger:
                    figure_list[-1][0].orientation -= 1
                    t = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = [t[0] - 1, t[1] + 1]

    elif event.key == pygame.K_m:
        # вращение против часовой стрелки
        left_rotate_trigger = True
        if figure_list[-1][0].type == 'stick':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0]][
                    figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                print(figure_list[-1][0].coordinates[0][0] + 3)
                if collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0]][
                    figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0] + 2][
                    figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[
                    figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or collision_list[
                    figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or collision_list[
                    figure_list[-1][0].coordinates[3][0] + 2][
                    figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
        if figure_list[-1][0].type == 'right_l_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                            figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0]][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                    figure_list[-1][0].coordinates[0][1] - 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                            figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0]][
                            figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0],
                                                         figure_list[-1][0].coordinates[0][1] - 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] + 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[0][0] - 1][
                    figure_list[-1][0].coordinates[0][1]] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0]][
                            figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] + 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                    figure_list[-1][0].coordinates[0][1] + 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[1][0]][
                            figure_list[-1][0].coordinates[1][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 2][
                            figure_list[-1][0].coordinates[3][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0],
                                                         figure_list[-1][0].coordinates[0][1] + 2]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0] - 1,
                                                         figure_list[-1][0].coordinates[1][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 1,
                                                         figure_list[-1][0].coordinates[3][1] - 1]

        left_rotate_trigger = True
        if figure_list[-1][0].type == 'left_l_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 2][
                    figure_list[-1][0].coordinates[0][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0]][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 1][
                            figure_list[-1][0].coordinates[3][1] - 2] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 1,
                                                         figure_list[-1][0].coordinates[0][1] + 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] - 1,
                                                         figure_list[-1][0].coordinates[2][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0],
                                                         figure_list[-1][0].coordinates[3][1] - 2]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[0][0] + 2][
                    figure_list[-1][0].coordinates[0][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0]][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] - 1][
                            figure_list[-1][0].coordinates[3][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 1,
                                                         figure_list[-1][0].coordinates[0][1] - 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] - 1,
                                                         figure_list[-1][0].coordinates[2][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 2,
                                                         figure_list[-1][0].coordinates[3][1]]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[0][0]][
                    figure_list[-1][0].coordinates[0][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 2][
                            figure_list[-1][0].coordinates[2][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 1][
                            figure_list[-1][0].coordinates[3][1] + 2] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 1,
                                                         figure_list[-1][0].coordinates[0][1] - 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] + 1,
                                                         figure_list[-1][0].coordinates[2][1] + 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0],
                                                         figure_list[-1][0].coordinates[3][1] + 2]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[0][0]][
                    figure_list[-1][0].coordinates[0][1] + 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[2][0] + 2][
                            figure_list[-1][0].coordinates[2][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 3][
                            figure_list[-1][0].coordinates[3][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 1,
                                                         figure_list[-1][0].coordinates[0][1] + 1]
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0] + 1,
                                                         figure_list[-1][0].coordinates[2][1] - 1]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 2,
                                                         figure_list[-1][0].coordinates[3][1]]

        if figure_list[-1][0].type == 't_figure':
            if figure_list[-1][0].orientation % 4 == 0:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    t = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = [t[0] + 1, t[1] - 1]
            elif figure_list[-1][0].orientation % 4 == 1:
                if collision_list[figure_list[-1][0].coordinates[1][0]][
                    figure_list[-1][0].coordinates[1][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    t = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = [t[0] - 1, t[1] - 1]
            elif figure_list[-1][0].orientation % 4 == 2:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    t = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = [t[0] - 1, t[1] + 1]
            elif figure_list[-1][0].orientation % 4 == 3:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 2][
                    figure_list[-1][0].coordinates[1][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    t = figure_list[-1][0].coordinates[0]
                    figure_list[-1][0].coordinates[0] = figure_list[-1][0].coordinates[3]
                    figure_list[-1][0].coordinates[3] = figure_list[-1][0].coordinates[2]
                    figure_list[-1][0].coordinates[2] = [t[0] + 1, t[1] + 1]

    if event.key == pygame.K_m or event.key == pygame.K_n:
        left_rotate_trigger = True
        if figure_list[-1][0].type == 'left_z_figure':
            if figure_list[-1][0].orientation % 2 == 0:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] - 1] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[0][0] + 1][
                            figure_list[-1][0].coordinates[0][1] + 1] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0],
                                                         figure_list[-1][0].coordinates[2][1] - 2]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] - 2,
                                                         figure_list[-1][0].coordinates[3][1]]
            else:
                if collision_list[figure_list[-1][0].coordinates[2][0] + 1][
                    figure_list[-1][0].coordinates[2][1] + 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[3][0] + 3][
                            figure_list[-1][0].coordinates[3][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[2] = [figure_list[-1][0].coordinates[2][0],
                                                         figure_list[-1][0].coordinates[2][1] + 2]
                    figure_list[-1][0].coordinates[3] = [figure_list[-1][0].coordinates[3][0] + 2,
                                                         figure_list[-1][0].coordinates[3][1]]
        if figure_list[-1][0].type == 'right_z_figure':
            if figure_list[-1][0].orientation % 2 == 0:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] - 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[0][0] + 3][
                            figure_list[-1][0].coordinates[0][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] + 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0],
                                                         figure_list[-1][0].coordinates[1][1] - 2]
            else:
                if collision_list[figure_list[-1][0].coordinates[1][0] + 1][
                    figure_list[-1][0].coordinates[1][1] + 2] == 1 or \
                        collision_list[figure_list[-1][0].coordinates[0][0] - 1][
                            figure_list[-1][0].coordinates[0][1]] == 1:
                    left_rotate_trigger = False
                if left_rotate_trigger:
                    figure_list[-1][0].orientation += 1
                    figure_list[-1][0].coordinates[0] = [figure_list[-1][0].coordinates[0][0] - 2,
                                                         figure_list[-1][0].coordinates[0][1]]
                    figure_list[-1][0].coordinates[1] = [figure_list[-1][0].coordinates[1][0],
                                                         figure_list[-1][0].coordinates[1][1] + 2]


def kvadratic_blik(x, y, a, i, color_type):
    ''' i - номер в массиве, который зависит от уровня
    и x пусть меняется от xx до xx+ширина игрового поля
    y строго от yy
    '''
    colors = COLORS[i]
    d = int(a // 10)
    pygame.draw.rect(screen, colors[color_type], (x, y, a, a))
    pygame.draw.rect(screen, BLACK, (x, y, a, a), d)
    pygame.draw.rect(screen, WHITE, (x + d + d, y + d + d, d, d))
    pygame.draw.rect(screen, WHITE, (x + 2 * d + d, y + d + d, d, d))
    pygame.draw.rect(screen, WHITE, (x + d + d, y + 2 * d + d, d, d))
    pygame.draw.rect(screen, WHITE, (x + d, y + d, d, d))
    pygame.draw.rect(screen, WHITE, (x + d + d, y + d + d, d, d))
    pygame.draw.rect(screen, WHITE, (x + 2 * d + d, y + d + d, d, d))
    pygame.draw.rect(screen, WHITE, (x + d + d, y + 2 * d + d, d, d))
    pygame.draw.rect(screen, WHITE, (x + d, y + d, d, d))


def kvadratic_bigblik(x, y, a, i):
    ''' i - номер в массиве, который зависит от уровня'''
    colors = COLORS[i]
    d = int(a // 10)
    pygame.draw.rect(screen, colors[0], (x, y, a, a))
    pygame.draw.rect(screen, BLACK, (x, y, a, a), d)
    pygame.draw.rect(screen, WHITE, (x + d + d, y + d + d, a - 2 * d - 2 * d, a - 2 * d - 2 * d))
    pygame.draw.rect(screen, WHITE, (x + d, y + d, d, d))
    pygame.draw.rect(screen, BLACK, (x, y, a, a), 2)
    pygame.draw.rect(screen, WHITE, (x + a / 10 + 5, y + a / 10 + 5, a - a / 5 - 10, a - a / 5 - 10))
    pygame.draw.rect(screen, WHITE, (x + 5, y + 5, a / 10, a / 10))

    pygame.draw.rect(screen, WHITE, (x + d + d, y + d + d, a - 2 * d - 2 * d, a - 2 * d - 2 * d))
    pygame.draw.rect(screen, WHITE, (x + d, y + d, d, d))


# a - ребро квадратика, нужно будет определить и поменять
# xx, yy - координаты  левого верхнего угла игрового окнa
def kvadratic(n, m, a, xx, yy):
    """ x_1, y_1 - координаты левого верхнего угла,
     n, m - координаты квадратика в игровом поле, выраженные через число квадратиков
     x, y - координаты квадратика в игровом окне"""
    x = xx + n * a
    y = yy + m * a
    return x, y


def scorer_draw(scr, clr, font):
    """"функция отрисовки очков игрока в поле score
        функция принимает три параметра: количество очков, цвет текста и шрифт текста
        функция выводит на экран в нужной ячейке количество очков заданым цветом и шрифтом"""
    Text = font.render(str(scr), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (290 / 405 * width, 45 / 630 * height)
    screen.blit(Text, TextRect)


def lvlup_draw(lvl, clr, font):
    """"функция отрисовки уровня игрока в поле lvl
        функция принимает три параметра: уровень игрока, цвет текста и шрифт текста
        функция выводит на экран в нужной ячейке уровень игрока заданым цветом и шрифтом"""
    Text = font.render(str(lvl), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (140 / 405 * width, 460 / 630 * height)
    screen.blit(Text, TextRect)


def trt_draw(trt, clr, font):
    """"функция отрисовки параметра trt в поле TRT
        функция принимает три параметра: процент линий зачищеных тетрисом(trt), цвет текста и шрифт текста
        функция выводит на экран в нужной ячейке показатель trt заданым цветом и шрифтом"""
    Text = font.render(str(trt), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (128 / 405 * width, 530 / 630 * height)
    screen.blit(Text, TextRect)


def line_draw(line, clr, font):
    """"функция отрисовки количества линий зачищеных игроком (или тетрисом) в поле LINE
        функция принимает три параметра: количества линий зачищеных игроком, цвет текста и шрифт текста
        функция выводит на экран в нужной ячейке количества линий зачищеных игроком заданым цветом и шрифтом"""
    Text = font.render(str(line), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (235 / 405 * width, 105 / 630 * height)
    screen.blit(Text, TextRect)


def nick_name(nn, clr, font):
    """"функция отрисовки никнейма в поле
        функция принимает три параметра: никнейм, цвет текста и шрифт текста
        функция выводит на экран в нужной ячейке никнейм заданым цветом и шрифтом"""
    Text = font.render(str(nn), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (290 / 405 * width, 600 / 630 * height)
    screen.blit(Text, TextRect)


def drawer():
    """"функция отрисовки игрового поля"""
    # feild
    rect(screen, clr1, (180 / 405 * width, 125 / 630 * height, 220 / 405 * width, 446 / 630 * height), 5)
    rect(screen, clr2, (182 / 405 * width, 129 / 630 * height, 216 / 405 * width, 440 / 630 * height), 2)
    rect(screen, clr2, (181 / 405 * width, 126 / 630 * height, 218 / 405 * width, 444 / 630 * height), 1)
    # LINE
    text1 = font1.render('LINE', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (234 / 405 * width, 85 / 630 * height)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (180 / 405 * width, 70 / 630 * height, 108 / 405 * width, 52.5 / 630 * height), 5)
    rect(screen, clr2, (182 / 405 * width, 73 / 630 * height, (108 - x1) / 405 * width, (52.5 - y1) / 630 * height), 2)
    rect(screen, clr2, (181 / 405 * width, 71 / 630 * height, (108 - x2) / 405 * width, (52.5 - y2) / 630 * height), 1)
    # next figure
    rect(screen, clr1, (291 / 405 * width, 70 / 630 * height, 108 / 405 * width, 52.5 / 630 * height), 5)
    rect(screen, clr2, (293 / 405 * width, 73 / 630 * height, (108 - x1) / 405 * width, (52.5 - y1) / 630 * height), 2)
    rect(screen, clr2, (292 / 405 * width, 71 / 630 * height, (108 - x2) / 405 * width, (52.5 - y2) / 630 * height), 1)
    # score
    text1 = font1.render('SCORE', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (290 / 405 * width, 20 / 630 * height)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (185 / 405 * width, 5 / 630 * height, 210 / 405 * width, 62.5 / 630 * height), 5)
    rect(screen, clr2, (187 / 405 * width, 8 / 630 * height, (210 - x1) / 405 * width, (62.5 - y1) / 630 * height), 2)
    rect(screen, clr2, (186 / 405 * width, 6 / 630 * height, (210 - x2) / 405 * width, (62.5 - y2) / 630 * height), 1)
    # level
    text1 = font2.render('LV', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (140 / 405 * width, 437 / 630 * height)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (105 / 405 * width, 420 / 630 * height, 70 / 405 * width, 60 / 630 * height), 5)
    rect(screen, clr2, (107 / 405 * width, 424 / 630 * height, (70 - x1) / 405 * width, (60 - y1) / 630 * height), 2)
    rect(screen, clr2, (106 / 405 * width, 422 / 630 * height, (70 - x2) / 405 * width, (60 - y2) / 630 * height), 1)
    # TRT
    text1 = font2.render('TRT', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (127.5 / 405 * width, 502 / 630 * height)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (80 / 405 * width, 485 / 630 * height, 95 / 405 * width, 70 / 630 * height), 5)
    rect(screen, clr2, (83 / 405 * width, 488 / 630 * height, (95 - x1) / 405 * width, (70 - y1) / 630 * height), 2)
    rect(screen, clr2, (81 / 405 * width, 486 / 630 * height, (95 - x2) / 405 * width, (70 - y2) / 630 * height), 1)
    # Nickname
    rect(screen, clr1, (180 / 405 * width, 576 / 630 * height, 220 / 405 * width, 49 / 630 * height), 5)
    rect(screen, clr2, (182 / 405 * width, 579 / 630 * height, (220 - x1) / 405 * width, (49 - y1) / 630 * height), 2)
    rect(screen, clr2, (181 / 405 * width, 577 / 630 * height, (220 - x2) / 405 * width, (49 - y2) / 630 * height), 1)
    # Flag
    rect(screen, clr1, (80 / 405 * width, 560 / 630 * height, 95 / 405 * width, 64 / 630 * height), 5)
    rect(screen, clr2, (83 / 405 * width, 563 / 630 * height, (95 - x1) / 405 * width, (63 - y1) / 630 * height), 2)
    rect(screen, clr2, (81 / 405 * width, 561 / 630 * height, (95 - x2) / 405 * width, (63 - y2) / 630 * height), 1)


def is_bad_column(A):
    column_counter = 0
    column_trigger = True
    column_set = set()
    for j in range(len(A[0])):
        if j != len(A[0]) - 4:
            for i in range(len(A)):
                if A[i][j] == 0:
                    column_trigger = False
            if column_trigger:
                column_counter += 1
                column_set.add(j)
            column_trigger = True
    return column_counter, column_set


def fix_bad_column(A, B):
    for elem in B:
        for i in range(1, len(A) - 1):
            A[i][elem] = 0
    return A

nfl_t = 0
figure_list = list()
next_figure_list = list()
static_figure_list = list()
clock = pygame.time.Clock()
finished = False
time_counter = 0
collision_list = [[0] * 24 for i in range(12)]
for i in range(len(collision_list)):
    for j in range(len(collision_list[i])):
        if j == len(collision_list[i]) - 4 or i == 0 or i == len(collision_list) - 1:
            collision_list[i][j] = 1
fast_move_down_trigger = False
fast_move_down_tick = 0
fast_move_left_tick = 0
fast_move_right_tick = 0
previous_statick_figure_list_len = 0
while not finished:
    current_statick_figure_list_len = len(static_figure_list)
    drawer()
    scorer_draw(score, clr3, font1)
    lvlup_draw(LVL, clr3, font2)
    line_draw(Line, clr3, font1)
    trt_draw(TRT, clr3, font2)
    nick_name(nick_n, clr3, font1)
    clock.tick(FPS)
    time_counter += 1
    level_color = 1
    if time_counter == 20:
        current_type = choice(types)
        if current_type == 'square':
            figure_list.append([figures('square', randint(0, 8)), randint(0, 2)])
            next_figure_list.append([figures('square', randint(0, 8)), randint(0, 2)])
        elif current_type == 'stick':
            figure_list.append([figures('stick', randint(0, 6)), randint(0, 2)])
            next_figure_list.append([figures('stick', randint(0, 6)), randint(0, 2)])
        else:
            figure_list.append([figures(current_type, randint(0, 7)), randint(0, 2)])
            next_figure_list.append([figures(current_type, randint(0, 7)), randint(0, 2)])
    if time_counter % 10 == 0:
        for fig in figure_list:
            move_trigger = True
            add_trigger = False
            touch_time = 0
            if nfl_t > 0:
                next_figure_list.remove(fig)
                nfl_t = 0
            for square in fig[0].coordinates:
                if collision_list[square[0] + 1][square[1] + 1] == 1:
                    move_trigger = False
                    nfl_t = 1
            if move_trigger:
                fig[0].__move__()
            else:
                figure_list.remove(fig)
                static_figure_list.append(fig)
                add_trigger = True
                touch_time = time.time()
                for square in fig[0].coordinates:
                    collision_list[square[0] + 1][square[1]] = 1
            if add_trigger:
                add_trigger = False
                while time.time() - touch_time < 0.2:
                    pass
                current_type = choice(types)
                if current_type == 'square':
                    figure_list.append(next_figure_list[0])
                    next_figure_list.append([figures('square', randint(0, 8)), randint(0, 2)])
                elif current_type == 'stick':
                    figure_list.append(next_figure_list[0])
                    next_figure_list.append([figures('stick', randint(0, 6)), randint(0, 2)])
                else:
                    figure_list.append(next_figure_list[0])
                    next_figure_list.append([figures(current_type, randint(0, 7)), randint(0, 2)])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                finished = True
            if event.key == pygame.K_DOWN:
                fast_move_down_trigger = False
        elif event.type == pygame.KEYDOWN:
            rotate()
            if event.key == pygame.K_LEFT:
                fast_move_left_trigger = True
                fast_move_left_tick = time.time()
                left_time_tick = time.time()
                move_left_trigger2 = True
                for square in figure_list[-1][0].coordinates:
                    if collision_list[square[0]][square[1]] == 1:
                        move_left_trigger2 = False
                if move_left_trigger2:
                    figure_list[-1][0].__move_left__()
            if event.key == pygame.K_RIGHT:
                fast_move_right_tick = time.time()
                move_right_trigger2 = True
                for square in figure_list[-1][0].coordinates:
                    if collision_list[square[0] + 2][square[1]] == 1:
                        move_right_trigger2 = False
                if move_right_trigger2:
                    figure_list[-1][0].__move_right__()
            figure_list_len = len(figure_list)
            if event.key == pygame.K_DOWN:
                fast_move_down_trigger = True
                fast_move_down_tick = time.time()
    if previous_statick_figure_list_len != current_statick_figure_list_len:
        fast_move_down_tick = time.time()
    if keyboard.is_pressed('down'):
        if time.time() - fast_move_down_tick > 0.2 and fast_move_down_tick != 0:
            move_down_trigger2 = True
            for square in figure_list[-1][0].coordinates:
                if collision_list[square[0] + 1][square[1] + 1] == 1:
                    move_down_trigger2 = False
            if move_down_trigger2:
                figure_list[-1][0].__move_down__()
    if previous_statick_figure_list_len != current_statick_figure_list_len:
        fast_move_left_tick = time.time()
    if keyboard.is_pressed('left'):
        if time.time() - fast_move_left_tick > 0.2 and fast_move_left_tick != 0:
            move_down_trigger2 = True
            for square in figure_list[-1][0].coordinates:
                if collision_list[square[0]][square[1]] == 1:
                    move_down_trigger2 = False
            if move_down_trigger2:
                figure_list[-1][0].__move_left__()
    if previous_statick_figure_list_len != current_statick_figure_list_len:
        fast_move_right_tick = time.time()
    if keyboard.is_pressed('right'):
        if time.time() - fast_move_right_tick > 0.2 and fast_move_right_tick != 0:
            move_down_trigger2 = True
            for square in figure_list[-1][0].coordinates:
                if collision_list[square[0] + 2][square[1]] == 1:
                    move_down_trigger2 = False
            if move_down_trigger2:
                figure_list[-1][0].__move_right__()
    # for i in range(len(collision_list)):
    # print(collision_list[i])
    full_string_counter, full_string_set = is_bad_column(collision_list)
    delete_full_string_list = list()
    for fig in static_figure_list:
        for square in fig[0].coordinates:
            for full_string in full_string_set:
                if square[1] == full_string:
                    delete_full_string_list.append([square[0], square[1]])
    for i in range(len(delete_full_string_list)):
        pops = 0
        for fig in static_figure_list:
            for j in range(len(fig[0].coordinates) - pops):
                j = j - pops
                if fig[0].coordinates[j][0] == delete_full_string_list[i][0] and fig[0].coordinates[j][1] == \
                        delete_full_string_list[i][1]:
                    fig[0].coordinates.pop(j)
                    pops += 1
    fix_bad_column(collision_list, full_string_set)

    full_string_list = list()
    for elem in full_string_set:
        full_string_list.append(elem)
    if len(full_string_set) > 0:
        print(full_string_list)
    full_string_list.sort()
    for i in range(len(full_string_list)):
        for j in range(len(static_figure_list)):
            for square in static_figure_list[j][0].coordinates:
                if square[1] < full_string_list[i]:
                    square[1] += 1
    collision_list = [[0] * 24 for i in range(12)]
    for i in range(len(collision_list)):
        for j in range(len(collision_list[i])):
            if j == len(collision_list[i]) - 4 or i == 0 or i == len(collision_list) - 1:
                collision_list[i][j] = 1
    for i in range(len(static_figure_list)):
        for square in static_figure_list[i][0].coordinates:
            collision_list[square[0]+1][square[1]] = 1
    full_string_set = set()
    for fig in figure_list:
        for i in range(len(fig[0].coordinates)):
            x_for_each_square, y_for_each_square = kvadratic(fig[0].coordinates[i][0], fig[0].coordinates[i][1],
                                                             square_side, 185 / 405 * width, 130 / 630 * height)
            if fig[0].coordinates[i][1] >= 0:
                if fig[1] == 0:
                    kvadratic_blik(x_for_each_square, y_for_each_square, square_side, level_color, 0)
                elif fig[1] == 1:
                    kvadratic_blik(x_for_each_square, y_for_each_square, square_side, level_color, 1)
                else:
                    kvadratic_bigblik(x_for_each_square, y_for_each_square, square_side, level_color)
    for fig in static_figure_list:
        for i in range(len(fig[0].coordinates)):
            x_for_each_square, y_for_each_square = kvadratic(fig[0].coordinates[i][0], fig[0].coordinates[i][1],
                                                             square_side, 185 / 405 * width, 130 / 630 * height)
            if fig[0].coordinates[i][1] >= 0:
                if fig[1] == 0:
                    kvadratic_blik(x_for_each_square, y_for_each_square, square_side, level_color, 0)
                elif fig[1] == 1:
                    kvadratic_blik(x_for_each_square, y_for_each_square, square_side, level_color, 1)
                else:
                    kvadratic_bigblik(x_for_each_square, y_for_each_square, square_side, level_color)
    previous_statick_figure_list_len = current_statick_figure_list_len
    pygame.display.update()
    screen.fill((15, 10, 30))
print('Huy')
pygame.quit()