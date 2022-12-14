import pygame
from pygame.draw import *
from random import randint

pygame.init()

number_of_balls = 10  # количество шаров
FPS = 100

width = 1200
height = 800
screen = pygame.display.set_mode((width, height))

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



pygame.quit()
