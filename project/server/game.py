from random import shuffle
from player import Player
from deck import Deck
from card import Card
from board import Board
# from turtle import Turtle

class Game:
    def __init__(self, ip_players): # gra dostaje liste adresow ip graczy
        self.players = {}
        self.whos_turn = []
        self.deck = Deck()
        self.board = Board()
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
                p.add_card(self.deck.take_card)

    def turn(self, player, card):
        self.board.accept_card(card) # karta rusza zlowiem
        player.remove_card(card) # zabieramy ta karte z reki
        self.deck.throw_card(card # wrzucamy na stos kart odrzuconych
        player.add_card(self.deck.take_card) # dobiera nowa karte

    def card_on_desk(self, ip_player, card):
        if ip_player == get.ip(self.whos_turn[self.licznik]): # jesli wlasciwy gracz zagral to przeprowadzamy ruch i odp stan gry
            turn(self.players[ip_player],card)
            self.licznik += 1
            if len(self.whos_turn) >= self.licznik:
                self.licznik = 0
            return get_state()
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
        self.is_finished = self.board.is_finished()
        if self.is_finished:
            return self.board.ranking() # na koniec gry wyswietl ranking ktory jest w board'zie
        return state



if __name__ == "__main__":
    import random
    players = ["a", "b", "c", "d", "e"]
    g = Game(players)
    print g.get_state() # nie wiem czemu tu wyskakuje blad...
    for i in range(20):
        p = random.choice(players)
        g.card_on_desk(p,g.get_state()["players"][p][random.randint(0,4)])
        print g.get_state()


# przeprowadzic rozgrywki kartami poprzez wykonanie tylko card_on_desk