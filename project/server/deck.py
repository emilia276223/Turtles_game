from card import Card
import random
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
            self.deck_stack.append(card("KOLOROWY", "^^"))
        for i in range(3):
            self.deck_stack.append(card("KOLOROWY", "^"))
        for i in range(5):
            self.deck_stack.append(card("KOLOROWY", "+"))
        for i in range(2):
            self.deck_stack.append(card("KOLOROWY", "-"))



    def take_card(self):
        if len(self.deck_stack) < 1:
            raise "error - deck_stack is empty"
        elif len(self.deck_stack) == 1:
            x = self.deck_stack[0]
            new_deck_stack(self)
            return x
        else:
            x = random.choice(self.deck_stack)
            i = 0
            while self.deck_stack[i] != x:
                i += 1
            return self.deck_stack.pop(i)

if __name__ == "__main__":
    l = [1, 5, 7]
    x = l
    shuffle(l)
    print(x)
    print(l)