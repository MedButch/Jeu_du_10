#Game logic
import Cards, Player

__name__ = "__main__"

def init_players(cards):
    players = [None] * 4
    hands = [[], [], [], []]
    for j in range(10):
        for i in range(4):
            hands[i].append(cards.pop())
    for i in range(4):
        players[i] = Player.Player(hands[i])
    return players

def bets(index):
    passed = [False] * 4
    value = 45
    while passed != [True, True, True, True]:
        if passed[index]:
            continue
        else:
            condition = True
            while condition:
                bet = int(input("Player " + str(index + 1) + " enter bet amount: "))
                if bet == 0:
                    passed[index] = True
                    condition = False
                elif bet == 100:
                    passed = [True] * 4
                    condition = False
                elif bet > value and bet % 5 == 0:
                    value = bet
                    condition = False
        index = (index + 1) % 4

def main():
    cards = Cards.initDeck()
    players = init_players(cards)
    bets(1)
    # for player in players:
    #     playable = player.playableCards(0 // 10)
    #     player.printHand()

if __name__ == "__main__":
    main()