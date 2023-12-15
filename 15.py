from collections import defaultdict


def run_hashing(step):
    current = 0
    for letter in step:
        current += ord(letter)
        current *= 17
        current %= 256
    return current


with open("inputs/15.txt") as f:
    steps = f.readline().split(",")
    print(f"Part 1: {sum(list(map(run_hashing, steps)))}")

    boxes = defaultdict(dict)
    for step in steps:
        if "-" in step:
            label = step[:-1]
            box_number = run_hashing(label)
            if label in boxes[box_number]:
                del boxes[box_number][label]
        if "=" in step:
            label, lens = step.split("=")
            box_number = run_hashing(label)
            lens = int(lens)
            boxes[box_number][label] = lens

    focussing_power = 0
    for box_number, lenses in boxes.items():
        for i, lens_strength in enumerate(lenses.values(), start=1):
            focussing_power += (box_number + 1) * i * lens_strength

    print(f"Part 2: {focussing_power}")
