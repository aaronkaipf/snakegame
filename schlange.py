import pygame
from richtung import Richtung
# ✅ NEU - Imports hinzugefügt:
from copy import deepcopy
from segment import Segment

class Schlange:
    def __init__(self):
        self.bild = pygame.image.load("bilder/head.png")
        self.x = 384
        self.y = 288
        self.richtung = Richtung.RECHTS
        self.neue_richtung = Richtung.RECHTS
        self.gedrehtes_bild = self.bild
        
        # ✅ NEU - Drei neue Variablen für Segmente:
        self.letzte_position = None
        self.segment_hinzufuegen = False
        self.segmente = []
    
    def richtung_aendern(self, neue_richtung):
        if self.richtung == Richtung.OBEN and neue_richtung != Richtung.UNTEN:
            self.neue_richtung = neue_richtung
        elif self.richtung == Richtung.UNTEN and neue_richtung != Richtung.OBEN:
            self.neue_richtung = neue_richtung
        elif self.richtung == Richtung.LINKS and neue_richtung != Richtung.RECHTS:
            self.neue_richtung = neue_richtung
        elif self.richtung == Richtung.RECHTS and neue_richtung != Richtung.LINKS:
            self.neue_richtung = neue_richtung
    
    def aktualisieren(self):
        # ✅ NEU - Alte Position speichern VOR der Bewegung!
        self.letzte_position = deepcopy((self.x, self.y))
        
        # Neue Richtung setzen
        self.richtung = self.neue_richtung
        
        # Bild drehen
        if self.richtung == Richtung.OBEN:
            self.gedrehtes_bild = self.bild
        elif self.richtung == Richtung.UNTEN:
            self.gedrehtes_bild = pygame.transform.rotate(self.bild, 180)
        elif self.richtung == Richtung.LINKS:
            self.gedrehtes_bild = pygame.transform.rotate(self.bild, 90)
        elif self.richtung == Richtung.RECHTS:
            self.gedrehtes_bild = pygame.transform.rotate(self.bild, -90)
        
        # Bewegung
        if self.richtung == Richtung.OBEN:
            self.y -= 32
        elif self.richtung == Richtung.UNTEN:
            self.y += 32
        elif self.richtung == Richtung.LINKS:
            self.x -= 32
        elif self.richtung == Richtung.RECHTS:
            self.x += 32
        
        # ✅ NEU - Segmente bewegen:
        for i in range(len(self.segmente)):
            if i == 0:
                # Erstes Segment folgt dem Kopf
                self.segmente[i].verschieben(self.letzte_position)
            else:
                # Andere Segmente folgen dem vorherigen Segment
                self.segmente[i].verschieben(self.segmente[i-1].letzte_position)
        
        # ✅ NEU - Neues Segment hinzufügen wenn Flagge gesetzt:
        if self.segment_hinzufuegen:
            neues_segment = Segment()
            
            if len(self.segmente) == 0:
                # Erstes Segment - Position vom Kopf
                neue_position = self.letzte_position
            else:
                # Weitere Segmente - Position vom letzten Segment
                neue_position = self.segmente[-1].letzte_position
            
            neues_segment.verschieben(neue_position)
            self.segmente.append(neues_segment)
            
            # Flagge zurücksetzen
            self.segment_hinzufuegen = False
    
    # ✅ NEU - Methode zum Zeichnen der Segmente:
    def segmente_zeichnen(self, anzeige):
        for segment in self.segmente:
            anzeige.blit(segment.bild, (segment.x, segment.y))
    
    # ✅ NEU - Methode zum Apfel fressen:
    def apfel_fressen(self):
        self.segment_hinzufuegen = True
    
    # ✅ NEU - Methode zur Kollisionserkennung:
    def kollision_pruefen(self):
        # Prüfe Kollision mit eigenem Schwanz
        for segment in self.segmente:
            if self.x == segment.x and self.y == segment.y:
                return True
        
        # Prüfe Kollision mit Bildschirmrändern
        if self.x < 0 or self.x >= 800:
            return True
        if self.y < 0 or self.y >= 608:
            return True
        
        # Keine Kollision
        return False