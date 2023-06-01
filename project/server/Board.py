from typing import List, Any
from field import Field, StartField
from turtle import Turtle

# pozbyć sie klasy zolw, robimy napisy jak wczesniej
class Board:
    def __init__(self, FIELDS, end_consumer, turtles):
        self.FIELDS = FIELDS
        self.fields = []
        self.fields.append(StartField(turtles))
        for _ in range(1, FIELDS):
            self.fields.append(Field())
        # print(len(self.fields))
        # self.turtles = {
        #     "YELLOW": 0,
        #     "BLUE": 0,
        #     "RED": 0,
        #     "GREEN": 0,
        #     "PURPLE": 0
        # }
        self.turtles = { #
            turtles[0]: 0,
            turtles[1]: 0,
            turtles[2]: 0,
            turtles[3]: 0,
            turtles[4]: 0
        }
        self.is_finished = False
        self.end_consumer = end_consumer # funkcja wyliczajaca wygrywajacego na podstawie listy rankingowej zolwi

    # def place_turtle(self, turtle, place):
    #     self.fields[place].add_turtle(turtle)

    # def add_turtle(self, turtle):
    #     self.turtles.append(turtle)
    #     self.place_turtle(turtle, 0)

    # def find_turtle(self, turtle):
    #     i = 0
    #     while i < self.FIELDS:
    #         if turtle in self.fields[i].get_state():
    #             return i
    #         i += 1
    #     return None

    # def if_finished(self):
    #     if len(self.fields[self.FIELDS - 1].get_state()) > 0:
    #         return True
    #     return False

    def finish(self):
        self.is_finished = True
        ranking = []
        for i in range(self.FIELDS - 1, -1, -1):
            ranking.extend(self.fields[i].get_state())
        self.end_consumer(ranking)

    def move_turtle(self, turtle, val): #poprawić
        place = self.turtles.get(turtle)
        # print(place)
        if place is None:
            raise "turtle does not exist"
        moved = self.fields[place].take_turtle(turtle)
        if moved is str:
            moved = [moved]
        # print(moved)
        if (self.FIELDS - 1) > place + val >= 0:
            for moved_turtle in moved:
                # print(moved_turtle)
                self.fields[place + val].add_turtle(moved_turtle)
                self.turtles[moved_turtle] = place + val
        elif place + val < 0:
            for moved_turtle in moved:
                # print(moved_turtle)
                self.fields[0].add_turtle(moved_turtle)
                self.turtles[moved_turtle] = 0
        else:
            for moved_turtle in moved:
                # print(moved_turtle)
                self.fields[self.FIELDS - 1].add_turtle(moved_turtle)
                self.turtles[moved_turtle] = self.FIELDS - 1
            self.finish() #dopisac

    def get_state(self):
        state = {}
        for i in range(0, self.FIELDS):
            state[i] = self.fields[i].get_state()
        return state

    def accept_card(self, card, color=None):
        # porudzenie odpowiednim zolwiem

if __name__ == "__main__":
    from card import Card
    yellow = Turtle("YELLOW")
    green = Turtle("GREEN")
    blue = Turtle("BLUE")
    purple = Turtle("PURPLE")
    red = Turtle("RED")

    turtles = [yellow, green, blue, purple, red]
    # dac lambde do funkcji, zeby nie powtarzac kodu
    print("gra pierwsza:")
    board = Board(5, lambda ranking: [print (i.get_color(), end=", ") for i in ranking], turtles.copy()) # przecinek w princie wstawia dodatkową spację
    board.move_turtle(yellow, 2)
    board.move_turtle(purple, 3)
    board.move_turtle(green, 2)
    board.move_turtle(yellow, 2)

    print("\ngra druga:")
    board = Board(5, lambda ranking: [print (i.get_color(), end=", ") for i in ranking], turtles.copy())  # przecinek w princie wstawia dodatkową spację
    board.move_turtle(green, 2)
    board.move_turtle(purple, 3)
    board.move_turtle(green, 2)
    board.move_turtle(yellow, 2)

    # dodac testy z kartami a nie move_turtle




