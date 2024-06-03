import pygame as pg
from settings import *
import math


class RayCasting:
    def __init__(self, game):
        self.game = game
        self.ray_casting_result = []
        self.object_to_render = []
        self.textures = self.game.object_renderer.wall_textures

    def get_objects_to_render(self):
        self.object_to_render = []
        for ray, value in enumerate(self.ray_casting_result):
            depth, proj_height, texture, offset = value

            if proj_height < LENGTH:                                    # Ten if jest gdy tekstura zajmuje mniej miejsca niz caly pov(nie tylko ta tekstura jest na ekranie)

                wall_column = self.textures[texture].subsurface(            # subsurface służy do przycinania powierzchni (surface) na podstawie określonych parametrów.
                    offset * (TEXTURE_SIZE - SCALE), 0, SCALE, TEXTURE_SIZE
                    )

                wall_column = pg.transform.scale(wall_column, (SCALE, proj_height))
                wall_pos = (ray * SCALE, HALF_LENGTH - proj_height // 2)

            else:                                                      # Ten jest gdy tekstura jest zajmuje cale pov(tylko tektura jest na ekranie)
                texture_height = TEXTURE_SIZE * LENGTH/proj_height
                wall_column = self .textures[texture].subsurface(offset*(TEXTURE_SIZE - SCALE),
                                                  HALF_TEXTURE_SIZE - texture_height//2, SCALE, texture_height)
                wall_column = pg.transform.scale(wall_column, (SCALE, LENGTH))
                wall_pos = (ray * SCALE, 0)

            self.object_to_render.append((depth, wall_column, wall_pos))

    def ray_casting(self):
        self.ray_casting_result = []
        x, y = self.game.player.pos()
        m_x, m_y = self.game.player.map_pos()

        textures_hor, textures_ver = 1, 1

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
                    textures_ver = self.game.map.world_map[actual_position_x]
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
                    textures_hor = self.game.map.world_map[actual_position_y]
                    break
                x_hor += dx
                y_hor += dy
                depth_horizontal += delta_depth

            if depth_vert < depth_horizontal:
                depth, texture = depth_vert, textures_ver
                y_vert %= 1
                if cos_a > 0:
                    offset = y_vert
                else:
                    offset = 1 - y_vert
            else:
                depth, texture = depth_horizontal, textures_hor
                x_hor %= 1
                if sin_a > 0:
                    offset = 1 - x_hor
                else:
                    offset = x_hor

            # usuniecie 'fishbowl' effect
            depth *= math.cos(self.game.player.player_angle - start_angle)

            # pseudo 3d
            projected_height = SCREEN_DIST/(depth + 0.00001)

            self.ray_casting_result.append((depth, projected_height, texture, offset))

            # wall_colour = [255/(1 + depth ** 5 * 0.00002)] * 3
            # pg.draw.rect(self.game.screen, wall_colour,
            #              (ray * SCALE, HALF_LENGTH - projected_height//2, SCALE, projected_height))

            start_angle += DELTA_ANGLE  # następny promień

    def update(self):
        self.ray_casting()
        self.get_objects_to_render()
