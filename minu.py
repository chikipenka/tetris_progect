import pygame
from pathlib import Path

path = Path('dog.jpg')

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

# initializing the constructor
pygame.init()
# display window parameters
width = 400
height = 600
screen = pygame.display.set_mode((width, height))

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


# white color
color = (255, 255, 255)

# light shade of the button
color_light = (170, 170, 170)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text = smallfont.render('quit', True, color)

while True:

    for ev in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        screen.blit(dog_surf, dog_rect)
        draw_button(buttons_list, mouse)

        if ev.type == pygame.QUIT:
            pygame.quit()

            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            if dead_inside(buttons_list[0][1], mouse):
                print("nachat igru")

            if dead_inside(buttons_list[1][1], mouse):
                pygame.quit()

    pygame.display.update()
