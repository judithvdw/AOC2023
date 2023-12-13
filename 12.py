from functools import cache


@cache
def find_variations(springs, report, curr_group_length=0):
    if len(springs) <= 0:
        return len(report) <= 0 and curr_group_length <= 0
    solutions = 0
    if springs[0] == "?":
        options = "#."
    else:
        options = springs[0]
    for option in options:
        if option == "#":
            solutions += find_variations(springs[1:], report, curr_group_length + 1)
        else:
            if curr_group_length > 0:
                if len(report) > 0 and report[0] == curr_group_length:
                    solutions += find_variations(springs[1:], report[1:])
            else:
                solutions += find_variations(springs[1:], report)
    return solutions


with open("inputs/12.txt") as f:
    data = f.read().splitlines()

reports = []
for line in data:
    springs, info = line.split()
    info = tuple(map(int, info.split(",")))
    reports.append((springs, info))

print(f"Part 1: {sum([find_variations(springs + ".", report) for springs, report in reports])}")
print(f"Part 2: {sum([find_variations("?".join([springs] * 5) + ".", report * 5) for springs, report in reports])}")