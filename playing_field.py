import pygame
from pygame.draw import *

# initializing pygame
pygame.font.init()

# check whether font is initialized
# or not
pygame.font.get_init()

# images2
fopf = pygame.image.load('flag.jpg')
# display window parameters
width = 400
height = 600
# border shift parameters
x1 = 4
x2 = 2
y1 = 6
y2 = 2
# main(first) border colour
clr1 = (105, 235, 175)
# second border colour
clr2 = (35, 35, 35)
# Texts colour
clr3 = (255, 255, 255)
# Create a font file by passing font file
# and size of the font
font1 = pygame.font.SysFont("Courier New", 24, bold=True)
font2 = pygame.font.SysFont("Courier New", 28, bold=True)

screen = pygame.display.set_mode((width, height))

pygame.init()


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
    rect(screen, clr2, (182 / 405 * width, 73 / 630 * height, (108 - x1) / 405 * width, (52.5 - y1) / 630 * height),
         2)
    rect(screen, clr2, (181 / 405 * width, 71 / 630 * height, (108 - x2) / 405 * width, (52.5 - y2) / 630 * height),
         1)
    # next figure
    rect(screen, clr1, (291 / 405 * width, 70 / 630 * height, 108 / 405 * width, 52.5 / 630 * height), 5)
    rect(screen, clr2, (293 / 405 * width, 73 / 630 * height, (108 - x1) / 405 * width, (52.5 - y1) / 630 * height),
         2)
    rect(screen, clr2, (292 / 405 * width, 71 / 630 * height, (108 - x2) / 405 * width, (52.5 - y2) / 630 * height),
         1)
    # score
    text1 = font1.render('SCORE', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (290 / 405 * width, 20 / 630 * height)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (185 / 405 * width, 5 / 630 * height, 210 / 405 * width, 62.5 / 630 * height), 5)
    rect(screen, clr2, (187 / 405 * width, 8 / 630 * height, (210 - x1) / 405 * width, (62.5 - y1) / 630 * height),
         2)
    rect(screen, clr2, (186 / 405 * width, 6 / 630 * height, (210 - x2) / 405 * width, (62.5 - y2) / 630 * height),
         1)
    # level
    text1 = font2.render('LV', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (140 / 405 * width, 437 / 630 * height)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (105 / 405 * width, 420 / 630 * height, 70 / 405 * width, 60 / 630 * height), 5)
    rect(screen, clr2, (107 / 405 * width, 424 / 630 * height, (70 - x1) / 405 * width, (60 - y1) / 630 * height),
         2)
    rect(screen, clr2, (106 / 405 * width, 422 / 630 * height, (70 - x2) / 405 * width, (60 - y2) / 630 * height),
         1)
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
    rect(screen, clr2, (182 / 405 * width, 579 / 630 * height, (220 - x1) / 405 * width, (49 - y1) / 630 * height),
         2)
    rect(screen, clr2, (181 / 405 * width, 577 / 630 * height, (220 - x2) / 405 * width, (49 - y2) / 630 * height),
         1)
    # Flag
    screen.blit(fopf, (95 / 405 * width, 565 / 630 * height))
    rect(screen, clr1, (80 / 405 * width, 560 / 630 * height, 95 / 405 * width, 64 / 630 * height), 5)
    rect(screen, clr2, (83 / 405 * width, 563 / 630 * height, (95 - x1) / 405 * width, (63 - y1) / 630 * height), 2)
    rect(screen, clr2, (81 / 405 * width, 561 / 630 * height, (95 - x2) / 405 * width, (63 - y2) / 630 * height), 1)
