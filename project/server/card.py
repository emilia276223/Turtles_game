class Card: # klasa karta - karta ma kolor i wartość, która jest informacją, jak zmienia położenie żółwia, na którego działa
    def __init__(self, color, val):
        self.color = color
        self.val = val

    def __str__(self): # wypisywanie karty (kolor i wartość)
        return self.color + " " + self.val
    