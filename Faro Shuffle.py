deck_of_cards = (input()).split()
number_of_splits = int(input())
for current_shuffle in range(number_of_splits):
    middle_part = len(deck_of_cards) // 2
    left_part = deck_of_cards[:middle_part]
    right_part = deck_of_cards[middle_part:]
    current_deck = []
    for card_index in range(middle_part):
        current_deck.append(left_part[card_index])
        current_deck.append(right_part[card_index])
    deck_of_cards = current_deck
print(deck_of_cards)
