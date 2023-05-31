from card import Card
from turtle import Turtle
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


if __name__ == "__main__":
	turtle1 = Turtle("GREEN")
	turtle2 = Turtle("PURPLE")
	player1 = Player(turtle1)
	player2 = Player(turtle2)
	card
