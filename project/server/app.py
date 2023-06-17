"""
from flask import Flask, render_template, request, flash

app = Flask(__name__)

@app.route("/getState")
def getState():
	# return render_template("getState.html")
	return "get state"
"""

from flask import Flask, render_template, request, flash
import random

app = Flask(__name__)


class GameMock:  # do testow
	def __init__(self):
		self.is_finished = False
		self.ranking = ["YELLOW", "GREEN", "BLUE", "RED", "PURPLE"]
		self.counter = 0

	def get_state(self):
		self.counter += 1
		if self.counter >= 8:
			self.is_finished = True
		return {"data": "mock data"}

	# dodać z 3 różne rzeczywiste stany odpowiednio na środek gry i koniec

	def card_on_desk(self, player, card):  # zwraca dokładnie tę samą kartę
		# cadd on s
		return card


class Server:
	def __init__(self):
		self.users = {}
		self.game = None

	def cart_table(self, card, ip):  # polozenie karty
		print("user", ip, "gives card", card)

	def user_init(self, ip, nick):
		user = UserInfo(nick)
		if self.game is None:
			self.users[ip] = user
			if len(self.users) == 1:
				self.turtles = ["YELLOW", "GREEN", "BLUE", "RED", "PURPLE"]
				random.shuffle(self.turtles)
			if len(self.users) == 5:
				self.game = game_class()

		turtle = self.turtles.pop()
		user.turtle = turtle
		return turtle

	# print(self.users)

	def get_nick_list(self):
		nl = []
		for ip in self.users:
			nl.append(self.users[ip].nick)

	def get_users_info(self):
		nl = []
		for ip in self.users:
			ui = self.users[ip]
			nl.append([ui.nick, ui.turtle])

	def get_state(self):
		if self.game is None:
			return {
				"g_status": "not started",
				"users": self.get_nick_list()
			}
		else:
			if self.game.is_finished:
				return {
					"g_status": "finished",
					"ranking": self.game.ranking,
					"users_info": self.get_users_info()  # ma zwrócić informację o tym kto jakim żółwiem grał
				}
			else:
				return {
					"g_status": "game",
					"game_state": self.game.get_state()
				}


class UserInfo:
	def __init__(self, nick):
		self.nick = nick
		self.turtle = None

	def __repr__(self):
		return self.nick + ", " + str(self.turtle)


game_class = GameMock

server = Server()


@app.route("/getState")
def getState():
	# return render_template("getState.html")
	state = server.get_state()
	print(state)
	return state


@app.route('/init', methods=['POST'])  # podłączenie użytkownika
def client_init():
	nick = request.json['name']  # obiekt request pochodzi od flaska poprzez @app.route
	ip = request.remote_addr
	print("user ", nick, " has been connected from", ip)
	turtle = server.user_init(ip, nick)
	return {"status": "connected", "turtle": turtle}


@app.route('/card', methods=['POST'])
def card_on_board():  # CZY TO JEST DOBRZE???
	card = request.json['card']
	server.cart_table(card)
	return {"status": "card posted"}


if __name__ == "__main__":
	user = UserInfo("Adam")
	print(user)
	user.turtle = "PINK"
	print(user)

