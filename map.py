import pygame as pg

_ = False
mini_map = [
    [3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 4, 3],
    [4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, 2, 2, 2, 2, _, _, _, 2, 5, 2, _, _, 3],
    [3, _, _, _, _, _, 5, _, _, _, _, _, 2, _, _, 3],
    [3, _, _, _, _, _, 5, _, _, _, _, _, 2, _, _, 4],
    [3, _, _, 2, 2, 2, 2, _, _, _, _, _, _, _, _, 3],
    [4, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 3],
    [3, _, _, _, _, _, _, _, 1, 1, _, _, _, _, _, 3],
    [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 4],
    ]


class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.make_map()

    def make_map(self):
        for index, row in enumerate(self.mini_map):
            for position, value in enumerate(row):
                if value:
                    self.world_map[(position, index)] = value

    def draw_map(self):
        #self.game.screen.fill('black')
        for pos in self.world_map.keys():
            pg.draw.rect(self.game.screen, 'grey', (pos[0] * 100, pos[1] * 100, 100, 100), 2)


