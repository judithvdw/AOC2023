def check_calibration_value(value, part2=False):
    numbers = "1233456789"
    valid_digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    indices = {}
    for num in numbers:
        if num in value:
            indices[value.index(num)] = num
            indices[value.rindex(num)] = num
    if part2:
        for digit in valid_digits:
            if digit in value:
                indices[value.index(digit)] = valid_digits[digit]
                indices[value.rindex(digit)] = valid_digits[digit]
    return int(indices[min(indices)] + indices[max(indices)])


with open("inputs/01.txt") as f:
    codes = [i.strip() for i in f.readlines()]

print(f"Part 1: {sum([check_calibration_value(code) for code in codes])}")
print(f"Part 2: {sum([check_calibration_value(code, part2=True) for code in codes])}")