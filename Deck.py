from datascience import *
import numpy as np

StandardDeck = Table.read_table("Deck.csv")

#Deck class, with card subclasses
class Deck:
    count = 52 #keeps track of number of cards in the deck
    used, unused = [], [] #keeps track of used and unused cards each round

    def __init__(self):
        self.deck = StandardDeck

    def shuffle(self):
        self.deck = self.deck.sample(with_replacement=False) #shuffled
        for card in self.deck.rows:
            self.unused.append(Card(card.item("Face"), card.item("Suit"), card.item("Value")))

class Card:

    def __init__(self, face, suit, value):
        self.face, self.suit, self.value = face, suit, value
