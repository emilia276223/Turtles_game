import requests
import json

HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain'}


class Connector: # klasa odpowiadająca za komunikację między klientem a serwerem
	def __init__(self, url, nick):
		# potrzebne informacje:
		self.url = "http://" + url + ":5000"
		data = {"name": nick}
		new_url = self.url+"/init"
		r = requests.post(new_url, data=json.dumps(data), headers=HEADERS)
		status = r.status_code
		if status == 200:  # zapytanie rest wykonało się poprawnie
			answer = r.content
			j = r.json()
			self.turtle = j["turtle"]
			self.ip = j["ip"]
			self.connected = True
		else:
			self.connected = False
			print("ERROR")

	def card_on_table(self, card): # podanie serwerowi informacji o wyłożeniu danej karty
		new_url = self.url+"/card"
		r = requests.post(new_url, data=json.dumps(card), headers=HEADERS)
		if r.status_code == 200:
			js = r.json()
			return js
		else:
			print("code", r.status_code, "url", new_url)


	def get_state(self): # odczytanie stanu gry od serwera
		new_url = self.url+"/getState"
		r = requests.get(new_url)
		if r.status_code == 200:
			js = r.json()
			return js
		else:
			print("code", r.status_code, "url", new_url)


if __name__ == "__main__": # testy
	url = "localhost"
	conn = Connector(url, "Burek") 
	if conn.connected:
		# print("turtle", conn.turtle)
		from time import time
		t = time()
		# for i in range(10):
			# print(conn.get_state())
		# print("time:", time()-t)
		# polozenie do 20 kart lub konca gry
		# for _ in range(20):
		# 	pass
			# sprawdzenie kart na ręku
			# losowanie
			# wybranie, danie karty
			# sprawdzenie czy koniec gry
	else:
		print("not connected :(")