import pygame, random
from pygame.locals import *
from engine.game import start_sequence
import time

NAME = 'Pharaoh'

""" Color Constants """
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

DIRT = 0
GRASS = 1
WATER = 2
NONE = 3

colors = {
    DIRT: BROWN,
    WATER: BLUE,
    GRASS: GREEN,
    NONE: BLACK
}

""" Map constants """

TILESIZE = 20
WIDTH = 30
HEIGHT = 50

gamemap = [[DIRT for w in range(WIDTH)] for h in range(HEIGHT)]
position = [0,0]

""" Main Entry """
def init() -> None:
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption(NAME)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        start_splash(screen)
        start_sequence()


def start_splash(screen):
    """ Title """
    titlefont = pygame.font.SysFont("comicsansms", 72)
    title = titlefont.render("Pharaoh", True, BROWN)
    screen.blit(title, (250 - title.get_width() // 2, 200 - title.get_height() // 2))

    """ Pyramid """
    pygame.draw.polygon(screen, BROWN, ( (25, 400), (250, 250), (475,400), 0))

    """ Credits """
    footfont = pygame.font.SysFont("comicsansms", 14)
    footer = footfont.render("Created by: Brock Ramsey & Jahan Addison", True, WHITE)
    screen.blit(footer, (250 - footer.get_width() // 2, 425 - footer.get_height() // 2))
   
    pygame.display.update()
    time.sleep(5)


if __name__ == '__main__':
    init()
