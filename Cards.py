# Card module and initialisation of deck
import math
import random

values = {
    0: '5',
    1: '6',
    2: '7',
    3: '8',
    4: '9',
    5: '10',
    6: 'J',
    7: 'Q',
    8: 'K',
    9: 'A'
}

suits = {
    0: '♠',
    1: '♦',
    2: '♥',
    3: '♣'
}


class Card:

    def __init__(self, number):
        self.number = number
        self.value = values[number % 10]
        self.suit = suits[number // 10]

    def __str__(self):
        return f"{self.value}{self.suit}"


def initDeck():
    cards = []
    for number in range(40):
        card = Card(number)
        cards.append(card)
    temp = []
    while (len(cards) > 0):
        i = math.floor(random.random() * len(cards))
        temp.append(cards.pop(i))
    cards = temp
    return cards
