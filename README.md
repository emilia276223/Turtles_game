# Turtles_game
Gra "Pędzące żółwie" wersja komputerowa, napisana w języku Python

## Uruchomienie gry

Potrzebne:
1. flask (https://pypi.org/project/Flask/)
2. pygame (https://www.pygame.org/wiki/GettingStarted)

### Uruchomienie servera:
Żeby móc podłączyć się do serwera z innych urządzeń trzeba uruchomić go komendą
```
flask run --host=0.0.0.0
```
W związku z tym, że pliki __init__ znajdujące się w katalogach server i client uniemożliwiają poprawne działanie flaska należy uruchomić go w katalogu nie zawierającym tych plików.

### Podłączenie klienta do serwera

Należy uruchomić plik client (z katalogu client). Następnie należy podać IP serwera, żeby się z nim połączyć oraz nick, jaki chce się mieć
