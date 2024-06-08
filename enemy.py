import pygame as pg
from settings import *


class Enemy:
    def __init__(self, game, path="npc/profil/0.png", pos=(10.5, 3.5)):
        self.game = game
        self.x, self.y = pos
        self.image = pg.image.load(path).convert_alpha()
        self.IMAGE_WIDTH = self.image.get_width()
        self.HALF_IMAGE_WIDTH = self.IMAGE_WIDTH // 2
        self.dx, self.dy, self.theta = 0, 0, 0
        self.IMAGE_RATIO = self.IMAGE_WIDTH/ self.image.get_height()

    def get_sprite(self):
        self.dx = self.x - self.game.player.x
        self.dy = self.y - self.game.player.y
        self.theta = math.atan2(self.dy, self.dx)        # kąt pod jakim patrzymy na przeciwnika

        delta = self.theta - self.game.player.player_angle
        if (self.dx > 0 and self.game.player.player_angle > math.pi) or (self.dx < 0 and self.dy < 0):   # ten if to zabezpieczenie zeby nie wyszlo poza dopuszcalny zakres
            delta += math.tau

        delta_rays = delta / DELTA_ANGLE                    # ilość promieni o ile przesunie się sprite w lewo lub w prawo w zależności od kąta
        self.screen_x = (HALF_NUM_RAYS + delta_rays) * SCALE    # pozycja na ekreanie wzglewdem srodka ekranu

        self.dist = math.hypot(self.dx, self.dy)  #  oblicza długość wektora od początku układu współrzędnych(gracza) do punktu o współrzędnych podanych(enemy)
        self.norm_dist = self.dist * math.cos(delta)    # odleglosc od przeciwnika uwzgledniajaca kat widzenia gracza

        if -self.HALF_IMAGE_WIDTH < self.screen_x < (WIDTH + self.HALF_IMAGE_WIDTH) and self.norm_dist > 0.5:   # czy przeciwnik jest w widocznej czesci ekranu
            self.get_sprite_projection()

    def get_sprite_projection(self):
        proj = SCREEN_DIST / self.norm_dist
        proj_width, proj_height = proj * self.IMAGE_RATIO, proj

        image = pg.transform.scale(self.image, (proj_width, proj_height))

        self.sprite_half_width = proj_width // 2
        pos = self.screen_x - self.sprite_half_width, HALF_LENGTH - proj_height // 2

        self.game.ray_cast.object_to_render.append((self.norm_dist, image, pos))

    def update(self):
        self.get_sprite()
