def get_next_sequence(sequence):
    nums = []
    last_num = sequence[-1]
    while any(sequence):
        new_sequence = []
        for i in range(len(sequence) - 1):
            new_sequence.append(sequence[i + 1] - sequence[i])
        nums.append(new_sequence[-1])
        sequence = new_sequence
    return last_num + sum(nums)


with open("inputs/09.txt") as f:
    sequences = [list(map(int, (k.split()))) for k in f.readlines()]

    print(sum(list(map(get_next_sequence, sequences))))
    print(sum(list(map(get_next_sequence, [i[::-1] for i in sequences]))))
