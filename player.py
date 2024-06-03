import pygame as pg
import math
from settings import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POSITION
        self.player_angle = PLAYER_ANGLE
        # diagonal movement correction
        self.diag_move_corr = 1 / math.sqrt(2)

    def movement(self):
        sin_a = math.sin(self.player_angle)
        cos_a = math.cos(self.player_angle)

        x_speed = PLAYER_SPEED * cos_a
        y_speed = PLAYER_SPEED * sin_a

        dx, dy = 0, 0

        keys = pg.key.get_pressed()
        number_of_key_pressed = -1
        if keys[pg.K_w]:
            print("W pressed")
            number_of_key_pressed += 1
            dx += x_speed
            dy += y_speed
        if keys[pg.K_s]:
            print("S pressed")
            number_of_key_pressed += 1
            dx -= x_speed
            dy -= y_speed
        if keys[pg.K_d]:
            print("D pressed")
            number_of_key_pressed += 1
            dx += -y_speed
            dy += x_speed
        if keys[pg.K_a]:
            print("A pressed")
            number_of_key_pressed += 1
            dx += y_speed
            dy += -x_speed


        if number_of_key_pressed:
            dx *= self.diag_move_corr
            dy *= self.diag_move_corr



        self.check_walls(dx, dy)

        # if keys[pg.K_LEFT]:
        #     self.player_angle -= PLAYER_ROTATION_SPEED
        # if keys[pg.K_RIGHT]:
        #     self.player_angle += PLAYER_ROTATION_SPEED
        self.player_angle %= math.tau

    def check_wall_collision(self, x, y) -> bool:
        return (x, y) not in self.game.map.world_map

    def check_walls(self, dx, dy) -> None:
        scale = PLAYER_SIZE_SCALE/FPS
        if self.check_wall_collision(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall_collision(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        pg.draw.circle(self.game.screen, 'red',
                       (self.x * 100, self.y * 100), 15)
        pg.draw.line(self.game.screen, 'red', (self.x * 100, self.y * 100),
                     (self.x * 100 + WIDTH*math.cos(self.player_angle),
                      self.y * 100 + WIDTH * math.sin(self.player_angle)))

    def mouse_control(self):
        mx, my = pg.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pg.mouse.set_pos([HALF_WIDTH, HALF_LENGTH])
        self.rel = pg.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.player_angle += self.rel * MOUSE_SENSITIVITY

    def update(self):
        self.movement()
        self.mouse_control()

    def pos(self):
        return self.x, self.y

    def map_pos(self):
        return int(self.x), int(self.y)
