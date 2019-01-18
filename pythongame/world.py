import pygame

_world = {}
starting_position = (0, 0)

def tileexists(x, y):
    return _world.get((x, y))

def loadtiles():
    with open('map/map.txt', 'r') as f:
        rows = f.readlines()
    x_max= len(rows[0],split('\t'))
    for y in range(len(rows)):
        cols = rows[y].split('\t')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')
            if tile_name == 'Lobby1':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattir(__import__('tiles'), tile_name)(x,y)
