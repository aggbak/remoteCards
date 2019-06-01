import socket

class Card:
	#Static variables for checking
	faces = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
	faces_string_map = {
		"A":"Ace",
		"J":"Jack",
		"Q":"Queen",
		"K":"King"
	}
	suit_map = {
		"S":"spades",
		"H":"hearts",
		"D":"diamonds",
		"C":"clubs"
	}
	def __init__(self, face, suit):
		if not Card.isValidFace(face) or not Card.isValidSuit(suit):
			raise Exception("Invalid card")
		else:
			self.face = face
			self.suit = suit

	@staticmethod			
	def isValidFace(face):
		return str(face) in Card.faces 

	@staticmethod
	def isValidSuit(suit):
		return suit in Card.suit_map.keys()

	def codedOutput(self):
		return "Card: %s of %s" % (face, suit)
	
	@staticmethod
	def standardDeck():
		deck = []
		for face in Card.faces:
			for suit in Card.suit_map.keys():
				deck.append(Card(face, suit))
		return deck

	@staticmethod
	def faceAsString(face):
		if face in Card.faces_string_map.keys():
			return Card.faces_string_map[face]
		else:
			return face

	def __repr__(self):
		return "%s of %s" % (Card.faceAsString(self.face), Card.suit_map[self.suit])

def main():
	print Card.standardDeck()

if __name__ == "__main__":
	main()
