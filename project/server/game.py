from random import shuffle
from player import Player
from deck import Deck
from card import Card
from board import Board
from turtle import Turtle

class Game:
    def __init__(self, ip_players): # gra dostaje liste adresow ip graczy
        self.players = []
        self.deck = Deck()
        self.board = Board()
        turtles = [Turtle("RED"),Turtle("GREEN"),Turtle("BLUE"),Turtle("PURPLE"),Turtle("YELLOW")]
        shuffle(turtles)
        # tworze graczy przypisuje im losowe zolwie i ich adresy ip
        for i in range(len(ip_players)):
            self.players.append(Player(turtles[0],ip_players[i]))
            turtles.pop(0)
        # gracze dostaja po 5 kart na poczatku
        for i in range(5):
            for p in self.players:
                p.add_card(self.deck.take_card)
        # to teraz gramy dopoki nie jest koniec
        i = 0
        while self.board.finish != True:  # tu cos inaczej!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            if i >= len(self.players):
                i = 0
            turn(self.players[i])
            i += 1
        # co robimy na koncu gry?

    def turn(self, player):
        card = # gracz wybiera karte, ale jak?????????????????????????????????????????????????
        self.board.accept_card(card) # karta rusza zlowiem
        player.remove_card(card) # zabieramy ta karte z reki
        self.deck.throw_card(card # wrzucamy na stos kart odrzuconych
        player.add_card(self.deck.take_card) # dobiera nowa karte

    def card_on_desk(self, player, card):
        # odpowiedz pusta oznacza ze ten gracz nie mial zagrac karty (None)
        # jesli wlasciwy gracz zagral to przeprowadzamy ruch i odp stan gry

    def get_state(self):
        state = {
            "board":self.board.get_state()
        }
        # dodaje wszystkie ustawienia ktore ma gra