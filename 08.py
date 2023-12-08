import math
from itertools import cycle
import re


def parse_data(raw):
    instructions = raw[0].strip()
    network = raw[2:]
    network_dict = {}
    for nodes in network:
        a, b, c = re.findall(r"\w{3}", nodes)
        network_dict[a] = (b, c)
    return instructions, network_dict


def walk_graph(start, ends, network, instructions):
    steps = 0
    current = start
    for step in cycle(instructions):
        if current in ends:
            return steps
        steps += 1
        left, right = network[current]
        if step == "L":
            current = left
        else:
            current = right


with open("inputs/08.txt") as f:
    raw = f.readlines()

instructions, network = parse_data(raw)

print(f"Part 1{walk_graph("AAA", ["ZZZ"], network, instructions)}")

starts = list(filter(lambda x: x[2] == "A", network.keys()))
ends = list(filter(lambda x: x[2] == "Z", network.keys()))

lengths = []
for start in starts:
    lengths.append(walk_graph(start, ends, network, instructions))

print(f"Part 1: {math.lcm(*lengths)}")
