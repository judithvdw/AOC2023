def parse_data(raw):
    raw = raw.split("\n\n")
    seeds, infomaps = raw[0], raw[1:]
    seeds = list(map(int, seeds.split()[1:]))
    seed_ranges = list(zip(seeds[::2], seeds[1::2]))
    infomaps = [[tuple(map(int, row.split())) for row in map_data.split("\n")[1:]] for map_data in infomaps]
    return seeds, seed_ranges, infomaps


def get_next_nr(number, info_map):
    for dest_range_start, source_range_start, range_length in info_map:
        if source_range_start <= number < (source_range_start + range_length):
            return dest_range_start + (number - source_range_start)
    return number


def get_prev_nr(number, info_map):
    for dest_range_start, source_range_start, range_length in info_map:
        if dest_range_start <= number < (dest_range_start + range_length):
            return source_range_start + (number - dest_range_start)
    return number


def from_location_to_seed(number, info_maps):
    for info_map in info_maps:
        number = get_prev_nr(number, info_map)
    return number


def check_range(seed, seed_ranges):
    for start, range_length in seed_ranges:
        if start <= seed < (start + range_length):
            return True
    return False


with open("inputs/05t.txt") as f:
    raw = f.read()
    seeds, seed_ranges, info_maps = parse_data(raw)

destinations = []
for seed in seeds:
    number = seed
    for info_map in info_maps:
        number = get_next_nr(number, info_map)
    destinations.append(number)

print(f"Part 1: {min(destinations)}")

location = 0
while True:
    seed = from_location_to_seed(location, info_maps[::-1])
    print(location, seed, location - seed)
    if check_range(seed, seed_ranges):
        print(f"Part 2: {location}")
        break
    location += 1
