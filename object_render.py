import pygame as pg
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()

    def draw(self):
        self.render_game_object()

    def render_game_object(self):
        list_object = self.game.ray_cast.object_to_render
        for depth, texture, position in list_object:
            self.screen.blit(texture, position)

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
