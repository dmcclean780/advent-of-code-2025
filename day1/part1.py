value = 50
total_of_0 = 0

with open('day1/input.txt', 'r') as f:
    lines = [line.strip() for line in f]
for line in lines:
    direction = +1 if line[0] == 'R' else -1
    steps = int(line[1:])
    delta = direction * steps

    value = (value + delta) % 100
    if value == 0:
        total_of_0 += 1

print(f"Total of 0s encountered: {total_of_0}")

