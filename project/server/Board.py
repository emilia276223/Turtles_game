from typing import List, Any
from field import Field

class Board:
    def __init__(self):
        self.FIELDS = 10
        self.fields = []
        for _ in range(0, self.FIELDS):
            self.fields.append(Field())
        print(len(self.fields))
        self.turtles = []

    def place_turtle(self, turtle, place):
        self.fields[place].add_turtle(turtle)

    def add_turtle(self, turtle):
        self.turtles.append(turtle)
        self.place_turtle(turtle, 0)

    def find_turtle(self, turtle):
        i = 0
        while i < self.FIELDS:
            if turtle in self.fields[i].get_state():
                return i
            i += 1
        return None

    def move_turtle(self, turtle, val):
        place = self.find_turtle(turtle)
        if place is None:
            raise "turtle does not exist"
        if self.FIELDS >= place + val >= 0:
            self.place_turtle(turtle, place + val)
        elif place + val < 0:
            self.place_turtle(turtle, 0)
        else:
            self.place_turtle(turtle, self.FIELDS - 1)


if __name__ == "__main__":
    board = Board()
    print(board.fields[0].turtle_stack)
    board.add_turtle("YELLOW")
    print(board.fields[1])

    print(board.find_turtle("YELLOW"))
    print(board.fields[0].turtle_stack)




