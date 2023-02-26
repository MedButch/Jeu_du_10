import Cards

class Player:
    def __init__(self, hand):
        self.hand = hand

    #Print out cards in hand
    #Todo: show playable cards
    def printHand(self):
        output = ""
        for card in self.hand:
            output = output + str(card)
            output = output + " "
        print(output)