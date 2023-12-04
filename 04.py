def parse_data(raw):
    my_nrs = []
    winning_nrs = []
    for line in raw:
        nr, data = line.split(":")
        my, winning = data.split("|")
        my = set(map(int, my.split()))
        winning = set(map(int, winning.split()))
        my_nrs.append(my)
        winning_nrs.append(winning)
    return my_nrs, winning_nrs


with open("inputs/04.txt") as f:
    raw = f.readlines()
    my_nrs, winning_nrs = parse_data(raw)
    totals = 0
    for my, winning in zip(my_nrs, winning_nrs):
        my_winning = my & winning
        points = 2 ** (len(my_winning) - 1) if len(my_winning) > 0 else 0
        totals += points
    print(totals)