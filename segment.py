import pygame
from copy import deepcopy

class Segment:
    def __init__(self):
        # Lade das Segment-Bild
        self.bild = pygame.image.load("bilder/segment.png")
        
        # Setze Position außerhalb des Bildschirms
        self.x = -100
        self.y = -100
        
        # Erstelle Variable für letzte Position
        self.letzte_position = None
    
    def verschieben(self, neue_position):
        # Speichere aktuelle Position als letzte Position
        self.letzte_position = deepcopy((self.x, self.y))
        
        # Setze neue Position
        self.x = neue_position[0]
        self.y = neue_position[1]