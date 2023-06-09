import pygame
import time

# obsługa interfejsu graficznego
class GUI: # całość / połączenie interfejsu graficznego
	def __init__(self, player_key): # ustawienie parametrów, załadowanie potrzebnych plików
		# ustawienie odpowiednich wartości
		self.player_key = player_key # ip gracza
		self.state = "not started"
		self.last_state = False

		# utworzenie okna, ale jeszcze nie uruchomienie
		self.SIZE = self.WIDTH, self.HEIGHT = (1500, 900)
		self.screen = pygame.display.set_mode(self.SIZE)
		pygame.display.set_caption("Turtles Game" + self.player_key)

		# klasy rysujące poszczególne części
		self.draw_board = DrawBoard(self.screen) # rysowanie planszy, w tym ustawienia żółwi
		self.draw_card = DrawCard(self.screen) # rysowanie konkretnej karty

		# obrazki potrzebne czasem (m. in. dopytanie o kolor karty)
		self.choose_image = pygame.image.load("choosing.png")
		self.choose_image_background = pygame.image.load("Choose_background.png")
		self.not_your_turn_image = pygame.image.load("not_your_turn.png")


	def start(self, turtle): # uruchomienie okna oraz dodanie informacji o żółwiu przydzielonym graczowi
		self.my_turtle = turtle
		self.draw_board.start(turtle)
		pygame.init()

	def end(self): # zamknięcie okna i wyłączenie gry
		pygame.quit()
		exit()
		pass

	def ask_if_needed(self, color, val): # dopytanie o to, jakim żółwiem należy poruszyć, jeśli karta pozwala na wybór
		if color == "RAINBOW":
			if (val != "^" and val != "^^"):
				# odpowiednia grafika
				self.screen.blit(self.choose_image_background, (0, 0))
				self.screen.blit(self.choose_image, (0, 0))
				pygame.display.update()
				while True:  # dopóki nie zostanie wybrane
					events = pygame.event.get()
					for e in events:
						if e.type == pygame.QUIT: # umożliwia zakończenie gry w dowolnym momencie (krzyżyk w prawym górnym rogu)
							self.end()
						if e.type == pygame.MOUSEBUTTONUP:  # zczytanie wybranego koloru żółwia
							position = pygame.mouse.get_pos()
							x, y = position
							if 360 < y < 505:
								if 346 < x < 502:
									return "RED"
								if 535 < x < 692:
									return "YELLOW"
								if 724 < x < 880:
									return "GREEN"
								if 915 < x < 1070:
									return "BLUE"
								if 1100 < x < 1255:
									return "PURPLE"
		return None

	def show(self, game_state): # aktualizacja planszy, bez możliwości wykonania ruchu
		state = game_state["game_state"]
		self.draw_board.draw(state["board"])
		self.screen.blit(self.not_your_turn_image, (0, 0))
		pygame.display.update()

	def go(self, game_state): # aktualizacja planszy + wykonanie ruchu

		# jeśli jest w trakcie gry
		if game_state["g_status"] == "game":
			state = game_state["game_state"]

			# narysowanie planszy
			self.draw_board.draw(state["board"])

			# wyświetlenie kart gracza
			i = 0
			for card in state["players"][self.player_key]:
				self.draw_card.draw(card, i)
				i += 1
			pygame.display.update()

			# wybranie karty do zagrania
			while True:
				events = pygame.event.get()
				for e in events:
					# umożliwienie zakończenia gry
					if e.type == pygame.QUIT:
						self.end()

					# sprawdzenie czy została wybrana karta
					if e.type == pygame.MOUSEBUTTONUP:  # jesli klikniecie
						position = pygame.mouse.get_pos()
						chosen = self.draw_card.chosen_card(position)

						# jeśli została wybrania karta to dopytanie się o dodatkowe informacje, jeśli są potrzebne
						# i zwrócenie całości
						if chosen:
							card = state["players"][self.player_key][chosen - 1]
							return {
								"color": card["color"],
								"val": card["val"],
								"choice": self.ask_if_needed(card["color"], card["val"])
							}

		# jeśli gra została już zakończona i chcemy pokazać wyniki
		elif game_state["g_status"] == "finished":
			ranking = game_state["ranking"]

			# jeśli gracz wygrał
			if ranking[0] == self.my_turtle:
				self.screen.blit(pygame.image.load("wygrana.png"), (0, 0))
				pygame.display.update()

			# jeśli gracz przegrał pokazujemy, który żółw wygrał
			else:
				self.screen.blit(pygame.image.load("przegrana.png"), (0, 0))
				pygame.display.update()
				if ranking[0] == "YELLOW":
					self.screen.blit(pygame.image.load("cyellow.png"), (655, 510))
				if ranking[0] == "RED":
					self.screen.blit(pygame.image.load("cred.png"), (655, 510))
				if ranking[0] == "BLUE":
					self.screen.blit(pygame.image.load("cblue.png"), (655, 510))
				if ranking[0] == "GREEN":
					self.screen.blit(pygame.image.load("cgreen.png"), (655, 510))
				if ranking[0] == "PURPLE":
					self.screen.blit(pygame.image.load("cpurple.png"), (655, 510))
				pygame.display.update()

			# czekamy na gracza, żeby kliknął, żeby miał czas zobaczyć wyniki
			while True:
				events = pygame.event.get()
				for e in events:
					if e.type == pygame.QUIT:
						self.end()
					if e.type == pygame.MOUSEBUTTONUP:
						self.end()
						return None

		# jeśli coś zadziałało źle zwracamy error
		else:
			self.state = "error"


