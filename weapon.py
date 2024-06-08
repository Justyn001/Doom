import pygame as pg
from settings import *


class Weapon:
    def __init__(self, game):
        self.game = game
        self.images = [pg.image.load(f'shoot_images/{i}.png').convert_alpha() for i in range(5)]
        self.image_index = 0
        self.animation_time = 140  # czas trwania jednej klatki animacji w milisekundach
        self.last_shot_time = pg.time.get_ticks()
        self.shooting = False

    def animate_shot(self):
        now = pg.time.get_ticks()       # czas od uruchomienia gry
        if now - self.last_shot_time > self.animation_time: # Jeśli czas trwania animacji jest większy niz 140 to wchodzi do petli
            self.image_index = (self.image_index + 1) % len(self.images)    # modulo tu jest by index szedl od zera jak dojdzie do 5
            self.last_shot_time = now
            if self.image_index == 0:  # Jeśli animacja się zakończyła
                self.shooting = False

    def shoot(self):
        self.shooting = True
        self.image_index = 0
        self.last_shot_time = pg.time.get_ticks()
        print("pifpaf")

    def draw_weapon(self):
        weapon_image = self.images[self.image_index]
        weapon_image = pg.transform.scale(weapon_image, (400, 400))
        weapon_rect = weapon_image.get_rect(midbottom=(800, 900))
        self.game.screen.blit(weapon_image, weapon_rect)

    def update(self):
        if self.shooting:
            self.animate_shot()
