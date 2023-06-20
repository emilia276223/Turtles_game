import pygame as pygame
from gui import GUI
from connection import Connector
import time
# from ConnectionMock import ConnectionMock

connect_class = Connector # ConnectionMock


class Client:
	def __init__(self):
		self.state = "waiting"
		self.textUI = TextUI()
		# self.conn = None
		self.nick, url = self.textUI.start()
		self.conn = connect_class(url, self.nick)

	def play(self):
		if self.state == "waiting":
			state = self.conn.get_state() # jeszcze nie wiadomo czy dziala
			self.textUI.go_on(state)
			if self.textUI.state == "game started":
				self.gui = GUI(self.conn.ip)
				# print("GUI started")
				self.gui.start(self.conn.turtle)
				self.state = "game"
			return
		if self.textUI.state == "error":
			return "error"

		game_state = self.conn.get_state()
		# print(state)
		if self.state == "game":
			if game_state["turn"] == self.conn.ip:
				card = self.gui.go(game_state)
				game_state = self.conn.card_on_table(card)
			else:
				self.gui.show(game_state)
				time.sleep(0.7) # how frequently is refreshed, can be changed by more frequency results in more visible

		if game_state["g_status"] == "finished":
			self.gui.go(game_state)
			self.state = "finished"
			self.ranking = game_state["ranking"]
			self.users_info = game_state["users_info"]
			print("Game finished")
			print("Ranking: ", g1.ranking)
			print("Users info: ", g1.users_info)
			self.gui.end()

		# else:
		# 	self.gui.end()

class TextUI:
	def __init__(self):
		self.state = "waiting"
	def start(self):
		self.state = "waiting"
		url = input("Input game IP:")
		print("Set your nick:")
		nick = input()
		return (nick, url)

	def go_on(self, state): # dopóki gra się nie rozpoczęła wypisuje informacje o czekaniu na graczy
		# jeszcze raczej nie dziala ale juz cos robi
		if state["g_status"] == "game":
			self.state = "game started"
		elif state["g_status"] == "not started":
			print("Still waiting for participants: ")
			print(len(state["users"]), "participants at the moment")
			time.sleep(3)
			self.state = "waiting"
		else:
			self.state = "error"
			print("There is a problem: game already ended")

if __name__ == "__main__":
	# uruchomienie gry
	g1 = Client() # stworzenie klienta (gracza)
	while not g1.state == "finished":
		g1.play() # odswieżenie gry

