import pygame as pg
import math
from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POSITION
        self.player_angle = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.player_angle)
        cos_a = math.cos(self.player_angle)

        x_speed = PLAYER_SPEED * cos_a
        y_speed = PLAYER_SPEED * sin_a

        dx, dy = 0, 0

        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            dx += x_speed
            dy += y_speed
        if keys[pg.K_s]:
            dx -= x_speed
            dy -= y_speed
        if keys[pg.K_d]:
            dx -= x_speed
            dy += y_speed
        if keys[pg.K_a]:
            dx += x_speed
            dy -= y_speed

        self.check_walls(dx, dy)

        if keys[pg.K_LEFT]:
            self.player_angle -= PLAYER_ROTATION_SPEED
        if keys[pg.K_RIGHT]:
            self.player_angle += PLAYER_ROTATION_SPEED
        self.player_angle %= math.tau

    def check_wall_collision(self, x, y) -> bool:
        return (x, y) not in self.game.map.world_map

    def check_walls(self, dx, dy) -> None:
        if self.check_wall_collision(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall_collision(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pg.draw.circle(self.game.screen, 'red',
                       (self.x * 100, self.y * 100), 15)
        pg.draw.line(self.game.screen, 'red', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH*math.cos(self.player_angle),
                      self.y * 100 + WIDTH * math.sin(self.player_angle)))

    def update(self):
        self.movement()


    def pos(self):
        return self.x, self.y


    def map_pos(self):
        return int(self.x), int(self.y)
