import pygame as pygame
from gui import GUI
from connection import Connector
import time
# from ConnectionMock import ConnectionMock

connect_class = Connector # ConnectionMock, for the tests

class Client: # informacje o danym kliencie (ip, polaczenie z serwerem przez connection, interfejs graficzny)
	def __init__(self):
		self.state = "waiting"
		self.textUI = TextUI()
		self.nick, url = self.textUI.start()
		self.conn = connect_class(url, self.nick)

	def play(self): # odswierzenie statusu gry, zaleznie od tego, ktorego gracza jest tura, odpowiednio dodatkowo polozenie karty

		# jeśli gra się jeszcze nie zaczęła
		if self.state == "waiting":
			# pobranie nowego statusu i odpowiednio oczekiwanie na pozostalych graczy lub rozpoczecie gry
			state = self.conn.get_state()
			self.textUI.go_on(state)
			if self.textUI.state == "game started":
				# uruchomienie interfejsu graficznego
				self.gui = GUI(self.conn.ip)
				self.gui.start(self.conn.turtle)
				self.state = "game"
			return

		if self.textUI.state == "error":
			return "error"

		# if we are past (waiting = textUI) state, so game is already started:
		game_state = self.conn.get_state()
		if game_state["g_status"] == "game":  # if the game has not ended
			if game_state["turn"] == self.conn.ip:
				# gracz wybiera kartę i przekazujemy ją do servera
				card = self.gui.go(game_state)
				game_state = self.conn.card_on_table(card)
			else:
				self.gui.show(game_state)
				time.sleep(0.7) # how frequently is refreshed, can be changed by more frequency results in more visible

		# jeśli gra została już zakończona
		if game_state["g_status"] == "finished":
			# wyświetlamy ranking ...
			self.state = "finished"
			self.ranking = game_state["ranking"]
			self.users_info = game_state["users_info"]
			print("Game finished")
			print("Ranking: ", g1.ranking)
			print("Users info: ", g1.users_info)
			# w interfejsie graficznym wyświetlamy czy wygrana / który żółw wygrał
			self.gui.go(game_state)

class TextUI:
	def __init__(self):
		self.state = "waiting"
	def start(self): # początek: ustawienie statusu, spytanie o potrzebne informacje
		self.state = "waiting"
		url = input("Input game IP:")
		print("Set your nick:")
		nick = input()
		return (nick, url) # zwracamy nick i url, żeby połączyć z serwerem

	def go_on(self, state): # dopóki gra się nie rozpoczęła wypisuje informacje o czekaniu na graczy
		if state["g_status"] == "game": # jeśli gra się zaczyna to zmienia status
			self.state = "game started"
		elif state["g_status"] == "not started":
			print("Still waiting for participants: ")
			print(len(state["users"]), "participants at the moment")
			time.sleep(3)
			self.state = "waiting"
		else: # w innych przypadkach error (błąd z połączeniem z serwerem na przykład
			self.state = "error"
			print("There is a problem: game already ended")


if __name__ == "__main__": # uruchomienie gry
	g1 = Client() # stworzenie klienta (gracza)
	while not g1.state == "finished":
		g1.play() # odswieżenie gry

