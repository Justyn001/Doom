import pygame as pg
import sys
from settings import *
from map import *
from player import *
from RayCasting import *


class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.ray_cast = RayCasting(self)

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f"{int(self.clock.get_fps())}")
        self.player.movement()
        self.ray_cast.update()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def draw(self):
        self.map.draw_map()
        self.player.draw()

    def run(self):
        while True:
            self.update()
            self.draw()
            self.check_events()


if __name__ == "__main__":
    game = Game()
    game.run()
