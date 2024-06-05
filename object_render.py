import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky = self.get_texture("textures/sky.png", (WIDTH, HALF_LENGTH))
        self.sky_offset = 0

    def draw(self):
        self.render_background()
        self.render_game_object()

    def render_game_object(self):
        list_object = self.game.ray_cast.object_to_render
        for depth, texture, position in list_object:
            self.screen.blit(texture, position)

    def render_background(self):
        self.sky_offset = (self.sky_offset + 4.5 *self.game.player.rel) % WIDTH     # 4.5 to stała, która kontroluje prędkość przesuwania tła nieba
        self.screen.blit(self.sky, (-self.sky_offset, 0))               # rysuje niebo przesunięte o -self.sky_offset w osi X i umieszczony na samej górze ekranu (y = 0).
        self.screen.blit(self.sky, (-self.sky_offset+WIDTH, 0))         # rysuje drugi obraz nieba, umieszczony tuż za pierwszym, zapewniając płynne przejście
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_LENGTH, WIDTH, LENGTH))

    @staticmethod
    def get_texture(path, size=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, size)

    def load_wall_textures(self):
        return {
            1: self.get_texture("textures/1.png"),
            2: self.get_texture("textures/2.png"),
            3: self.get_texture("textures/3.png"),
            4: self.get_texture("textures/4.png"),
            5: self.get_texture("textures/5.png"),
        }
