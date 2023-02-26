#Game logic
import Cards

__name__ = "__main__"
def main():
    cards = Cards.initDeck()
    for card in cards:
        print(card)

if __name__ == "__main__":
    main()