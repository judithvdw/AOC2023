def parse_data(raw):
    winning_nrs = []
    for line in raw:
        nr, data = line.split(":")
        my, winning = data.split("|")
        my = set(map(int, my.split()))
        winning = set(map(int, winning.split()))
        my_winning = my & winning
        winning_nrs.append(len(my_winning))
    return winning_nrs


with open("inputs/04.txt") as f:
    raw = f.readlines()
    number_of_winning_numbers = parse_data(raw)
    points = map(lambda x: 2 ** (x - 1) if x > 0 else 0, number_of_winning_numbers)
    print(f"Part 1: {sum(points)}")

    cards = [1] * len(number_of_winning_numbers)
    for i, n in enumerate(number_of_winning_numbers):
        amount = cards[i]
        for j in range(i+1, i + n + 1):
            cards[j] += amount
    print(f"Part 2: {sum(cards)}")

