import cards
import random


class Deck:
    def __init__(self):
        self.card_index = 0
        self.cards_Deck = [cards.Card() for x in range(1, 10)]

    def __iter__(self):
        return self.cards_Deck[self.card_index]

    def __next__(self):
        if self.card_index > len(self.cards_deck):
            raise StopIteration
        self.card_index += 1
        return self.cards_Deck[self.card_index - 1]

    def __bool__(self):
        if self.cards_Deck:
            return True
        else:
            return False

    def shuffle_deck(self):
        return random.shuffle(self.cards_Deck)

    def deal(self):
        return self.cards_Deck.pop()


