from typing import List, Any
from field import Field, StartField


class Board:
    def __init__(self, FIELDS, end_consumer):
        self.FIELDS = FIELDS
        self.fields = []
        self.fields.append(StartField())
        for _ in range(1, FIELDS):
            self.fields.append(Field())
        # print(len(self.fields))
        self.turtles = {
            "YELLOW": 0,
            "BLUE": 0,
            "RED": 0,
            "GREEN": 0,
            "PURPLE": 0
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
        print(place)
        if place is None:
            raise "turtle does not exist"
        moved = self.fields[place].take_turtle(turtle)
        if moved is str:
            moved = [moved]
        print(moved)
        if self.FIELDS > place + val >= 0:
            for moved_turtle in moved:
                print(moved_turtle)
                self.fields[place + val].add_turtle(moved_turtle)
                self.turtles[moved_turtle] = place + val
        elif place + val < 0:
            for moved_turtle in moved:
                print(moved_turtle)
                self.fields[0].add_turtle(moved_turtle)
                self.turtles[moved_turtle] = 0
        else:
            for moved_turtle in moved:
                print(moved_turtle)
                self.fields[self.FIELDS - 1].add_turtle(moved_turtle)
                self.turtles[moved_turtle] = self.FIELDS - 1
            self.finish() #dopisac


if __name__ == "__main__":
    board = Board(5, lambda ranking: print("Wynik gry:", ranking)) # przecinek w princie wstawia dodatkową spację
    print(board.fields[0].turtle_stack)
    print(board.fields[1])

    print(board.fields[0].turtle_stack)

    print (board.move_turtle("YELLOW", 2))
    print (board.move_turtle("PURPLE", 3))
    print (board.move_turtle("GREEN", 2))
    print (board.move_turtle("YELLOW", 2))
    print (board.move_turtle("YELLOW", 2))
    # print(board.move_turtle("YELLOW", 2))
    # print(board.move_turtle("YELLOW", 2))
    # dodac wiecej testow




