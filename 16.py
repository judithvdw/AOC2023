from collections import deque


def find_beam(graph, source):
    visited = set()
    stack = deque()
    stack.append(source)
    grid_size = len(graph[0])

    direction_map = {
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
        "^": (0, -1)
    }

    while stack:
        s = stack.pop()
        if s not in visited:
            visited.add(s)
        else:
            continue
        x, y, direction = s
        dx, dy = direction_map[direction]
        x += dx
        y += dy
        if x >= grid_size or x < 0 or y >= grid_size or y < 0:
            continue
        next_shape = graph[y][x]
        if next_shape == ".":  # direction stays the same
            stack.append((x, y, direction))
        elif next_shape == "|":
            if direction in "<>":
                stack.append((x, y, "^"))
                stack.append((x, y, "v"))
            else:
                stack.append((x, y, direction))
        elif next_shape == "-":
            if direction in "v^":
                stack.append((x, y, "<"))
                stack.append((x, y, ">"))
            else:
                stack.append((x, y, direction))
        elif next_shape == "/":
            if direction == ">":
                stack.append((x, y, "^"))
            if direction == "v":
                stack.append((x, y, "<"))
            if direction == "<":
                stack.append((x, y, "v"))
            if direction == "^":
                stack.append((x, y, ">"))
        elif next_shape == "\\":
            if direction == ">":
                stack.append((x, y, "v"))
            if direction == "v":
                stack.append((x, y, ">"))
            if direction == "<":
                stack.append((x, y, "^"))
            if direction == "^":
                stack.append((x, y, "<"))

    return visited


with open("inputs/16.txt") as f:
    mirror_map = f.read().splitlines()

start = (-1, 0, ">")
locations = find_beam(mirror_map, start)
unique_locations = {(x, y) for x, y, _ in locations}

print(len(unique_locations) - 1)

top = ((i, -1, "v") for i in range(len(mirror_map)))
left = ((-1, i, ">") for i in range(len(mirror_map)))
right = ((len(mirror_map), i, "<") for i in range(len(mirror_map)))
bottom = ((i, len(mirror_map), "^") for i in range(len(mirror_map)))

lengths = []
for start in [*top, *left, *right, *bottom]:
    locations = find_beam(mirror_map, start)
    unique_locations = {(x, y) for x, y, _ in locations}
    lengths.append(len(unique_locations) - 1)

print(max(lengths))
