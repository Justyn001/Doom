import pygame as pg
import pygame.mixer


class Sounds:
    def __init__(self, game):
        self.game = game
        self.shotgun_sound = pygame.mixer.Sound("sounds/shotgun_sound.wav")
        self.theme_song = pygame.mixer.Sound("sounds/theme2.mp3")

    def shotgun_sounds(self):
        self.shotgun_sound.set_volume(0.2)
        self.shotgun_sound.play()

    def theme(self):
        self.theme_song.set_volume(0.1)    #0.15
        self.theme_song.play(loops=-1)
