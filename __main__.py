import pygame
from player import skill
from player import level

NAME = 'Pharaoh'

""" Main Entry """
def init() -> None:
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption(NAME)

    screen.fill((255, 255, 255))

    done = False

    """ Event Loop """

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

if __name__ == '__main__':
    init()
