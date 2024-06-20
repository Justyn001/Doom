import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_render import *
from weapon import *
from sounds import *
from enemy import *


class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.new_game()
        self.music.theme()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.ray_cast = RayCasting(self)
        self.weapon = Weapon(self)
        self.music = Sounds(self)

        self.enemy = Enemy(self)
        self.enemy2 = Enemy(self, path="npc/profil/0.png", pos=(5, 5))


    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f"{int(self.clock.get_fps())}")
        self.player.update()
        self.ray_cast.update()
        self.weapon.update()

        self.enemy.update()
        self.enemy2.update()


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and self.weapon.shooting is False:
                self.weapon.shoot()
                self.music.shotgun_sounds()

    def draw(self):
        #self.screen.fill("black")
        self.object_renderer.draw()
        self.weapon.draw_weapon()
        #self.ray_cast.update()
        #self.map.draw_map()
        #self.player.draw()


    def run(self):
        while True:
            self.update()
            self.draw()
            self.check_events()


if __name__ == "__main__":
    game = Game()
    game.run()
