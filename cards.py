import random


class Card:
    def __init__(self):
        card_color = ['red', 'blue', 'green', 'yellow']
        self.type = random.choice(card_color)
        card_number = [x for x in range(1, 10)]
        self.number = random.choice(card_number)

    def __iter__(self):
        return self.type , self.number

    def __next__(self):
        return self.type , self.number

