class Player:
	def __init__(self, turtle):
		self.cards = []
		self.turtle = turtle

	def get_turtle(self):
		return self.turtle

	def add_card(self, card):
		self.cards.append(card)

	def get_cards(self):
		return self.cards

	def remove_card(self, card):
		self.cards.remove(card)