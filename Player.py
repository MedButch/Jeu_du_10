import Cards

class Player:
    def __init__(self, hand):
        self.hand = []
        hand.sort(key=lambda x: x.number)
        spades = list(filter(lambda x: x.number // 10 == 0, hand))
        diamonds = list(filter(lambda x: x.number // 10 == 1, hand))
        hearts = list(filter(lambda x: x.number // 10 == 2, hand))
        clovers = list(filter(lambda x: x.number // 10 == 3, hand))
        self.hand.append(spades)
        self.hand.append(diamonds)
        self.hand.append(hearts)
        self.hand.append(clovers)

    #Get playable cards in hand
    #Return suit of round or all other suits if that suit is not held
    def playableCards(self, suit):
        result = []
        #empty list is False
        if self.hand[suit]:
            result = self.hand[suit]
        else:
            for i in range(4):
                if i != suit and self.hand[i]:
                    result.append(self.hand[i])
        return result


    #Print out cards in hand
    def printHand(self):
        output = ""
        for suit in self.hand:
            for card in suit:
                output = output + str(card)
                output = output + " "
        print(output)