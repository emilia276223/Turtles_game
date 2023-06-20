class Card: # klasa karta - karta ma kolor i wartość, która jest informacją, jak zmienia położenie żółwia, na którego działa
    def __init__(self, color, val):
        self.color = color
        self.val = val

    def get_state(self): # wypisywanie karty jako słownika
        return{
            "color": self.color,
            "val": self.val
        }

    def __str__(self): # wypisywanie karty
        return self.color + " " + self.val
    