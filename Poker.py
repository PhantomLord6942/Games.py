# Evaluate poker hands
def evaluate_hand(hand):
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

    value_counts = {value: 0 for value in values}
    flush = len(set(suit for value, suit in hand)) == 1

    for value, suit in hand:
        value_counts[value] += 1

    is_straight = len(value_counts) == 5
    is_flush = flush
    kind_counts = set(value_counts.values())

    if is_straight and is_flush:
        return 9, values.index(hand[0][0])  # Straight flush
    elif kind_counts == {1}:
        return 6, values.index(hand[0][0])  # High card
    elif kind_counts == {2, 3}:
        return 1, values.index(max(value_counts, key=value_counts.get))  # One pair
    elif kind_counts == {1, 4}:
        return 2, values.index(max(value_counts, key=value_counts.get))  # Four of a kind
    # Add more combinations...

    return 0, values.index(hand[0][0])  # Default to high card


# In Game class play() method

# Evaluate hands
hand_scores = []
for player in self.players:
    hand_value, hand_high_card = evaluate_hand(player.hand)
    hand_scores.append((player, hand_value, hand_high_card))

# Find winner
winner = max(hand_scores, key=lambda x: (x[1], x[2]))
print(f'{winner[0].name} wins with {winner[1]}!')
# Pay out chips...
