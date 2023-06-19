from gui import GUI
from game import Game
from card import Card
import random

F = 10 # liczba pól, grafika jest na 10

N = int(input("Podaj liczbe graczy (dziala tylko dla 1)"))

player_info = {
	"nick": None,
	"gui": None,
	"turtle": None
}

turtles = ["YELLOW", "GREEN", "RED", "PURPLE", "BLUE"]
random.shuffle(turtles)

players = []
nicks = []

for i in range(N):
	players.append(player_info)
	players[i]["nick"] = input("Wpisz nick gracza " + str(i + 1) + ":\n")
	nicks.append(players[i]["nick"])
	players[i]["gui"] = GUI(players[i]["nick"])
	turtle = turtles.pop()
	players[i]["turtle"] = turtle
	players[i]["gui"].start(turtle)

game = Game(nicks, F)
state = game.get_state()
i = 0

while not game.is_finished:
	effect = players[i]["gui"].go({
		"g_status": "game",
		"game_state": state})
	while effect is None:
		break
	game.card_on_desk(players[i]["nick"], Card(effect["color"], effect["val"]), effect["choice"])
	state = game.get_state()
	i += 1
	if i >= N:
		i -= N

for p in players:
	p["gui"].go({
		"g_status": "finished",
		"ranking": game.board.ranking
	})
	p["gui"].end()

print(game.board.ranking)
print("A")