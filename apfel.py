import pygame
import random
 
 
class Apfel(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bild = pygame.image.load("bilder/apple.png")
        self.rect = pygame.Rect(
            random.randint(0, 24)*32,
            random.randint(0, 18)*32,
            32,
            32
        )
 
 