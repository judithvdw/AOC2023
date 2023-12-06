import math


def num_winning(stats):
    duration, record = stats
    a = -1
    b = duration
    c = -record
    low, high = ((-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a), ((-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a)
    return math.floor(high) - math.floor(low)


part_1 = [(57, 291), (72, 1172), (69, 1176), (92, 2026)]
part_2 = [list(map(lambda x: int(''.join([str(i) for i in x])), list(zip(*part_1))))]  # lol, met de hand was sneller

print(f"Part 1: {math.prod(list(map(num_winning, part_1)))}")
print(f"Part 2: {math.prod(list(map(num_winning, part_2)))}")
