

class Field:
    def __init__(self):
        self.turtle_stack = []

    def add_turtle(self, turtle):
        self.turtle_stack.append(turtle)

    def take_turtle(self, turtle):
        i = 0
        while self.turtle_stack[i] != turtle:
            i += 1
        x = self.turtle_stack[i:]
        self.turtle_stack[i:] = []
        return x.copy() # dodalam copy, zeby nikt inny nie mogl tego zmienic (nie dzialalo mi bo przypadkiem zmienilam w board

    def get_state(self):
        return self.turtle_stack.copy() # dodalam copy, zeby nikt inny nie mogl tego zmienic (nie dzialalo mi bo przypadkiem zmienilam w board


class StartField(Field):
    def __init__(self):
        self.turtle_stack = ["YELLOW", "GREEN", "BLUE", "RED", "PURPLE"]

    def take_turtle(self, turtle): # zabiera żółwia
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
