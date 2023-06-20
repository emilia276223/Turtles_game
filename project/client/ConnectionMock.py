from server.app import Server

# potrzebne jedynie do testów
class ConnectionMock:
	def __init__(self, url, nick):
		self.ip = "mock_ip"  # to chyba bedzie trzeba zmienic ale to sie jeszcze okaze
		self.nick = nick
		self.server = Server()
		self.turtle = self.server.user_init(self.ip, self.nick)

	def card_to_dict(self, card):
		return {
			"color": card.color,
			"val": card.val
		}
	def card_on_table(self, card):
		self.server.card_table(card, self.ip)
		return self.server.get_state()

	def get_state(self):
		return self.server.get_state()