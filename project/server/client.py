import pygame as pygame

class Client:
	def __init__(self, w, h, conn, ): # tu sie musimy zastanowic jak z tym w, h
		pass

class GUI:
	def __init__(self, w, h): # tu sie musimy zastanowic jak z tym w, h
		self.screen = pygame.display.set_mode((w, h))
		pygame.display.set_caption("Turtles Game")
		self.draw_turtle = DrawTurtle(screen)
		self.draw_board = DrawBoard(screen)  # to jeszcze zobaczymy czy potrzebne, mozliwe ze nie
		self.draw_card = DrawCard(screen)

	def show_game_state(self, game_state):
		pass

class DrawTurtle:
	def __init__(self, screen):
		self.images = {
			"YELLOW": pygame.image.load("red.png"),
			"RED": pygame.image.load("red.png"), # to sie zmieni jak mi zacznie dzialac program do rysowania bo na razie odmawia wspolpracy z internetem
			"BLUE": pygame.image.load("red.png"),
			"GREEN": pygame.image.load("red.png"),
			"PURPLE": pygame.image.load("red.png")
		}
		self.screen = screen

	def draw(self, turtle, place):
		pass


class DrawBoard:
	def __init__(self, screen):
		pass

	def draw(self):
		pass
	# jeszcze zobaczymy czy jest potrzebne


class DrawCard:
	def __init__(self, screen):
		self.colors = {
			"RAINBOW": pygame.image.load("red.png"), # jak wyzej, obrazki potem zmienimy
			"YELLOW": pygame.image.load("red.png"),
			"RED": pygame.image.load("red.png"),
			"BLUE": pygame.image.load("red.png"),
			"GREEN": pygame.image.load("red.png"),
			"PURPLE": pygame.image.load("red.png")
		}

		self.movement = {
			"++": pygame.image.load("red.png"),
			"+": pygame.image.load("red.png"),
			"--": pygame.image.load("red.png"),
			"-": pygame.image.load("red.png"),
			"^^": pygame.image.load("red.png"),
			"^": pygame.image.load("red.png"),
		}

	def draw(self, card):
		pass
