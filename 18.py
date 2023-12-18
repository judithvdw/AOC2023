from itertools import pairwise


def parse_instructions(instructions, start=(0, 0)):
    coords = [start]
    x, y = start
    total_steps = 0
    for direction, steps, _ in instructions:
        x = x + (mapping[direction][0] * steps)
        y = y + (mapping[direction][1] * steps)
        coords.append((x, y))
        total_steps += steps
    return coords, total_steps


def calculate_total_area(coords, steps):
    pairs = []
    for (ax, ay), (bx, by) in pairwise(coords):
        pairs.append(ax * by - bx * ay)
    interior = abs(sum(pairs)) // 2 - steps // 2 + 1
    return interior + steps


with open("inputs/18.txt") as f:
    raw = [i.split() for i in f.read().splitlines()]

mapping = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
directions = {0: "R", 1: "D", 2: "L", 3: "U"}

instructions = list(map(lambda x: (x[0], int(x[1]), x[2][2:-1]), raw))
new_instructions = list(map(lambda x: (directions[int(x[2][-1])], int(x[2][:-1], 16), None), instructions))
print(f"Part 1: {calculate_total_area(*parse_instructions(instructions))}")
print(f"Part 2: {calculate_total_area(*parse_instructions(new_instructions))}")
