import pygame
from pygame.draw import *

# initializing pygame
pygame.font.init()

# check whether font is initialized
# or not
pygame.font.get_init()

pygame.init()

# display window parameters
w = 400
h = 600
# border shift parameters
x1 = 4
x2 = 2
y1 = 6
y2 = 2
# variable texts (start value)
score = 0
lvl = 0
trt = 0
line = 0
#Nickname
print("Please enter your nickname:")
nick_n = str(input())
# main(first) border colour
clr1 = (105, 235, 175)

# second border colour
clr2 = (35, 35, 35)
# Texts colour
clr3 = (255, 255, 255)

FPS = 30
screen = pygame.display.set_mode((w, h))

# texts
# add background color using RGB values
screen.fill((15, 10, 30))

# Create a font file by passing font file
# and size of the font
font1 = pygame.font.SysFont("Courier New", 24, bold=True)
font2 = pygame.font.SysFont("Courier New", 28, bold=True)


def scorer_draw(scr, clr, font):
    Text = font.render(str(scr), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (290 / 405 * w, 45 / 630 * h)
    screen.blit(Text, TextRect)

def lvlup_draw(lvl, clr, font):
    Text = font.render(str(lvl), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (140 / 405 * w, 460 / 630 * h)
    screen.blit(Text, TextRect)

def trt_draw(trt, clr, font):
    Text = font.render(str(trt), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (128 / 405 * w, 530 / 630 * h)
    screen.blit(Text, TextRect)

def LINE_draw(line, clr, font):
    Text = font.render(str(line), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (235 / 405 * w, 105 / 630 * h)
    screen.blit(Text, TextRect)

def NickName(nn, clr, font):
    Text = font.render(str(nn), True, clr)
    TextRect = Text.get_rect()
    TextRect.center = (290 / 405 * w, 595 / 630 * h)
    screen.blit(Text, TextRect)

def drawer():
    # feild
    rect(screen, clr1, (180 / 405 * w, 125 / 630 * h, 220 / 405 * w, 440 / 630 * h), 5)
    rect(screen, clr2, (182 / 405 * w, 129 / 630 * h, 216 / 405 * w, 434 / 630 * h), 2)
    rect(screen, clr2, (181 / 405 * w, 126 / 630 * h, 218 / 405 * w, 438 / 630 * h), 1)
    # LINE
    text1 = font1.render('LINE', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (234 / 405 * w, 85 / 630 * h)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (180 / 405 * w, 70 / 630 * h, 108 / 405 * w, 52.5 / 630 * h), 5)
    rect(screen, clr2, (182 / 405 * w, 73 / 630 * h, (108 - x1) / 405 * w, (52.5 - y1) / 630 * h), 2)
    rect(screen, clr2, (181 / 405 * w, 71 / 630 * h, (108 - x2) / 405 * w, (52.5 - y2) / 630 * h), 1)
    # next figure
    rect(screen, clr1, (291 / 405 * w, 70 / 630 * h, 108 / 405 * w, 52.5 / 630 * h), 5)
    rect(screen, clr2, (293 / 405 * w, 73 / 630 * h, (108 - x1) / 405 * w, (52.5 - y1) / 630 * h), 2)
    rect(screen, clr2, (292 / 405 * w, 71 / 630 * h, (108 - x2) / 405 * w, (52.5 - y2) / 630 * h), 1)
    # score
    text1 = font1.render('SCORE', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (290 / 405 * w, 20 / 630 * h)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (185 / 405 * w, 5 / 630 * h, 210 / 405 * w, 62.5 / 630 * h), 5)
    rect(screen, clr2, (187 / 405 * w, 8 / 630 * h, (210 - x1) / 405 * w, (62.5 - y1) / 630 * h), 2)
    rect(screen, clr2, (186 / 405 * w, 6 / 630 * h, (210 - x2) / 405 * w, (62.5 - y2) / 630 * h), 1)
    # level
    text1 = font2.render('LV', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (140 / 405 * w, 437 / 630 * h)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (105 / 405 * w, 420 / 630 * h, 70 / 405 * w, 60 / 630 * h), 5)
    rect(screen, clr2, (107 / 405 * w, 424 / 630 * h, (70 - x1) / 405 * w, (60 - y1) / 630 * h), 2)
    rect(screen, clr2, (106 / 405 * w, 422 / 630 * h, (70 - x2) / 405 * w, (60 - y2) / 630 * h), 1)
    # TRT
    text1 = font2.render('TRT', True, clr3)
    textRect1 = text1.get_rect()
    textRect1.center = (127.5 / 405 * w, 502 / 630 * h)
    screen.blit(text1, textRect1)
    rect(screen, clr1, (80 / 405 * w, 485 / 630 * h, 95 / 405 * w, 70 / 630 * h), 5)
    rect(screen, clr2, (83 / 405 * w, 488 / 630 * h, (95 - x1) / 405 * w, (70 - y1) / 630 * h), 2)
    rect(screen, clr2, (81 / 405 * w, 486 / 630 * h, (95 - x2) / 405 * w, (70 - y2) / 630 * h), 1)
    # Nickname
    rect(screen, clr1, (180 / 405 * w, 570 / 630 * h, 220 / 405 * w, 55 / 630 * h), 5)
    rect(screen, clr2, (182 / 405 * w, 573 / 630 * h, (220 - x1) / 405 * w, (55 - y1) / 630 * h), 2)
    rect(screen, clr2, (181 / 405 * w, 571 / 630 * h, (220 - x2) / 405 * w, (55 - y2) / 630 * h), 1)
    # Flag
    rect(screen, clr1, (80 / 405 * w, 560 / 630 * h, 95 / 405 * w, 64 / 630 * h), 5)
    rect(screen, clr2, (83 / 405 * w, 563 / 630 * h, (95 - x1) / 405 * w, (63 - y1) / 630 * h), 2)
    rect(screen, clr2, (81 / 405 * w, 561 / 630 * h, (95 - x2) / 405 * w, (63 - y2) / 630 * h), 1)


clock = pygame.time.Clock()
finished = False

while not finished:
    # texts
    # add background color using RGB values
    screen.fill((15, 10, 30))
    drawer()
    scorer_draw(score, clr3, font1)
    lvlup_draw(lvl, clr3, font2)
    LINE_draw(line, clr3, font1)
    trt_draw(trt, clr3, font2)
    NickName(nick_n, clr3, font1)
    clock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                finished = True

pygame.quit()
