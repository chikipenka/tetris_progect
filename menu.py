import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
from typing import Tuple, Any


pygame.init()

FPS = 30

width = 600
height = 400

surface = create_example_window('Example - Simple', (600, 400))


def start_the_game(trigger):
    """ Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc."""
    trigger = True


menu = pygame_menu.Menu("Let's go play Tetris", width, height,
                        theme=pygame_menu.themes.THEME_SOLARIZED)
menu.add.text_input('Name :', default='your nickname')
menu.add.button('Play', start_the_game(start_the_game_trigger))
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                finished = True
    pygame.display.update()
pygame.quit()