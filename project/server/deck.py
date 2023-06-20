from card import Card
from random import shuffle

class Deck: # klasa talia kart - przechowuje stos kart do dobierania i stos kart odrzuconych
    def __init__(self):

        # stworzenie talii kart i stosu kart odrzuconych
        self.deck_stack = []
        self.used_cards = []

        # dodanie to talii wszystkich kart i posortowanie jej
        colors = ["YELLOW", "BLUE", "GREEN", "RED", "PURPLE"]
        for color in colors:
            for i in range(5):
                self.deck_stack.append(Card(color, "+"))
            self.deck_stack.append(Card(color, "++"))
            for i in range(2):
                self.deck_stack.append(Card(color, "-"))
        for i in range(2):
            self.deck_stack.append(Card("RAINBOW", "^^"))
        for i in range(3):
            self.deck_stack.append(Card("RAINBOW", "^"))
        for i in range(5):
            self.deck_stack.append(Card("RAINBOW", "+"))
        for i in range(2):
            self.deck_stack.append(Card("RAINBOW", "-"))
        shuffle(self.deck_stack)

    def take_card(self): # usuwa pierwszą karte ze stosu kart do dobierania (gracz dobiera kartę)
        if len(self.deck_stack) < 1:
            raise "error - deck_stack is empty"
        else:
            # gdy zostaje wzięta ostatnia karta z kart to dobrania
            if len(self.deck_stack) == 1:
                # karty z stosu kart odrzuconych są tasowane i przeniesione do kart do dobierania
                shuffle(self.used_cards)
                self.deck_stack = self.deck_stack + self.used_cards
                self.used_cards = []
            return self.deck_stack.pop(0)

    def throw_card(self, card): # dodaje kartę do stosu kart odrzuconych (gracz zagrał kartę)
        self.used_cards.append(card)

if __name__ == "__main__": # testy
    def show(cards):
        print("[", end="")
        for c in cards:
            print("(" + c.color + ", " + c.val + ")", end=", ")
        print("]")

    d = Deck()
    reka = []
    for i in range(5):
        reka.append(d.take_card())
    show(reka)
    for i in range(40):
        d.throw_card(reka[1])
        reka = [reka[0]] + reka[2:]
        reka.append(d.take_card())
        show(reka)
