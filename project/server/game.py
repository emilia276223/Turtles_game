from random import shuffle
from player import Player
from deck import Deck
from card import Card
from board import Board

class Game: # klasa gra - koordynuje przebieg gry: kolejność graczy, ich tury, zachowanie się planszy
    def __init__(self, ip_players, fields): # gra dostaje listę adresow ip graczy i liczbę pol które sa na planszy (w sumie ze startem i metą)
        self.players = {}
        self.whos_turn = []
        self.deck = Deck() # tworzę stos kart do dobierania
        self.board = Board(fields) # tworzę planszę
        self.licznik = 0
        self.is_finished = False
        for i in range(len(ip_players)): # tworzę graczy
            player = Player(ip_players[i])
            self.players[ip_players[i]] = player
            self.whos_turn.append(player)
        for i in range(5): # gracze dostają po 5 kart na początku
            for p in self.players:
                self.players[p].add_card(self.deck.take_card())

    def get_ip_of_next(self): # zwraca ip gracza który następny będzie wykonywał ruch
        return self.whos_turn[self.licznik].ip

    def turn(self, player, card, color=None): # przebieg tury gracza
        self.board.accept_card(card, color) # karta rusza żółwiem
        player.remove_card(card) # zabieramy tą karte z reki gracza
        self.deck.throw_card(card) # wrzucamy ją na stos kart odrzuconych
        player.add_card(self.deck.take_card()) # gracz dobiera nową kartę

    def card_on_desk(self, ip_player, card, color=None): # zagranie karty przez gracza
        who = self.whos_turn[self.licznik].ip
        if ip_player == who: # jesli właściwy gracz zagrał to przeprowadzamy ruch i zwracamy stan gry
            self.turn(self.players[ip_player], card, color)
            self.licznik += 1
            if len(self.whos_turn) == self.licznik:
                self.licznik = 0
            return self.get_state()
        else: # gdy zagrał gracz który nie ma teraz ruchu nic się nie dzieje
            return None

    def get_state(self): # stan gry - zwraca aktualny stan planszy i lista stanow kart graczy, a gdy koniec gry zwraca ranking
        players_state = {}
        for key in self.players:
            players_state[key] = self.players[key].get_state()
        state = {
            "board": self.board.get_state(),
            "players": players_state
        }
        self.is_finished = self.board.is_finished
        if self.is_finished:
            return self.board.ranking
        return state



if __name__ == "__main__": # testy
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
