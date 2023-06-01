from card import Card
from turtle import Turtle
class Player:
	def __init__(self, turtle, ip):
		self.cards = []
		self.turtle = turtle
		self.IP = ip

	def get_turtle(self): #del
		return self.turtle

	def add_card(self, card):
		self.cards.append(card)

	def get_cards(self): #del
		return self.cards

	def remove_card(self, card):
		self.cards.remove(card)

	def get_state(self):
		pass

if __name__ == "__main__":
	turtle1 = Turtle("GREEN")
	turtle2 = Turtle("PURPLE")
	player1 = Player(turtle1)
	player2 = Player(turtle2)
	card