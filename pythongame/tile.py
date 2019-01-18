import items, enemies

import pygame, sys
import os
from pygame.locals import *

# make MAPWIDHT, MAPHEIGHT and tilemap work!!
# make MAPWIDHT, MAPHEIGHT and tilemap work!!
# make MAPWIDHT, MAPHEIGHT and tilemap work!!
# make MAPWIDHT, MAPHEIGHT and tilemap work!!

TILESIZE = 40
MAPHEGHT = 10
MAPWIDHT = 10
BLACK= (0, 0, 0)
BROWN= (100, 30, 0)
GREEN= (0, 255, 0)
BLUE= (0, 0, 255)
GRAY= (125, 125, 125)

FLOOR=0
WALL=1
DOOROPEN=2
DOORCLOSED=3

textures = {
             FLOOR : pygame.image.load(os.path.join('C:/Users/Erik/pythgen/pythongame/images','floor.png')),
             WALL : pygame.image.load(os.path.join('C:/Users/Erik/pythgen/pythongame/images','wall.png')),
             DOOROPEN : pygame.image.load(os.path.join('C:/Users/Erik/pythgen/pythongame/images','dooropen.png')),
             DOORCLOSED : pygame.image.load(os.path.join('C:/Users/Erik/pythgen/pythongame/images','doorclosed.png'))
           }


class maptile:
    def __init__(self, tilemap, MAPWIDHT, MAPHEIGHT):
        self.tilemap = tilemap
        self. MAPWIDHT = MAPWIDHT
        self. MAPHEIGHT = MAPHEIGHT

class Bedroom1(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEIGHT =1 )

class Bedroom2(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEIGHT =1 )

class Bedroom3(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEIGHT =1 )

class Bedroom4(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEIGHT =1 )

class Bedroom5(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1 )



class Hallway1(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1 )

class Hallway2(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1 )

class Hallway3(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1 )

class Hallway4(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1 )



class Livingroom1(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1)

class Livingroom2(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1)

class Livingroom3(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1)

class Livingroom4(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1)



class Kitchen1(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1)

class Kitchen2(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEIGHT =1)



class Shower1(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1)



class Patio1(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1)



class Lobby1(maptile):
    def __init__(self):
        super().__init__(tilemap =(), MAPWIDHT =1, MAPHEGHT =1)
