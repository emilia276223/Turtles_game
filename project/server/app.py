from flask import Flask, render_template, request, flash
import random
from game import Game

app = Flask(__name__)

NUMBER_OF_FIELDS = 5 # 10 eccomended because of GUI
NUMBER_OF_REQUIRED_PLAYERS = 2

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
		self.N = NUMBER_OF_REQUIRED_PLAYERS # liczba potrzebnych graczy do gry

	def card_table(self, card, ip):  # polozenie karty
		c = None
		for cp in self.game.players[ip].cards:
			if cp.color == card["color"] and cp.val == card["val"]:
				c = cp
				break
		if card["color"] == "RAINBOW":
			self.game.card_on_desk(ip, c, card["choice"])
		else:
			self.game.card_on_desk(ip, c)
		# akcja na game - klade karte na stole # TODO # done
		# print("user {} gives card {}".format(ip, card)) # print("user", ip, "gives card", card)

	def user_init(self, ip, nick):
		user = UserInfo(nick)
		if self.game is None:
			self.users[ip] = user
			if len(self.users) == 1:
				self.turtles = ["YELLOW", "GREEN", "BLUE", "RED", "PURPLE"]
				random.shuffle(self.turtles)
			if len(self.users) == self.N:
				users_ip = []
				for ip in self.users:
					users_ip.append(ip)
				self.game = game_class(users_ip, NUMBER_OF_FIELDS) # TODO # done

		turtle = self.turtles.pop()
		user.turtle = turtle
		return turtle

	# print(self.users)

	def get_nick_list(self):
		nl = []
		for ip in self.users:
			nl.append(self.users[ip].nick)
		return nl

	def get_users_info(self):
		nl = []
		for ip in self.users:
			ui = self.users[ip]
			nl.append([ui.nick, ui.turtle])
		return nl

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
					"ranking": self.game.get_state(),
					"users_info": self.get_users_info()  # ma zwrócić informację o tym kto jakim żółwiem grał
				}
			else:
				return {
					"g_status": "game",
					"game_state": self.game.get_state(),
					"turn": self.game.get_ip_of_next()
				}


class UserInfo:
	def __init__(self, nick):
		self.nick = nick
		self.turtle = None

	def __repr__(self):
		return self.nick + ", " + str(self.turtle)


game_class = Game

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
	print("user {} has been connected from {}".format(nick, ip))
	turtle = server.user_init(ip, nick)
	return {"status": "connected", "turtle": turtle, "ip": ip}


@app.route('/card', methods=['POST'])
def card_on_board():  # CZY TO JEST DOBRZE???
	card = request.json
	ip = request.remote_addr
	server.card_table(card, ip) # TODO # done
	return server.get_state()


if __name__ == "__main__": # testy
	user = UserInfo("Adam")
	print(user)
	user.turtle = "PINK"
	print(user)
	# test klasy serwer # TODO # done
	card1 = {"color": "GREEN",
			 "val": "++"}
	card2 = {"color": "RAINBOW",
			 "val": "+",
			 "choice": "BLUE"}
	s = Server()
	s.user_init("1", "Adam")
	s.user_init("2", "Borys")
	s.user_init("3", "Cecylia")
	s.user_init("4", "Dominik")
	s.user_init("5", "Ewa")
	print(s.get_nick_list())
	print(s.get_users_info())
	print(s.get_state())
	c3 = s.game.whos_turn[0].get_cards()[0]
	print(s.game.whos_turn[0].get_cards()[0])
	card3 = {"color": c3.get_color(),
			 "val": c3.get_val()}
	if c3.get_color() == "RAINBOW":
		card3["choice"] = "GREEN"
	s.card_table(card3, "1")
	print(s.get_state())

