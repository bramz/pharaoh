import pygame, random
from pygame.locals import *

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
HEIGHT = 20

gamemap = [[DIRT for w in range(WIDTH)] for h in range(HEIGHT)]
position = [0,0]

""" Main Entry """
def init() -> None:
    pygame.init()
    screen = pygame.display.set_mode((WIDTH*TILESIZE, HEIGHT*TILESIZE))
    pygame.display.set_caption(NAME)

#    screen.fill((255, 255, 255))
    for rw in range(HEIGHT):
        for cl in range(WIDTH):
            rnum = random.randint(0,15)
            if rnum == 0:
                tile = NONE
            elif rnum == 1 or rnum == 2:
                tile = WATER
            elif rnum >= 3 and rnum <= 7:
                tile = GRASS
            else:
                tile = DIRT

            gamemap[rw][cl] = tile

    done = False

    """ Event Loop """

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
#            elif event.type == KEYDOWN:
#                if (event.key) == K_RIGHT:
#                    position[0] += 1

        for row in range(HEIGHT):
            for column in range(WIDTH):
                pygame.draw.rect(screen, colors[gamemap[row][column]], (column*TILESIZE, row*TILESIZE,TILESIZE,TILESIZE))

        pygame.display.update()

if __name__ == '__main__':
    init()
