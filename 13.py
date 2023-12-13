def clean_pattern(pattern):
    return [line for line in pattern.split("\n")]


def find_reflection(pattern):
    for i in range(1, len(pattern)):
        left = pattern[:i]
        right = pattern[i:]
        smallest = min(len(left), len(right))
        left = left[-smallest:]
        right = right[:smallest][::-1]
        if left == right:
            return i
    return 0


with open("inputs/13.txt") as f:
    raw = f.read().split("\n\n")
    patterns = list(map(clean_pattern, raw))

total = []
for pattern in patterns:
    vertical = ["".join(i[::-1]) for i in zip(*pattern)]
    total.append((find_reflection(pattern) * 100 + find_reflection(vertical)))

print(sum(total))



    #
    # for row in patterns[1]:
    #     print(row)
    #
    # print()
    #
    #
    # # for row in patterns[1][::-1]:
    # #     print(row)
    # #
    # # print()
    #
    # for row in ["".join(i[::-1]) for i in zip(*patterns[1])]:
    #     print(row)
    # for pattern in patterns:
    #     print(len(pattern))
