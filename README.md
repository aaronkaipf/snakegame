# 🐍 Snake Game

Ein klassisches Snake-Spiel implementiert in Python mit Pygame.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)


## 📋 Inhaltsverzeichnis

- [Über das Projekt](#über-das-projekt)
- [Features](#features)
- [Installation](#installation)
- [Steuerung](#steuerung)
- [Spielregeln](#spielregeln)
- [Projektstruktur](#projektstruktur)
- [Technische Details](#technische-details)
- [Screenshots](#screenshots)
- [Lizenz](#lizenz)

## 🎮 Über das Projekt

Dieses Projekt ist eine moderne Implementierung des klassischen Snake-Spiels. Steuere die Schlange, friss Äpfel, wachse und vermeide Kollisionen mit den Wänden und deinem eigenen Schwanz!

## ✨ Features

- 🐍 Flüssige Schlangenbewegung mit 4 Richtungen
- 🍎 Zufällige Apfel-Positionierung
- 📈 Punktesystem
- 💥 Kollisionserkennung (Wände und Schwanz)
- 🎨 Ansprechende Grafiken
- ⌨️ Intuitive Tastatursteuerung
- 🎯 Game Over Screen

## 🚀 Installation

### Voraussetzungen

- Python 3.8 oder höher
- pip (Python Package Manager)

### Schritte

1. Repository klonen:
```bash
git clone https://github.com/deinusername/snake-game.git
cd snake-game
```

2. Pygame installieren:
```bash
pip install pygame
```

3. Spiel starten:
```bash
python projekt.py
```

## 🎮 Steuerung

| Taste | Aktion |
|-------|--------|
| ⬆️ Pfeil nach oben | Bewege nach oben |
| ⬇️ Pfeil nach unten | Bewege nach unten |
| ⬅️ Pfeil nach links | Bewege nach links |
| ➡️ Pfeil nach rechts | Bewege nach rechts |
| ESC | Spiel beenden |

## 📖 Spielregeln

1. **Ziel**: Sammle so viele Äpfel wie möglich und erreiche den höchsten Score
2. **Wachstum**: Jeder gefressene Apfel lässt die Schlange um ein Segment wachsen
3. **Punkte**: Pro Apfel erhältst du 1 Punkt
4. **Game Over**: Das Spiel endet bei Kollision mit:
   - Den Bildschirmrändern
   - Dem eigenen Schwanz

## 📁 Projektstruktur

```
snake-game/
│
├── projekt.py          # Hauptprogramm und Spiellogik
├── schlange.py         # Schlangen-Klasse
├── segment.py          # Segment-Klasse für den Schlangenkörper
├── apfel.py           # Apfel-Klasse
├── richtung.py        # Enum für Bewegungsrichtungen
│
├── bilder/
│   ├── head.png       # Schlangenkopf
│   ├── body.png       # Schlangenkörper-Segment
│   ├── apple.png      # Apfel
│   └── background.png # Hintergrund-Kachel
│
└── README.md          # Diese Datei
```

## 🔧 Technische Details

### Architektur

Das Projekt folgt einem objektorientierten Ansatz mit klarer Trennung der Verantwortlichkeiten:

- **Schlange**: Verwaltet Kopfposition, Bewegung, Richtung und Segmente
- **Segment**: Repräsentiert einzelne Körperteile der Schlange
- **Apfel**: Sprite-Objekt mit zufälliger Positionierung
- **Richtung**: Enum für typsichere Richtungssteuerung

### Verwendete Konzepte

- **Objektorientierte Programmierung**: Klassen und Vererbung
- **Event-Handling**: Tastatureingaben und Timer-Events
- **Sprite-System**: Pygame's Sprite-Gruppen für Kollisionserkennung
- **Enum**: Typsichere Richtungsverwaltung
- **Deep Copy**: Korrekte Positionsspeicherung für Segmente

### Spielparameter

```python
ANZEIGE_BREITE = 800    # Bildschirmbreite in Pixeln
ANZEIGE_HOEHE = 608     # Bildschirmhöhe in Pixeln
GITTER_GROESSE = 32     # Größe einer Kachel
BEWEGUNGS_INTERVAL = 200 # Millisekunden zwischen Bewegungen
FPS = 30                # Frames pro Sekunde
```

## 🛠️ Anpassungen und Erweiterungen

### Ideen für Erweiterungen:

- 🥚 Zusätzliche Items (z.B. Eier mit mehr Punkten)
- ⚡ Power-Ups (Geschwindigkeit, Unverwundbarkeit)
- 🏆 High-Score System mit Persistenz
- 🎵 Sound-Effekte und Hintergrundmusik
- 📊 Schwierigkeitsgrade
- 🌈 Verschiedene Themes/Skins
- 🎨 Partikel-Effekte
- 🏅 Achievements System

### Schwierigkeit anpassen:

```python
# In projekt.py die Geschwindigkeit ändern:
pygame.time.set_timer(BEWEGE_SCHLANGE, 150)  # Schneller
pygame.time.set_timer(BEWEGE_SCHLANGE, 300)  # Langsamer
```
