total = 0

with open('day5/input.txt', 'r') as f:
    lines = [line.strip() for line in f]

ranges = []
current = 'ranges'
for line in lines:
    if line == '':
        break
    if current == 'ranges':
        parts = line.split('-')
        new_start, new_end = int(parts[0]), int(parts[1])
        merged = []
        placed = False
        for (start, end) in ranges:
            if end+1 < new_start:
                merged.append((start, end))
            elif new_end + 1 < start:
                if not placed:
                    merged.append((new_start, new_end))
                    placed = True
                merged.append((start, end))
            else:
                new_start = min(start, new_start)
                new_end = max(end, new_end)

        if not placed:
            merged.append((new_start, new_end))

        ranges = merged

print(ranges)

for start, end in ranges:
    total += end - start + 1

print(total)