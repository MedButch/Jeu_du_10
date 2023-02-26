# Card module and initialisation of deck
import math
import random

values = {
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

suits = {
    'Pic': '♠',
    'Carreau': '♦',
    'Coeur': '♥',
    'Trèfle': '♣'
}


class Card:

    def __init__(self, value, suit):
        # print(type(value))
        # print(type(suit))
        self.value = values[value]
        self.suit = suits[suit]

    def __str__(self):
        return f"{self.value}{self.suit}"


def initDeck():
    cards = []
    for suit in suits:
        for value in values:
            # print(value)
            # print(suit)
            card = Card(value, suit)
            cards.append(card)
    temp = []
    while (len(cards) > 0):
        i = math.floor(random.random() * len(cards))
        temp.append(cards.pop(i))
    cards = temp
    return cards
