import math


def get_symbol_locations(grid):
    symbols = {}
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if not grid[x][y].isnumeric() and grid[x][y] != ".":
                symbols[(x, y)] = grid[x][y]
    return symbols


def get_parts(grid):
    parts = {}
    for x in range(len(grid[0])):
        current_num_idxs = []
        current_num = ""
        adjacendness = False
        dx_dy = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1))
        for y in range(len(grid)):
            if grid[x][y].isnumeric():
                current_num += grid[x][y]
                current_num_idxs.append((x, y))
                for dx, dy in dx_dy:
                    if (x + dx, y + dy) in symbol_overview:
                        adjacendness = True
            else:
                if adjacendness:
                    parts[tuple(current_num_idxs)] = int(current_num)
                adjacendness = False
                current_num = ""
                current_num_idxs = []
        if adjacendness:
            parts[tuple(current_num_idxs)] = int(current_num)
    return parts


def get_gear_ratios(potential_gears, complete_overview_parts):
    gear_ratios = []
    for gear in potential_gears:
        adjacent_numbers = set()  # shortcut, if there is a gear is adjacent to two of the same number, it goes wrong
        dx_dy = ((0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, -1), (1, 1), (-1, -1))
        for dx, dy in dx_dy:
            if (gear[0] + dx, gear[1] + dy) in complete_overview_parts:
                adjacent_numbers.add(complete_overview_parts[(gear[0] + dx, gear[1] + dy)])
        if len(adjacent_numbers) == 2:
            gear_ratios.append(math.prod(adjacent_numbers))
    return gear_ratios


with open("inputs/03.txt") as f:
    grid = f.read()
    grid = grid.split("\n")

symbol_overview = get_symbol_locations(grid)
parts = get_parts(grid)

potential_gears = dict(filter(lambda x: x[1] == "*", symbol_overview.items()))
complete_overview_parts = {loc: v for k, v in parts.items() for loc in k}

print(f"Part 1: {sum(parts.values())}")
print(f"Part 2: {sum(get_gear_ratios(potential_gears, complete_overview_parts))}")
