import pygame as pg
from settings import *
import math


class RayCasting:
    def __init__(self, game):
        self.game = game

    def ray_casting(self):
        x, y = self.game.player.pos()
        m_x, m_y = self.game.player.map_pos()

        start_angle = self.game.player.player_angle - HALF_POV + 0.0001

        for ray in range(NUM_RAYS):
            sin_a = math.sin(start_angle)
            cos_a = math.cos(start_angle)

            if cos_a > 0:  # kierunek przecięcia osi y
                x_vert, dx = m_x + 1, 1
            else:
                x_vert, dx = m_x - 1e-6, -1

            depth_vert = (x_vert - x) / cos_a  # oblicza długość przeciwprostokątnej od punktu startowego
            y_vert = y + depth_vert * sin_a  # y_vert to położenie na osi y promienia

            delta_depth = dx / cos_a  # a to już od pierwszego kwadratu do końca tego kwadratu
            dy = delta_depth * sin_a  # dy = o ile należy przesunąć się w osi y podczas przemieszczania się promienia w pionowym kierunku

            for k in range(MAX_DEPTH):
                actual_position_x = int(x_vert), int(y_vert)
                if actual_position_x in self.game.map.world_map:
                    break
                x_vert += dx  # Przejscie z wartościami do następnego kwadratu
                y_vert += dy
                depth_vert += delta_depth

            if sin_a > 0:  # kierunek przecięcia osi x
                y_hor, dy = m_y + 1, 1
            else:
                y_hor, dy = m_y - 1e-6, -1

            depth_horizontal = (y_hor - y) / sin_a
            x_hor = x + depth_horizontal * cos_a

            delta_depth = dy / sin_a
            dx = delta_depth * cos_a

            for i in range(MAX_DEPTH):
                actual_position_y = int(x_hor), int(y_hor)
                if actual_position_y in self.game.map.world_map:
                    break
                x_hor += dx
                y_hor += dy
                depth_horizontal += delta_depth

            if depth_vert < depth_horizontal:
                depth = depth_vert
            else:
                depth = depth_horizontal

            # usuniecie 'fishbowl' effect
            depth *= math.cos(self.game.player.player_angle - start_angle)

            # pseudo 3d
            projected_height = SCREEN_DIST/(depth + 0.00001)

            wall_colour = [255/(1 + depth ** 5 * 0.00002)] * 3
            pg.draw.rect(self.game.screen, wall_colour,
                         (ray * SCALE, HALF_LENGTH - projected_height//2, SCALE, projected_height))
            start_angle += DELTA_ANGLE  # następny promień

    def update(self):
        self.ray_casting()
