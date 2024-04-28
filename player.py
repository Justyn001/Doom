import pygame as pg
import math
from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POSITION
        self.player_angel = PLAYER_ANGLE

    def movement(self):
        sin_a = math.sin(self.player_angel)
        cos_a = math.cos(self.player_angel)

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
            self.player_angel -= PLAYER_ROTATION_SPEED
        if keys[pg.K_RIGHT]:
            self.player_angel += PLAYER_ROTATION_SPEED
        self.player_angel %= math.tau

    def check_wall_collision(self, x, y) -> bool:
        return (x, y) not in self.game.map.world_map

    def check_walls(self, dx, dy):
        if self.check_wall_collision(int(self.x + dx), int(self.y)):
            self.x += dx
        if self.check_wall_collision(int(self.x), int(self.y + dy)):
            self.y += dy

    def draw(self):
        pg.draw.circle(self.game.screen, 'red',
                       (self.x * 100, self.y * 100), 15)
        pg.draw.line(self.game.screen, 'red', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH*math.cos(self.player_angel),
                      self.y * 100 + WIDTH * math.sin(self.player_angel)))

    def update(self):
        self.movement()

# from settings import *
# import pygame as pg
# import math
#
#
# class Player:
#     def __init__(self, game):
#         self.game = game
#         self.x, self.y = PLAYER_POSITION
#         self.angle = PLAYER_ANGLE
#
#     def movement(self):
#         sin_a = math.sin(self.angle)
#         cos_a = math.cos(self.angle)
#         dx, dy = 0, 0
#         speed = PLAYER_SPEED
#         speed_sin = speed * sin_a
#         speed_cos = speed * cos_a
#
#         keys = pg.key.get_pressed()
#         num_key_pressed = -1
#         if keys[pg.K_w]:
#             num_key_pressed += 1
#             dx += speed_cos
#             dy += speed_sin
#         if keys[pg.K_s]:
#             num_key_pressed += 1
#             dx += -speed_cos
#             dy += -speed_sin
#         if keys[pg.K_a]:
#             num_key_pressed += 1
#             dx += speed_sin
#             dy += -speed_cos
#         if keys[pg.K_d]:
#             num_key_pressed += 1
#             dx += -speed_sin
#
#             dy += speed_cos
#     def draw(self):
#         pg.draw.line(self.game.screen, 'yellow', (self.x * 100, self.y * 100),
#                      (self.x * 100 + WIDTH * math.cos(self.angle),
#                       self.y * 100 + WIDTH * math.sin(self.angle)), 2)
#         pg.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)
#
#     def update(self):
#             self.movement()
#
#     @property
#     def pos(self):
#         return self.x, self.y
#
#     @property
#     def map_pos(self):
#         return int(self.x), int(self.y)
