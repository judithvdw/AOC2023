from scipy.spatial.distance import cityblock


def get_coords(raw_map):
    coords = []
    for y in range(len(raw_map)):
        for x in range(len(raw_map[0])):
            if raw_map[y][x] == "#":
                coords.append((x, y))
    return coords


def adjust_coords(coords, factor):
    empty_rows = {i for i in range(len(raw_map[0]))} - {i[1] for i in coords}
    empty_cols = {i for i in range(len(raw_map))} - {i[0] for i in coords}
    for coord in coords:
        x, y = coord
        x += sum([x > i for i in empty_cols]) * factor
        y += sum([y > i for i in empty_rows]) * factor
        yield x, y


def get_distances(coord, coords):
    for compare in coords:
        yield cityblock(coord, compare)


def get_totals(coords):
    total = 0
    for coord in coords:
        total += sum(get_distances(coord, coords))
    return total // 2


with (open("inputs/11.txt") as f):
    raw_map = f.read().splitlines()
    coords = get_coords(raw_map)

print(f"Part 1: {get_totals(list(adjust_coords(coords, 1)))}")
print(f"Part 2: {get_totals(list(adjust_coords(coords, 999_999)))}")
