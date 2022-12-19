import pygame
import pygame_menu
from pygame_menu.examples import create_example_window
from typing import Tuple, Any
from main_tetris import *

pygame.init()

FPS = 100

width = 600
height = 400

surface = create_example_window('Example - Simple', (600, 400))


def start_the_game() -> None:
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    global user_name
    print(f'{user_name.get_value()}, Do the job here!')


menu = pygame_menu.Menu(
    height=300,
    theme=pygame_menu.themes.THEME_BLUE,
    title='Welcome',
    width=400
)

user_name = menu.add.text_input('Name: ', default='John Doe', maxchar=10)
menu.add.selector('Difficulty: ', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

if __name__ == '__main__':
    menu.mainloop(surface)

clock = pygame.time.Clock()
Finished = False
while not Finished:
    menu.mainloop(surface)
    clock.tick(FPS)
    if start_the_game_trigger:
        Finished = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Finished = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE:
                Finished = True
    pygame.display.update()
pygame.quit()
