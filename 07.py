from collections import Counter


def get_type(hand):
    hand = Counter(hand)
    if hand.most_common()[0][1] == 5:
        return 1 # five of a kind
    elif hand.most_common()[0][1] == 4:
        return 2 # four of a kind
    elif hand.most_common()[0][1] == 3 and hand.most_common()[1][1] == 2:
        return 3 # full house
    elif hand.most_common()[0][1] == 3:
        return 4 # three of a kind
    elif hand.most_common()[0][1] == 2 and hand.most_common()[1][1] == 2:
        return 5 # two pair
    elif hand.most_common()[0][1] == 2:
        return 6 # pair
    else:
        return 7 # highest number


def get_type_with_jokers(hand):
    hand = Counter(hand)
    num_jokers = hand["J"]
    if hand.most_common()[0][1] == 5:
        return 1  # 5 of a kind
    elif hand.most_common()[0][1] == 4:
        return 1
    elif hand.most_common()[0][1] == 3 and hand.most_common()[1][1] == 2:
        return 1
    elif hand.most_common()[0][1] == 3:
        return 2  # 4 of a kind
    elif hand.most_common()[0][1] == 2 and hand.most_common()[1][1] == 2:
        if num_jokers == 2:
            return 2
        else:  # num_jokers == 1
            return 3  # full house
    elif hand.most_common()[0][1] == 2:
        return 4  # three of a kind
    else:
        return 6  # two of a kind


def parse_data(data):
    for d in data:
        hand, bid = d.split()
        hand_type = get_type(hand)
        if "J" not in hand:
            hand_type_joker = hand_type
        else:
            hand_type_joker = get_type_with_jokers(hand)
        yield hand, int(bid), hand_type, hand_type_joker


with open("inputs/07.txt") as f:
    raw = f.readlines()
    hands = parse_data(raw)
    card_values = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    sorted_hands = sorted(hands, key=lambda x: (
        x[2], card_values.index(x[0][0]), card_values.index(x[0][1]), card_values.index(x[0][2]),
        card_values.index(x[0][3]), card_values.index(x[0][4])))[::-1]

    total = 0
    for i, hand in enumerate(sorted_hands):
        total += hand[1] * (i + 1)

    print(f"Part 1: {total}")

    card_values = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    hands = parse_data(raw)
    sorted_hands_pt2 = sorted(hands, key=lambda x: (
        x[3], card_values.index(x[0][0]), card_values.index(x[0][1]), card_values.index(x[0][2]),
        card_values.index(x[0][3]), card_values.index(x[0][4])))[::-1]

    total = 0
    for i, hand in enumerate(sorted_hands_pt2):
        total += hand[1] * (i + 1)

    print(f"Part 2: {total}")
