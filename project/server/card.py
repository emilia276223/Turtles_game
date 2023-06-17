class Card:
    def __init__(self, color, val):
        self.color = color
        self.val = val

    def get_color(self):
        return self.color

    def get_val(self):
        return self.val

    def __str__(self):
        return self.color + " " + self.val
    