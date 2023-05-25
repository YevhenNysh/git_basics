import random
from cards import *

cardDeck = FrenchDeck()
random.shuffle(cardDeck.deck)

n = int(input("Скільки карт ви хочете отримати?")) 

for card in cardDeck.deck[:n]:
    print(card)