value_map = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8,
             "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}
value_map2 = {"A": 9, "2": 10, "3": 11, "4": 12, "5": 13, "6": 1, "7": 2,
              "8": 3, "9": 4, "10": 5, "J": 6, "Q": 7, "K": 8}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = value_map[rank]
        # something else


suits = input().split(',')
ranks = input().split(',')

cards = []
for i in range(5):
    cards.append(Card(suits[i], ranks[i]))
cards.sort(key=lambda x: x.value)
cards2 = sorted(cards, key=lambda x: value_map2[x.rank])

straight = True
flush = True
for i in range(4):
    if cards[i + 1].value - cards[i].value != 1 and \
            value_map2[cards2[i + 1].rank] - value_map2[cards2[i].rank] != 1:
        straight = False
    if cards[i + 1].suit != cards[i].suit:
        flush = False

four = False
if cards[1].rank == cards[2].rank == cards[3].rank and \
        (cards[0].rank == cards[1].rank or cards[4].rank == cards[1].rank):
    four = True

house = False
if (cards[1].rank == cards[2].rank == cards[0].rank and
    cards[3].rank == cards[4].rank) or \
        (cards[4].rank == cards[2].rank == cards[3].rank and
         cards[0].rank == cards[1].rank):
    house = True

score = 0
if straight and flush:
    score += 100
elif four:
    score += 20
    if cards[0].rank == "A" and cards[0].rank != cards[1].rank:
        score += 1
    if cards[4].rank == "A" and cards[4].rank != cards[3].rank:
        score += 1
elif house:
    score += 10
elif straight:
    score += 5
elif flush:
    score += 3
else:
    score = 0
    for i in range(len(cards) - 2):
        if cards[i + 1].value == cards[i].value:
            score += 2
            cards.pop(i + 1)
            cards.pop(i)
        if len(cards) < 2:
            break
    for card in cards:
        if card.rank == "A":
            score += 1

print(score)
