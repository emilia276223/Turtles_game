

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
        return x

    def get_state(self):
        return self.turtle_stack


class StartField:
    def __init__(self):
        self.turtle_stack = ["YELLOW", "RED", "GREEN", "PURPLE", "BLUE"]

    def add_turtle(self, turtle):
        self.turtle_stack.append(turtle)

    def take_turtle(self, turtle): # zabiera żółwia
        i = 0
        while self.turtle_stack[i] != turtle:
            i += 1
        return [self.turtle_stack.pop(i)]

    def get_state(self):
        return self.turtle_stack


if __name__=="__main__":
    f = Field()
    f.add_turtle("YELLOW")
    f.add_turtle("BLUE")
    f.add_turtle("RED")
    f.add_turtle("GREEN")
    f.add_turtle("PURPLE")
    print (f.get_state())
    print (f.take_turtle("RED"))
    print(f.get_state())

    f = StartField()
    print(f.get_state())
    print(f.take_turtle("RED"))
    print(f.take_turtle("GREEN"))
    print(f.get_state())
