from card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.deck_stack = []
        self.used_cards = []
        colors = ["YELLOW", "BLUE", "GREEN", "RED", "PURPLE"]
        for color in colors:
            for i in range(5):
                self.deck_stack.append(card(color, "+"))
            self.deck_stack.append(card(color, "++"))
            for i in range(2):
                self.deck_stack.append(card(color, "-"))
        for i in range(2):
            self.deck_stack.append(card("RAINBOW", "^^"))
        for i in range(3):
            self.deck_stack.append(card("RAINBOW", "^"))
        for i in range(5):
            self.deck_stack.append(card("RAINBOW", "+"))
        for i in range(2):
            self.deck_stack.append(card("RAINBOW", "-"))
        shuffle(self.deck_stack)

    def take_card(self):
        if len(self.deck_stack) < 1:
            raise "error - deck_stack is empty"
        else:
            if len(self.deck_stack) == 1:
                shuffle(self.used_cards)
                self.deck_stack = self.deck_stack + self.used_cards
                self.used_cards = []
            return self.deck_stack.pop(0)

    def throw_card(self, card):
        self.used_cards.append(card)

if __name__ == "__main__":
    # l = [1, 5, 7]
    # x = l
    # shuffle(l)
    # print(x)
    # print(l)
    d = Deck()
    reka = []
    for i in range(5):
        reka.append(d.take_card())
        print(reka)
    for i in range(40):
        d.throw_card(reka[1])
        reka = reka[0] + reka[2:]
        reka.append(d.take_card())
        print(reka)