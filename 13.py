def clean_pattern(pattern):
    new = []
    for line in pattern.split():
        new_line = []
        for item in line.strip():
            if item == ".":
                new_line.append(False)
            if item == "#":
                new_line.append(True)
        new.append(new_line)
    return new


def find_reflection(pattern, smudges):
    for i in range(1, len(pattern)):
        left = pattern[:i]
        right = pattern[i:]
        smallest = min(len(left), len(right))
        left = left[-smallest:]
        right = right[:smallest][::-1]
        result = 0
        for x in range(len(left)):
            for y in range(len(left[0])):
                result += abs(left[x][y] - right[x][y])
        if result == smudges:
            return i
    return 0


with open("inputs/13.txt") as f:
    raw = f.read().split("\n\n")
    patterns = list(map(clean_pattern, raw))

print(f"Part 1: {sum([(find_reflection(pattern, 0) * 100 + find_reflection(list(zip(*pattern)), 0)) for pattern in patterns])}")
print(f"Part 2: {sum([(find_reflection(pattern, 1) * 100 + find_reflection(list(zip(*pattern)), 1)) for pattern in patterns])}")
