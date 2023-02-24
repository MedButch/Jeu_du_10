class Card:

    def __init__(self, value, suit):
        self.value = self.values[value]
        self.suit = self.suits[suit]

    def __str__(self):
        return f"{self.value}{self.suit}"

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


print(Card('7', 'Pic'))
