from typing import List, Any


class Board:
    def __int__(self):
        self.FIELDS = 10
        self.fields = []
        self.turtles = []

    def place_turtle(self, turtle, place):
        self.fields[place] = turtle
    def add_turtle(self, turtle):
        self.turtles.append(turtle)
        self.place_turtle(turtle, 0)

    def find_turtle(self, turtle):
        i = 0
        while i < self.FIELDS:
            if turtle in self.fields[i].get_state:
                return i
            i += 1
        return None
    def move_turtle(self, turtle, val):
        place = self.find_turtle(turtle)
        if place == None:
            raise "turtle does not exist"
        if self.FIELDS >= place + val >= 0:
            self.place_turtle(turtle, place + val)
        elif place + val < 0:
            self.place_turtle(turtle, 0)
        else:
            self.place_turtle(turtle, FIELDS - 1)

if __name__ == "__main__":
    board = Board
    board.find_turtle("YELLOW")






