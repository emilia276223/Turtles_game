from card import Card
# from card import Card
# from turtle import Turtle
class Player:
	def __init__(self, ip):
		self.cards = []
		# self.turtle = turtle
		self.IP = ip

	# def get_turtle(self): #del
	# 	return self.turtle

	def get_ip(self):
		return self.IP

	def add_card(self, card):
		self.cards.append(card)

	def get_cards(self): #del
		return self.cards

	def remove_card(self, card):
		for c in self.cards:
			if c.color == card.color and c.val == card.val:
				self.cards.remove(c)
				return True
		return False
		# self.cards.remove(card)

	def get_state(self):
		state_cars_list = [c.get_state() for c in self.cards]
		return state_cars_list

if __name__ == "__main__":
	# turtle1 = Turtle("GREEN")
	# turtle2 = Turtle("PURPLE")
	# player1 = Player(turtle1)
	# player2 = Player(turtle2)
	# card
	pass
