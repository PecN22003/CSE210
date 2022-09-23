from random import randint

class suit:
    def __init__(this, name) -> None:
        this.name = name
        this.symbol = {"clubs": "♣", "hearts": "♥", "spades": "♠", "diamonds": "♦"}[name.lower()]

class card:
    def __init__(this, suit, value):
        this.suit = suit
        this.value = value
    def __str__(this):
        return f"{this.suit.symbol} {this.value}"
        

def main ():
    points = 300
    deck = []
    for i in ["clubs", "hearts", "spades", "diamonds"]:
        for j in range(13):
            deck.append(card(suit(i),j+1))
    current_card = deck.pop(randint(0, len(deck)-1))
    while points > 0:
        print(f"The card is: {current_card}")
        guess_is_higher = input("Higher or lower? [h/l]")[0].lower()
        print(guess_is_higher)
        guess_is_higher = guess_is_higher == "h"
        next_card =deck.pop(randint(0, len(deck)-1))
        print(f"Next card was: {next_card}")
        print(guess_is_higher, next_card.value>current_card.value, )
        if (guess_is_higher and next_card.value > current_card.value) or ((not guess_is_higher) and next_card.value < current_card.value):
            points += 100
        else:
            points -= 75
        print(f"Your score is {points}")
        current_card = next_card
        if input("Play again? [y/n]")[0].lower() == "n":
            break
        print()


if __name__ == "__main__":
    main()