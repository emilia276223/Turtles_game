class Card:
    def __init__(self, color, val):
        self.color = color
        self.val = val

    def __str__(self):
        return self.color + " " + self.val
    