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
input_box = []
a = 120
c = int(a/2)
c_1 = int(2.4*a/2)
d = 5
default = '1'
default_name = 'guest'
width2 = int(width/2)
height2 = int(height/2)
buttons_list.append(('start', (width2-c, height2+2*c, a, c), DPURPLE, PURPLE))
buttons_list.append(('quit', ((width2)-c, height2+3*c, a, c), DPURPLE, PURPLE))
buttons_list.append((default_name, (width2-c_1, height2, 2.4*a, c), DPURPLE, PURPLE))
buttons_list.append((default, (width2-c_1, height2+c, 2.4*a, c), DPURPLE, PURPLE))
print(buttons_list)



def draw_button(but, mouz, text):
        if dead_inside(but[1], mouz):
            pygame.draw.rect(screen, but[3], but[1])
            pygame.draw.rect(screen, WHITE, (but[1][0]-d, but[1][1] - d, but[1][2]+2*d, c+2*d), d)
        else:
            pygame.draw.rect(screen, but[2], but[1])
            pygame.draw.rect(screen, WHITE, (but[1][0] - d, but[1][1] - d, but[1][2] + 2 * d, c + 2 * d), d)
        font = pygame.font.SysFont('lobster', 55)
        text = font.render(text, False, (0, 0, 0))

        screen.blit(text, (but[1][0]+a/8, but[1][1]+a/10))


def dead_inside(tup, mouz):
    if tup[0] < mouz[0] < tup[0] + tup[2] and tup[1] < mouz[1] < tup[1] + tup[3]:
        return True
    return False

user_text = ''
level = ''
clock = pygame.time.Clock()
finished = False
while True:

    for ev in pygame.event.get():
        mouse = pygame.mouse.get_pos()
        screen.blit(dog_surf, dog_rect)
        for but in buttons_list:
            draw_button(but, mouse, but[0])

        if dead_inside(buttons_list[2][1], mouse):
            default_name = ' '
            if ev.type == pygame.KEYDOWN:
                # Check for backspace
                if ev.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    user_text = user_text[:-1]
                    default_name = user_text
                    buttons_list[2] = list(buttons_list[2])
                    buttons_list[2][0] = default_name
                    buttons_list[2] = tuple(buttons_list[2])
                # Unicode standard is used for string
                # formation
                else:
                    user_text += ev.unicode
                    default_name = user_text
                    buttons_list[2] = list(buttons_list[2])
                    buttons_list[2][0] = default_name
                    buttons_list[2] = tuple(buttons_list[2])
        if dead_inside(buttons_list[3][1], mouse):
            default = ' '
            if ev.type == pygame.KEYDOWN:
                # Check for backspace
                if ev.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    level = level[:-1]
                    default = level
                    buttons_list[3] = list(buttons_list[3])
                    buttons_list[3][0] = default
                    buttons_list[3] = tuple(buttons_list[3])

                # Unicode standard is used for string
                # formation
                else:
                    if ev.unicode in '0123456789':
                        level += ev.unicode
                        default = level
                        buttons_list[3] = list(buttons_list[3])
                        buttons_list[3][0] = default
                        buttons_list[3] = tuple(buttons_list[3])


        # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            if dead_inside(buttons_list[0][1], mouse):
                print("nachat igru")




            if dead_inside(buttons_list[1][1], mouse):
                print('paka')
                pygame.quit()


        if ev.type == pygame.QUIT:
            pygame.quit()



    pygame.display.update()
