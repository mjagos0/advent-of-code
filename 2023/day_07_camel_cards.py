from collections import Counter


def day_7_p1(input):
    cards_priority = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    def classify_hand(cards):
        cnt = Counter(cards)
        nkeys = len(cnt.keys())
        maxcnt = max(cnt.values())
        if maxcnt == 5:
            return 6
        elif maxcnt == 4:
            return 5
        elif maxcnt == 3:
            if nkeys == 2:
                return 4
            else:
                return 3
        elif maxcnt == 2:
            if nkeys == 3:
                return 2
            else:
                return 1
        else:
            return 0

    input = input.split('\n')
    hands = []
    for hand in input:
        cards, bet = hand.split(' ')
        stregth = classify_hand(cards)
        hands.append((cards, stregth, int(bet)))

    hands = sorted(hands, key=lambda x: (x[1], [cards_priority[card] for card in x[0]]))
    winnings = 0
    for i, h in enumerate(hands):
        winnings += (i+1)*h[2]

    return winnings


def day_7_p2(input):
    cards_priority = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 1,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    def classify_hand(cards):
        jokers = cards.count('J')
        if jokers == 5:
            return 6
        cards = cards.replace('J', '')
        cnt = Counter(cards)
        nkeys = len(cnt.keys())
        maxcnt = max(cnt.values())
        if maxcnt+jokers == 5:
            return 6
        elif maxcnt+jokers == 4:
            return 5
        elif maxcnt+jokers == 3:
            if jokers in (0, 1) and nkeys == 2:
                return 4
            else:
                return 3
        elif maxcnt+jokers == 2:
            if jokers in (0, 1) and nkeys == 3:
                return 2
            else:
                return 1
        else:
            return 0

    input = input.split('\n')
    hands = []
    for hand in input:
        cards, bet = hand.split(' ')
        stregth = classify_hand(cards)
        hands.append((cards, stregth, int(bet)))

    hands = sorted(hands, key=lambda x: (x[1], [cards_priority[card] for card in x[0]]))
    winnings = 0
    for i, h in enumerate(hands):
        winnings += (i+1)*h[2]

    return winnings

with open('../input.txt') as f:
    input = f.read()

sample = '''32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483'''

# print(day_7_p1(input))
print(day_7_p2(input))
