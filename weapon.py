import pygame as pg
import re
from enemy import *
from settings import *


class Weapon:
    def __init__(self, game):
        self.game = game
        f = open('images.txt')
        files = [str(f.readline().strip()) for i in range(5)]
        png_files = [file for file in files if re.match(r'.*\.png$', file)]
        self.images = [pg.image.load(file).convert_alpha() for file in png_files]
        self.image_index = 0
        self.animation_time = 140  # czas trwania jednej klatki animacji w milisekundach
        self.last_shot_time = pg.time.get_ticks()
        f.close()
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
        self.check_hit_in_npc()

    def draw_weapon(self):
        weapon_image = self.images[self.image_index]
        weapon_image = pg.transform.scale(weapon_image, (400, 400))
        weapon_rect = weapon_image.get_rect(midbottom=(800, 900))
        self.game.screen.blit(weapon_image, weapon_rect)

    def check_hit_in_npc(self):
        if HALF_WIDTH - self.game.enemy.sprite_half_width < self.game.enemy.screen_x < HALF_WIDTH + self.game.enemy.sprite_half_width:
            self.game.music.play_hit_sound()
            self.game.enemy.image = pg.image.load("npc/profil/death.png").convert_alpha()

    def update(self):
        if self.shooting:
            self.animate_shot()

