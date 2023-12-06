import math


def find_winning_strategies(data):
    for duration, record in data:
        distances = [speed * (duration - speed) for speed in range(duration)]
        winning = list(filter(lambda x: x > record, distances))
        yield len(winning)


part_1 = [(57, 291), (72, 1172), (69, 1176), (92, 2026)]
part_2 = [list(map(lambda x: int(''.join([str(i) for i in x])), list(zip(*part_1))))]  # lol, met de hand was sneller

print(math.prod(find_winning_strategies(part_1)))
print(math.prod(find_winning_strategies(part_2)))
