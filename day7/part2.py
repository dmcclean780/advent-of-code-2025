from collections import defaultdict

total = 0
with open('day7/input.txt', 'r') as f:
    lines = [list(line.strip()) for line in f]

laser_pos = defaultdict(int)
laser_pos[lines[0].index('S')] = 1

num_rows = len(lines)

for row_idx, line in enumerate(lines[1:], start=1):
    print(line)
    next_laser_pos = defaultdict(int)
    completed_positions = set()
    for pos, count in laser_pos.items():
        if line[pos] == '.':
            if all(lines[r][pos] == '.' for r in range(row_idx, num_rows)):
                total += count
            else:
                next_laser_pos[pos] += count
        elif line[pos] == '^':
            next_laser_pos[pos - 1] += count
            next_laser_pos[pos + 1] += count
    laser_pos = next_laser_pos

print(sum(laser_pos.values()) + total)

