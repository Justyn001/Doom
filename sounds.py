import pygame as pg
import pygame.mixer


class Sounds:
    def __init__(self, game):
        self.game = game
        self.shotgun_sound = pygame.mixer.Sound("sounds/shotgun_sound.wav")

    def shotgun_sounds(self):
        self.shotgun_sound.set_volume(0.5)
        self.shotgun_sound.play()
