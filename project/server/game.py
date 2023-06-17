from random import shuffle
from player import Player
from deck import Deck
from card import Card
from board import Board
# from turtle import Turtle

class Game:
    def __init__(self, ip_players, fields): # gra dostaje liste adresow ip graczy
        self.players = {}
        self.whos_turn = []
        self.deck = Deck()
        self.board = Board(fields)
        self.licznik = 0
        self.is_finished = False
        # turtles = [Turtle("RED"),Turtle("GREEN"),Turtle("BLUE"),Turtle("PURPLE"),Turtle("YELLOW")]
        # shuffle(turtles)
        # tworze graczy przypisuje im losowe zolwie i ich adresy ip
        for i in range(len(ip_players)):
            player = Player(ip_players[i])
            self.players[ip_players[i]] = player
            self.whos_turn.append(player)
            # turtles.pop(0)
        # gracze dostaja po 5 kart na poczatku
        for i in range(5):
            for p in self.players:
                self.players[p].add_card(self.deck.take_card())

    def turn(self, player, card, color=None):
        self.board.accept_card(card, color) # karta rusza zlowiem
        player.remove_card(card) # zabieramy ta karte z reki
        self.deck.throw_card(card) # wrzucamy na stos kart odrzuconych
        player.add_card(self.deck.take_card()) # dobiera nowa karte

    def card_on_desk(self, ip_player, card, color=None):
        who = self.whos_turn[self.licznik].get_ip()
        # print("player {} who should {}".format(ip_player, who))
        if ip_player == who: # jesli wlasciwy gracz zagral to przeprowadzamy ruch i odp stan gry
            # print("corect player {} play card {}".format(ip_player,card))
            self.turn(self.players[ip_player],card, color) # przy wywolaniu metody tez jest self
            self.licznik += 1
            # print("licznik {}".format(self.licznik))
            if len(self.whos_turn) == self.licznik:
                self.licznik = 0
            return self.get_state()
        else: # odpowiedz pusta oznacza ze ten gracz nie mial zagrac karty (None)
            return None

    def get_state(self):
        players_state = {} # []
        for key in self.players:
            players_state[key] = self.players[key].get_cards() # lista stanow kart graczy
        state = {
            "board":self.board.get_state(),
            "players":players_state
        }
        self.is_finished = self.board.is_finished
        if self.is_finished:
            return self.board.ranking # na koniec gry wyswietl ranking ktory jest w board'zie
        return state



if __name__ == "__main__":
    import random
    for j in range(5):
        koniec = True
        players = ["a", "b", "c", "d", "e"]
        colors = ["RED", "GREEN", "BLUE", "PURPLE", "YELLOW"]
        g = Game(players,5)
        print(g.get_state())
        i = 0
        while not g.is_finished:
            p = players[i%5]
            c = random.choice(colors)
            # print("++++++++++++++++")
            card = g.players[p].cards[random.randint(0,4)]
            # print(card)
            g.card_on_desk(p,card,c)
            # print("*********")
            state = g.get_state()
            print(state)
            # print("ktory krok gry ", i)
            i += 1
            if i == 200:
                koniec = False
                break
        print("gra skonczyla sie po {} krokach".format(i))
        print("czy gra sie skonczyla? ", koniec)



# przeprowadzic rozgrywki kartami poprzez wykonanie tylko card_on_desk

# co jak na koniec jest kilka zlowi na starcie? jak powinny byc pokazane w rankingu?