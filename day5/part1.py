total = 0

with open('day5/input.txt', 'r') as f:
    lines = [line.strip() for line in f]

ranges = []
values = []
current = 'ranges'
for line in lines:
    if line == '':
        current = 'values'
        continue
    if current == 'ranges':
        parts = line.split('-')
        ranges.append((int(parts[0]), int(parts[1])))
    else:
        values.append(int(line))

print(ranges)
print(values)

for value in values:
    for r in ranges:
        if r[0] <= value <= r[1]:
            total += 1
            break

print(total)