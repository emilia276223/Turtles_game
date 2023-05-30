

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


if __name__=="__main__":
    f = Field()
    f.add_turtle("YELLOW")
    print (f.get_state())