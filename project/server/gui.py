import pygame
from card import Card
import time

class GUI:
	def __init__(self, player_key): # tu sie musimy zastanowic jak z tym w, h
		self.player_key = player_key
		self.state = "not started"
		self.last_state = False
		self.SIZE = self.WIDTH, self.HEIGHT = (1500, 900)
		self.screen = pygame.display.set_mode(self.SIZE)
		pygame.display.set_caption("Turtles Game")
		# self.draw_board = DrawBoard(self.screen)  # to jeszcze zobaczymy czy potrzebne, mozliwe ze nie
		self.draw_card = DrawCard(self.screen)

	def start(self, turtle):
		# wyswietlenie zolwia danego gracza na duzym ekranie
		self.my_turtle = turtle
		pygame.init()

	def end(self):
		# sprawdzenie czy gracz wygral czy nie
		pygame.quit()
		exit()
		pass

	def go(self, game_state):
		if self.last_state == game_state:
			return
		self.last_state = game_state

		if game_state["g_status"] == "game":
			state = game_state["game_state"]
			# self.draw_board.draw(state["board"])
			i = 0
			for card in state["players"][self.player_key]:
				self.draw_card.draw(card, i)
				i += 1
			pygame.display.update()

		elif game_state["g_status"] == "finished":
			pass # uzupelnic

		else:
			self.state = "error"


class DrawBoard:
	def __init__(self, screen):
		self.draw_turtle = DrawTurtle(screen)
		self.board = pygame.image.load("board.png")
		self.fields = { # miejsca powinny byc git, nie ma to jak GIMP
			0: [330, 1400],  # start
			1: [102, 1216],
			2: [268, 1160],
			3: [390, 1035],
			4: [274, 846],
			5: [433, 672],
			6: [292, 552],
			7: [200, 390],
			8: [360, 213],
			9: [335, 10]
		}

	def draw(self, state):
		self.screen.blit(board, (0, 0))
		for i in len(state):
			for j in len(state[i]):
				self.draw_turtle.draw(state[i][j], (self.fields[i][0], self.fields[i][1] - i * 15))

class DrawTurtle:
	def __init__(self, screen):
		self.images = {
			"YELLOW": pygame.image.load("yellow.png"),
			"RED": pygame.image.load("red.png"), # to sie zmieni jak mi zacznie dzialac program do rysowania bo na razie odmawia wspolpracy z internetem
			"BLUE": pygame.image.load("blue.png"),
			"GREEN": pygame.image.load("green.png"),
			"PURPLE": pygame.image.load("purple.png")
		}
		self.screen = screen

	def draw(self, turtle, place):
		self.screen.blit(images[turtle], place)

class DrawCard:
	def __init__(self, screen):
		self.screen = screen
		self.background = pygame.image.load("card_background.png")
		self.colors = {
			"RAINBOW": pygame.image.load("crainbow.png"), # jak wyzej, obrazki potem zmienimy
			"YELLOW": pygame.image.load("cyellow.png"),
			"RED": pygame.image.load("cred.png"),
			"BLUE": pygame.image.load("cblue.png"),
			"GREEN": pygame.image.load("cgreen.png"),
			"PURPLE": pygame.image.load("cpurple.png")
		}

		self.movement = {
			"++": pygame.image.load("pp.png"),
			"+": pygame.image.load("p.png"),
			"--": pygame.image.load("mm.png"),
			"-": pygame.image.load("m.png"),
			"^^": pygame.image.load("uu.png"),
			"^": pygame.image.load("u.png"),
		}

		self.places = {
			0: (135, 520),
			1: (385, 520),
			2: (635, 520),
			3: (885, 520),
			4: (1135, 520)
		}

	def draw(self, card, field):
		place = self.places[field]
		self.screen.blit(self.background, place)
		self.screen.blit(self.colors[card.color], place)
		self.screen.blit(self.movement[card.val], place)

if __name__ == "__main__":
	gui = GUI("gracz1")
	gui.start("YELLOW")
	time.sleep(1)
	gui.go(
		{
			"g_status": "game",
			"game_state": {
				"board": False,
				"players": {
					"gracz1": [Card("RAINBOW", "++"), Card("RED", "+"), Card("BLUE", "-"), Card("RAINBOW", "^^"), Card("GREEN", "++")],
					"reszta": False
				}
			}
		}
	)
	time.sleep(10)
	gui.end()
