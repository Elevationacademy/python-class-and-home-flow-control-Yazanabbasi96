import deck

my_deck = deck.Deck()

PoppedCard = my_deck.deal()
print(PoppedCard.number, PoppedCard.type)

for i in my_deck.cards_Deck:
    print(next(i))

for i in range(len(my_deck.cards_Deck)):
    my_deck.deal()

if my_deck:
    card = my_deck.deal()
else:
    print("My deck is empty")
