from card import Card

class Player: # klasa gracz - przechowuje ip gracza i jego aktualne karty
	def __init__(self, ip): # w momencie dołączenia gracza do gry zapamiętujemy jego ip
		self.cards = []
		self.ip = ip

	def add_card(self, card): # dodanie dobranej ze stosu karty do kart na ręce
		self.cards.append(card)

	def remove_card(self, card): # usunięcie karty z ręki gracza - gracz zagrywa kartę
		for c in self.cards:
			if c.color == card.color and c.val == card.val:
				self.cards.remove(c)
				return True
		return False

	def get_state(self): # wypisanie aktualnych kart na ręce gracza
		state_cars_list = [c.get_state() for c in self.cards]
		return state_cars_list

if __name__ == "__main__": # testy
	# turtle1 = Turtle("GREEN")
	# turtle2 = Turtle("PURPLE")
	# player1 = Player(turtle1)
	# player2 = Player(turtle2)
	# card
	pass