class DrawBoard: # wyświetlenie planszy wraz z żółwiami na niej
	def __init__(self, screen):
		self.screen = screen
		self.draw_turtle = DrawTurtle(screen)
		self.board = pygame.image.load("board.png")
		self.fields = {  # umiejscowienie pól na obrazku
			0: [380, 1400], # pole startowe
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

		self.myturtles = {
			"YELLOW": pygame.image.load("myyellowturtle.png"),
			"RED": pygame.image.load("myredturtle.png"),
			"BLUE": pygame.image.load("myblueturtle.png"),
			"GREEN": pygame.image.load("mygreenturtle.png"),
			"PURPLE": pygame.image.load("mypurpleturtle.png")
		}

	def start(self, turtle): # ustawienie żółwia gracza
		self.myturtle = self.myturtles[turtle]

	def draw(self, state):  # wyświetlenie tła i żółwi w odpowiednich miejscach
		self.screen.blit(self.board, (0, 0))
		self.screen.blit(self.myturtle, (0, 0))
		# print(state)
		for j in range(len(state["0"])): # na polu startowym żółwie są obok siebie
			self.draw_turtle.draw(state["0"][j], (self.fields[0][1], self.fields[0][0] - j * 70))
			self.draw_turtle.draw(state["0"][j], (self.fields[0][1], self.fields[0][0] - j * 70))

		# a na pozostałych polach są jedne na drugich
		for i in range(1, len(state)):
			for j in range(len(state[str(i)])):
				self.draw_turtle.draw(state[str(i)][j], (self.fields[i][1], self.fields[i][0] - j * 15))


class DrawTurtle: # wyświetlenie żółwia
	def __init__(self, screen):
		self.images = {
			"YELLOW": pygame.image.load("yellow.png"),
			"RED": pygame.image.load("red.png"),
			"BLUE": pygame.image.load("blue.png"),
			"GREEN": pygame.image.load("green.png"),
			"PURPLE": pygame.image.load("purple.png")
		}
		self.screen = screen

	def draw(self, turtle, place): # wyświetlenie żółwia w odpowiednim kolorze w danym miejscu
		self.screen.blit(self.images[turtle], place)
		pygame.display.update()


class DrawCard: # wyświetlanie karty

	def __init__(self, screen):
		self.screen = screen

		# potrzebne grafiki, z których (odpowiednio wybranych) składa się każda karta
		self.background = pygame.image.load("card_background.png")
		self.colors = {
			"RAINBOW": pygame.image.load("crainbow.png"),  # jak wyzej, obrazki potem zmienimy
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
			0: (135, 550),
			1: (385, 550),
			2: (635, 550),
			3: (885, 550),
			4: (1135, 550)
		}

	def draw(self, card, field): # "złożenie" i wyświetlenie karty w miejscu odpowiadającym danemu polu
		place = self.places[field]
		self.screen.blit(self.background, place)
		self.screen.blit(self.colors[card["color"]], place)
		self.screen.blit(self.movement[card["val"]], place)

	def chosen_card(self, place): # sprawdzenie, czy i która karta została kliknięta
		x, y = place
		if y > 850:
			return False
		if y < 550:
			return False
		if 135 < x < 365:
			return 1
		if 365 < x < 615:
			return 2
		if 635 < x < 865:
			return 3
		if 885 < x < 1115:
			return 4
		if 1135 < x < 1365:
			return 5
		return False


if __name__ == "__main__": #testy
	gui = GUI("a")
	gui.start("YELLOW")

	from game import Game

	game = Game(["a"], 10)
	effect = 1
	state = game.get_state()
	while not game.is_finished:
		effect = gui.go({
			"g_status": "game",
			"game_state": state})
		game.card_on_desk("a", Card(effect["color"], effect["val"]), effect["choice"])
		state = game.get_state()

	gui.go({
		"g_status": "finished",
		"ranking": game.board.ranking
	})
	gui.end()
