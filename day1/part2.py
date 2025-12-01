value = 50
total_of_0 = 0

with open('day1/input.txt', 'r') as f:
    lines = [line.strip() for line in f]
for line in lines:
    direction = +1 if line[0] == 'R' else -1
    steps = int(line[1:])
    delta = direction * steps

    SIZE = 100
    start = value

    if direction > 0:
        # moving right
        end = start + steps
        wraps = end // SIZE - start // SIZE
        total_of_0 += wraps
        value = end % SIZE
    else:
        # moving left
        end = start - steps
        # shift start by -1 to handle left wrapping correctly
        wraps = (start - 1) // SIZE - (end - 1) // SIZE
        total_of_0 += wraps
        value = end % SIZE

print(f"Total of 0s encountered: {total_of_0}")

