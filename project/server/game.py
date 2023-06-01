from random import shuffle


class Game:
    def __init__(self, id_players):
        self.players = []
        turtles = ["RED","GREEN","BLUE","PURPLE","YELLOW"]
        shuffle(turtles)
        for i in range(len(id_players)):
            self.players.append(Player(turtles[0],id_players[i]))
            turtles.pop(0)
    