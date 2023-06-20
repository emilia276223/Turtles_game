from typing import List, Any
from field import Field, StartField

class Board: #klasa plansza - przechowuje informacje o stanie planszy, ma pola (klasy Pole), między którymi przechodzą żółwie
    def __init__(self, FIELDS):
        self.FIELDS = FIELDS
        self.fields = []
        self.fields.append(StartField())
        for _ in range(1, FIELDS):
            self.fields.append(Field())
        self.turtles = {
            "YELLOW": 0,
            "BLUE": 0,
            "RED": 0,
            "GREEN": 0,
            "PURPLE": 0
        }
        self.is_finished = False

    def finish(self): # gdy gra się kończy tworzymy ranking
        self.is_finished = True
        self.ranking = self.get_ranking()

    def get_ranking(self): # tworzenie rankingu - w jakiej kolejności żółwie były od mety na końcu gry
        ranking = []
        for i in range(self.FIELDS - 1, -1, -1):
            ranking.extend(self.fields[i].get_state())
        return ranking
    def move_turtle(self, turtle, val): #poprawić # przesuwamy żółwia z pola, na którym się znajduje o podaną wartość do przodu lub do tyłu
        place = self.turtles[turtle]
        if place is None:
            raise "turtle does not exist"
        moved = self.fields[place].take_turtle(turtle)
        if moved is str:
            moved = [moved]
        if (self.FIELDS - 1) > place + val >= 0:
            for moved_turtle in moved:
                self.fields[place + val].add_turtle(moved_turtle)
                self.turtles[moved_turtle] = place + val
        elif place + val < 0:
            for moved_turtle in moved:
                self.fields[0].add_turtle(moved_turtle)
                self.turtles[moved_turtle] = 0
        else:
            for moved_turtle in moved:
                self.fields[self.FIELDS - 1].add_turtle(moved_turtle)
                self.turtles[moved_turtle] = self.FIELDS - 1
            self.finish() #dopisac

    def get_state(self): # aktualny stan planszy - słownik kolejnych pól z ich stanem - na którym polu które żółwie stoją i w jakiej kolejności
        state = {}
        for i in range(0, self.FIELDS):
            state[i] = self.fields[i].get_state()
        return state

    def accept_card(self, card, color=None): # przesunięcie żółwi na planszy zgodnie z informacją na zagranej karcie
        # zakladam ze jesli jest wiecej niz 1 ostatni (np kilka na starcie) to mam podane ktory
        if card.val == "++" or card.val == "^^":
            shift = 2
        elif card.val == "+" or card.val == "^":
            shift = 1
        elif card.val == "-":
            shift = -1
        elif card.val == "--":
            shift = -2
        else:
            raise "unknown card"

        if card.val == "^" or card.val == "^^":
            moved_turtle = self.get_ranking()[4]
        elif card.color == "RAINBOW":
            moved_turtle = color
        else:
            moved_turtle = card.color

        self.move_turtle(moved_turtle, shift)



if __name__ == "__main__": # testy
    from card import Card
    def print_end(ranking):
        print(ranking)

    print("TESTY BEZ KART:")

    print("gra pierwsza:")
    board = Board(5) # przecinek w princie wstawia dodatkową spację
    board.move_turtle("YELLOW", 2)
    board.move_turtle("PURPLE", 3)
    board.move_turtle("GREEN", 2)
    board.move_turtle("YELLOW", 2)
    print("powinno być: y, g, p, (b / r), (r / b)")

    print("\ngra druga:")
    board = Board(5)  # przecinek w princie wstawia dodatkową spację
    board.move_turtle("GREEN", 2)
    board.move_turtle("PURPLE", 3)
    board.move_turtle("GREEN", 2)
    print("powinno być: g, p, (y / b / r dowolnie)")

    print("TESTY Z KARTAMI PROSTYMI:")

    y2 = Card("YELLOW", "++")
    y1 = Card("YELLOW", "+")
    y_1 = Card("YELLOW", "-")
    b1 = Card("BLUE", "+")
    p1 = Card("PURPLE", "+")
    p2 = Card("PURPLE", "++")
    g2 = Card("GREEN", "++")
    g_2 = Card("GREEN", "--")
    g_1 = Card("GREEN", "-")
    p_1 = Card("PURPLE", "-")


# (poprawienie boarda tak jak bylo ustalone + dodanie kart, ale na razie tylko prostych (bez rainbow))
    print("gra pierwsza:")
    board = Board(5) # przecinek w princie wstawia dodatkową spację
    board.accept_card(y2)
    board.accept_card(p1)
    board.accept_card(p2)
    board.accept_card(g2)
    board.accept_card(y2)
    print("powinno być: y, g, p, (b / r), (r / b)")


    print("\ngra druga:")
    board = Board(5)  # przecinek w princie wstawia dodatkową spację
    board.accept_card(g2)
    # print(board.get_state())
    board.accept_card(p2)
    # print(board.get_state())
    board.accept_card(p_1)
    # print(board.get_state())
    board.accept_card(p2)
    # print(board.get_state())
    board.accept_card(y1)
    # print(board.get_state())
    board.accept_card(b1)
    # print(board.get_state())
    board.accept_card(y_1)
    # print(board.get_state())
    board.accept_card(y2)
    # print(board.get_state())
    board.accept_card(g2)
    # print(board.get_state())

    print("powinno być: g, y, p, ( b / r dowolnie)")
#  (poprawienie boarda tak jak bylo ustalone + dodanie kart, ale na razie tylko prostych (bez rainbow))

    print("\ngra druga:")
    board = Board(5)  # przecinek w princie wstawia dodatkową spację
    board.accept_card(g2)
    board.accept_card(p2)

    print("ostatni/e to:", board.get_last_s()) # y, b, r

    board.accept_card(p_1)
    board.accept_card(p2)
    board.accept_card(y1)
    board.accept_card(b1)
    board.accept_card(y_1)
    board.accept_card(y2)

    print("ostatni/e to:", board.get_last_s()) # r, b

    board.accept_card(g2)

    print("powinno być: g, y, p, ( b / r dowolnie)")

    # WAŻNE - założyłam, że to gra zadba o to, żeby dostarczyć odpowiednią informację o kolorze jesli jest RAINBOW,
    # w tym kiedy jest ^ lub ^^ (bo jesli jest więcej niż 1 na starcie to można wybrać, na którego działa

    board = Board(5)
    board.move_turtle("YELLOW", 2)
    board.move_turtle("PURPLE", 3)
    board.move_turtle("GREEN", 2)
    board.move_turtle("BLUE", 2)
    board.move_turtle("RED", 2)

    print("ostatni/e to:", board.get_last_s()) # r

    board.move_turtle("YELLOW", 2)

    print("ostatni/e to:", board.get_last_s()) # p

    print(board.ranking)