import requests
import json


HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


class Connector:
	def __init__(self, url, nick):
		self.url = url
		data = {"name": nick}
		new_url = self.url+"/init"
		r = requests.post(new_url, data=json.dumps(data), headers=HEADERS)
		status = r.status_code
		print("status", status)
		if status == 200:  # zapytanie rest wykonało się poprawnie
			answer = r.content
			j = r.json()
			print(answer, j)
			print(j["status"])
			self.turtle = j["turtle"]
			self.ip = j["ip"]
			self.connected = True
		else:
			self.connected = False

	def card_on_table(self, card):
		r = requests.post(self.url+"/card", data=json.dumps(card), headers=HEADERS)
		if r.status_code == 200:
			js = r.json()
			return js
		else:
			print("code", r.status_code, "url", new_url)


	def get_state(self):
		new_url = self.url+"/getState"
		r = requests.get(new_url)
		if r.status_code == 200:
			js = r.json()
			return js
		else:
			print("code", r.status_code, "url", new_url)


if __name__ == "__main__":
	url = "http://localhost:5000"
	conn = Connector(url, "Burek") 
	if conn.connected:
		print("turtle", conn.turtle)
		from time import time
		t = time()
		for i in range(10):
			print(conn.get_state())
		print("time:", time()-t)
		# polozenie do 20 kart lub konca gry
		for _ in range(20):
			pass
			# sprawdzenie kart na ręku
			# losowanie
			# wybranie, danie karty
			# sprawdzenie czy koniec gry
	else:
		print("not connected :(")

	import random


	# przy okazji bedziemy sprawdzac czy kladzenie karty dziala poprawnie
	#
	# koniec = False
	# players = ["a"]
	# colors = ["RED", "GREEN", "BLUE", "PURPLE", "YELLOW"]
	# g = Game(players, 10)
	# print(g.get_state())
	# i = 0
	# while not g.is_finished:
	# 	p = players[0]
	# 	c = random.choice(colors)
	# 	card = g.players[p].cards[random.randint(0, 4)]
	# 	g.card_on_desk(p, card, c)
	# 	state = g.get_state()
	# 	print(state)
	# 	i += 1
	# 	if i == 20:
	# 		koniec = True
	# 		break
	# print("gra skonczyla sie po {} krokach".format(i))
	# print("czy gra sie skonczyla? ", not koniec)