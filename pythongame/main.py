import tile, items, enemies

import pygame, sys
from pygame.locals import *


# make MAPWIDHT, MAPHEIGHT and tilemap work!!
# make MAPWIDHT, MAPHEIGHT and tilemap work!!
# make MAPWIDHT, MAPHEIGHT and tilemap work!!
# make MAPWIDHT, MAPHEIGHT and tilemap work!!

pygame.init()
DISPLAYSURF = pygame.display.set_mode((20*tile.TILESIZE,20*tile.TILESIZE))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for row in range(tile.MAPHEIGHT):
        for column in range(tile.MAPWIDHT):
            DISPLAYSURF.blit(tile.textures[tile.tilemap[row][column]], (column*tile.TILESIZE,row*tile.TILESIZE))

    pygame.display.update()
