def parse(raw_data):
    all_games = {}
    for game in raw_data:
        header, info = game.split(": ")
        game_nr = int(header.split()[1])
        cube_sets = []
        for game_round in info.split("; "):
            for colour in game_round.split(", "):
                n, col = colour.split()
                cube_sets.append((int(n), col))
        all_games[game_nr] = cube_sets
    return all_games


def part1(all_games):
    total = 0
    valids = {"red": 12, "green": 13, "blue": 14}
    for nr, cubes in all_games.items():
        for cube in cubes:
            if cube[0] > valids[cube[1]]:
                break
        else:
            total += nr
    return total


def part2(all_games):
    powers = []
    for nr, cubes in all_games.items():
        reds, greens, blues = [], [], []
        for cube in cubes:
            if cube[1] == "blue":
                blues.append(cube[0])
            if cube[1] == "green":
                greens.append(cube[0])
            if cube[1] == "red":
                reds.append(cube[0])
        powers.append(max(reds) * max(greens) * max(blues))
    return sum(powers)


with open("inputs/02.txt") as f:
    raw_data = f.readlines()
    all_games = parse(raw_data)

print(f"Part 1: {part1(all_games)}")
print(f"Part 2: {part2(all_games)}")
