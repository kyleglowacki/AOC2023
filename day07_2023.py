import aocd
from collections import Counter

def get_distribution(hand):
    #print(Counter(hand))
    return dict(Counter(hand))


def eval_distribution(hand_count):
    global SCORE
    #print(SCORE)
    #print(hand_count)
    # Check the 7 possible hands
    for t in SCORE:
        if len(hand_count) == t[0]:
            for key, value in hand_count.items():
                if value == t[1]:
                    return t[2]

    print("FOUND NOTHING - ERROR")
    return -1

def orig():
    return "23456789TJQKA"
def dumb():
    return "J23456789TQKA"
def val(card, order = orig):
    v = order().find(card)+2
    if v == -1:
        print(f"ERROR CARD VALUE MISSING - {card}")
    return v

def dump(dist):
    d = []
    for k, v in dist.items():
        d.append([k,v])
    return d

def card_values_with_frequency(dist, amt):
    cards = dump(dist)
    vals = []
    for c in cards:
        if c[1] == amt:
            vals.append(val(c[0]))
    vals.sort()
    vals.reverse()
    #print(f"High to low = {vals}")
    return vals

def card_with_frequency(dist, amt):
    for k, v in dist.items():
        if v == amt:
            return k
    #print(f"No cards with {amt} many cards")
    return None

def compute_type(dist):
    hand_type = 0
    if len(dist) == 1:
        hand_type = 7
        # 5 of a kind
    # Two diff cards
    if len(dist) == 2:
        if card_with_frequency(dist, 4) is not None:
            hand_type = 6
            # 4 of a kind
        else:
            # full house
            hand_type = 5
    if len(dist) == 3:
        if card_with_frequency(dist, 3) is not None:
            hand_type = 4
            # 3 of a kind + 2 diff
        else:
            # 2 pair + 1 card
            hand_type = 3
    if len(dist) == 4:
        # 1 pair + 3 cards
        hand_type = 2
    if len(dist) == 5:
        # high card
        hand_type = 1
    return hand_type

def compute_wildtype(dist):
    hand_type = 0
    if len(dist) == 1:
        hand_type = 7
        # 5 of a kind
    # Two diff cards
    if len(dist) == 2:
        if card_with_frequency(dist, 4) is not None:
            hand_type = 6
            # 4 of a kind
        else:
            # full house
            hand_type = 5
    if len(dist) == 3:
        if card_with_frequency(dist, 3) is not None:
            hand_type = 4
            # 3 of a kind + 2 diff
        else:
            # 2 pair + 1 card
            hand_type = 3
    if len(dist) == 4:
        # 1 pair + 3 cards
        hand_type = 2
    if len(dist) == 5:
        # high card
        hand_type = 1
    return hand_type

class Hand():
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid
        self.dist = get_distribution(self.cards)
        self.hand_type = compute_type(self.dist)
        self.wild_type = compute_wildtype(self.dist)

    def __str__(self):
        return f"{self.cards} = {self.bid} with score of {self.score}"
        
    #def __lt__(self, other):
    #    return self.score < other.score
    def __lt__(self, other):
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        else:
            # equal.. so walk through cards
            idx = 0
            while self.cards[idx] == other.cards[idx]:
                idx += 1
            # FOR first star...
            #return val(self.cards[idx]) < val(other.cards[idx])
            return val(self.cards[idx], dumb) < val(other.cards[idx], dumb)
        
raw = aocd.get_data(day=7, year=2023)
data = raw.splitlines()
#print(len(data))
#data = ['32T3K 765','T55J5 684','KK677 28','KTJJT 220','QQQJA 483']

hands = []
t = 0
r = 0


for line in data:
    d = {}
    card,bid = line.split()
    bid = int(bid)
    hand = Hand(card, bid)
    hands.append(hand)


total = 0
print("******************* FIRST STAR ***************")
hands.sort()
rank = 1
for hand in hands:
    total += rank * hand.bid
    rank += 1

print(f"FIRST total = 248812215")


total = 0
print("********** SECOND STAR *************")
# 248936974 too low
hands.sort()
rank = 1
for hand in hands:
    total += rank * hand.bid
    rank += 1

print(f"SECOND total = {total}")
