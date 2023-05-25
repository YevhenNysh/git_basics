import itertools
from enum import Enum

_ranks = [6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
_suits = {
    'spades': '\u2660',
    'hearts': '\u2665',
    'diamonds': '\u2666',
    'clubs': '\u2663'
}

class SuitEnum(Enum):

    def __str__(cls):
        return cls.value


Suit = SuitEnum('Suit', _suits)


class Card:
    __slots__ = 'rank', 'suit'  # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self) -> str:
        return str(self.rank) + " " + str(self.suit)


class CardDeckBase:

    def __init__(self, _ranks):
        self.deck = []
        p = itertools.product(_ranks, Suit)
        self.deck = [Card(rank, suit) for rank, suit in p]

    def __str__(self) -> str:
        string = ""
        return string.append(card for card in self.deck)
    
class FrenchDeck(CardDeckBase):
    french_ranks = [2,3,4,5,6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    special_rank = ["Joker"]
    special_suit = ["red", "black"]


    def __init__(self):
        super().__init__(self.french_ranks)
        p = itertools.product(self.special_rank, self.special_suit)
        for card in p:
            self.deck.append(Card(card[0],card[1]))
