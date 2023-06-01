
# pozbywamy sie
class Turtle:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def __str__(self):
        return self.color


if __name__ == "__main__":
    zolw = Turtle("GREEN")
    print(zolw)