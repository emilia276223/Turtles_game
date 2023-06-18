import pygame
from server.card import Card

class GUI:
	def __init__(self, player_key): # tu sie musimy zastanowic jak z tym w, h
		self.player_key = player_key
		self.state = "not started"
		self.last_state = False
		self.SIZE = self.HEIGHT, self.WIDTH = (900, 1500)
		self.screen = pygame.display.set_mode(self.SIZE)
		pygame.display.set_caption("Turtles Game")
		self.draw_board = DrawBoard(screen)  # to jeszcze zobaczymy czy potrzebne, mozliwe ze nie
		self.draw_card = DrawCard(screen)

	def start(self, turtle):
		# wyswietlenie zolwia danego gracza na duzym ekranie
		self.my_turtle = turtle

	def end(self):
		# sprawdzenie czy gracz wygral czy nie
		pass

	def go(self, game_state):
		if self.last_state == game_state:
			return
		self.last_state = game_state

		if game_state["g_status"] == "game":
			state = game_state["game_state"]
			self.draw_board.draw(state["board"])
			self.draw_turtle.draw(state["players"])
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
			0: [1400, 330],  # start
			1: [1216, 102],
			2: [1160, 268],
			3: [1035, 390],
			4: [846, 274],
			5: [672, 433],
			6: [552, 292],
			7: [390, 200],
			8: [213, 360],
			9: [10, 335]
		}

	def draw(self, state):
		self.screen.blit(board, (0,0))
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
			0: (520, 135),
			1: (520, 385),
			2: (520, 635),
			3: (520, 985),
			4: (520, 1135)
		}

	def draw(self, card, field):
		place = places[field]
		self.screen.blit(colors[card.color], place)
		self.screen.blit(movement[card.val], place)
