import pygame as pygame
from gui import GUI

class Client:
	def __init__(self, conn): # tu sie musimy zastanowic jak z tym w, h
		self.connector = conn
		self.textUI = TestUI()
		self.gui = GUI("PLAYER_KEY")

	def play(self):
		nick = self.textUI.start()
		# trzeba przekazac nick do conn
		while self.textUI.state == "waiting":
			state = conn.get_state() # jeszcze nie wiadomo czy dziala
			self.textUI.go(state)
		if self.textUI.state == "error":
			return "error"

		state = conn.get_state()  # jeszcze nie wiadomo czy dziala
		gui.start(self.get_turtle(state))
		while gui.state == "game":
			state = conn.get_state() # jeszcze nie wiadomo czy dziala
			self.gui.go(state)

		state = conn.get_state()  # jeszcze nie wiadomo czy dziala
		gui.end(state)

	def get_turtle(self, state):
		return "NOT YET"

class TextUI:
	def __init__(self):
		self.state = "not started"
	def start(self):
		self.state = "waiting"
		print("Set your nick:")
		nick = input()
		return nick

	def go_on(self, state):
		# jeszcze raczej nie dziala ale juz cos robi
		if state["g_status"] == "game":
			self.state = "game started"
		elif state["g_status"] == "not started":
			print("Still waiting for participants: ")
			print(state["users"].len, "participants at the moment")
			self.state = "waiting"
		else:
			self.state = "error"
			print("There is a problem: game already ended")

if __name__ == "__main__":
	ktos = Client()
	