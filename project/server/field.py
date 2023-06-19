class Field: # klasa pole - pole przechowuje listę żółwi, które na nim stoją (w kolejności w jakiej były stawiane na to pole)
    def __init__(self):
        self.turtle_stack = []

    def add_turtle(self, turtle): # dodanie żółwia do listy - żółw został postawiony na to pole
        self.turtle_stack.append(turtle)

    def take_turtle(self, turtle): # usunięcie z listy żółwia wraz ze wszystkimi żółwiami stojącymi na nim - żółw został zabrany z tego pola
        i = 0
        while self.turtle_stack[i] != turtle:
            i += 1
        x = self.turtle_stack[i:]
        self.turtle_stack[i:] = []
        return x.copy() # dodalam copy, zeby nikt inny nie mogl tego zmienic (nie dzialalo mi bo przypadkiem zmienilam w board

    def get_state(self): # wypisuje aktualny stan pola - listę stojących na nim żółwi
        return self.turtle_stack.copy() # dodalam copy, zeby nikt inny nie mogl tego zmienic (nie dzialalo mi bo przypadkiem zmienilam w board


class StartField(Field): # podklasa klasy pole - pole startowe
    def __init__(self): # na początku gry stoją na nim wszystkie żółwie
        self.turtle_stack = ["YELLOW", "GREEN", "BLUE", "RED", "PURPLE"]

    def take_turtle(self, turtle): # usunięcie z listy żółwia - żółw został zabrany z tego pola
        i = 0
        while self.turtle_stack[i] != turtle:
            i += 1
        return [self.turtle_stack.pop(i)]


if __name__=="__main__":

    f = Field()
    f.add_turtle("YELLOW")
    f.add_turtle("BLUE")
    f.add_turtle("RED")
    f.add_turtle("GREEN")
    f.add_turtle("PURPLE")
    print (f.get_state(), "powinno być: y, b, r, g, p")
    print (f.take_turtle("RED"), "powinno być: r, g, p")
    print(f.get_state(), "powinno być: y, b")

    f = StartField()
    print(f.get_state(), "powinno być: wszystkie w dowolnej kolejnosci")
    print(f.take_turtle("RED"), "powinno być: RED")
    print(f.take_turtle("GREEN"), "powinno być: GREEN")
    print(f.get_state(), "powinno być: (y, p, b))")
