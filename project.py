import pygame
import random
import time
from apfel import Apfel
from schlange import Schlange
from richtung import Richtung
 
# Breite und Höhe des Displays
ANZEIGE_BREITE = 800
ANZEIGE_HOEHE = 608

# ✅ NEU - Variable für Punkte:
punkte = 0

# Hintergrund erstellen
hintergrund = pygame.Surface((ANZEIGE_BREITE, ANZEIGE_HOEHE))
 
for i in range(25):
    for j in range(19):
        kachel = pygame.image.load("bilder/background.png")
        maske = (random.randrange(0, 20), random.randrange(0, 20), random.randrange(0, 20))
        kachel.fill(maske, special_flags=pygame.BLEND_ADD)
        hintergrund.blit(kachel, (i*32, j*32))
 
# Einstellungen
pygame.init()

# ✅ NEU - Schriftart für Punkte und Game Over:
schrift = pygame.font.Font(None, 36)
 
# Display-Objekt und Spieluhr
anzeige = pygame.display.set_mode([ANZEIGE_BREITE, ANZEIGE_HOEHE])
uhr = pygame.time.Clock()
 
# Äpfel
apfel = Apfel()
aepfel = pygame.sprite.Group()
aepfel.add(apfel)

# Schlange erstellen
schlange = Schlange()

# Event für Schlangen-Bewegung
BEWEGE_SCHLANGE = pygame.USEREVENT + 1
pygame.time.set_timer(BEWEGE_SCHLANGE, 200)
 
spiel_aktiv = True
while spiel_aktiv:
    for ereignis in pygame.event.get():
        if ereignis.type == pygame.KEYDOWN:
            if ereignis.key == pygame.K_ESCAPE:
                spiel_aktiv = False
            # Tastatursteuerung
            elif ereignis.key == pygame.K_UP:
                schlange.richtung_aendern(Richtung.OBEN)
            elif ereignis.key == pygame.K_DOWN:
                schlange.richtung_aendern(Richtung.UNTEN)
            elif ereignis.key == pygame.K_LEFT:
                schlange.richtung_aendern(Richtung.LINKS)
            elif ereignis.key == pygame.K_RIGHT:
                schlange.richtung_aendern(Richtung.RECHTS)
 
        elif ereignis.type == pygame.QUIT:
            spiel_aktiv = False
        
        # Event für Schlangen-Bewegung
        elif ereignis.type == BEWEGE_SCHLANGE:
            schlange.aktualisieren()
    
    # ✅ NEU - Kollision mit Apfel prüfen:
    for apfel in aepfel:
        if schlange.x == apfel.rect.x and schlange.y == apfel.rect.y:
            # Apfel entfernen
            aepfel.remove(apfel)
            
            # Schlange wächst
            schlange.apfel_fressen()
            
            # Punkte erhöhen
            punkte += 1
            
            # Neuen Apfel erstellen
            neuer_apfel = Apfel()
            aepfel.add(neuer_apfel)
 
    # Hintergrund zeichnen
    anzeige.blit(hintergrund, (0, 0))
    
    # ✅ NEU - Segmente zeichnen:
    schlange.segmente_zeichnen(anzeige)
 
    # Äpfel zeichnen
    for apfel in aepfel:
        anzeige.blit(apfel.bild, apfel.rect)
    
    # Schlange zeichnen
    anzeige.blit(schlange.gedrehtes_bild, (schlange.x, schlange.y))
    
    # ✅ NEU - Punkte anzeigen:
    punkte_text = schrift.render(f"Punkte: {punkte}", True, (255, 255, 255))
    anzeige.blit(punkte_text, (10, 10))
    
    # ✅ NEU - Kollision prüfen und Game Over:
    if schlange.kollision_pruefen():
        # Game Over Text
        game_over_text = schrift.render("Game Over!", True, (255, 0, 0))
        text_rect = game_over_text.get_rect(center=(ANZEIGE_BREITE//2, ANZEIGE_HOEHE//2))
        anzeige.blit(game_over_text, text_rect)
        
        # Aktualisiere den Bildschirm
        pygame.display.flip()
        
        # Warte 3 Sekunden
        time.sleep(3)
        
        # Beende das Spiel
        spiel_aktiv = False
 
    # Bildschirm aktualisieren
    pygame.display.flip()
    # FPS auf 30 setzen
    uhr.tick(30)
 
# 3 Sekunden Wartezeit
time.sleep(3)
# Programm schließen
pygame.quit()