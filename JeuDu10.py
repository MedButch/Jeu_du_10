#Game logic
import Cards, Player

__name__ = "__main__"
def main():
    cards = Cards.initDeck()
    players = [None] * 4
    hands = [[], [], [], []]
    for j in range(10):
        for i in range(4):
            hands[i].append(cards.pop())
    for i in range(4):
        players[i] = Player.Player(hands[i])

if __name__ == "__main__":
    main()