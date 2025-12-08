total = 0

with open('day7/input.txt', 'r') as f:
    lines = [list(line.strip()) for line in f]

laser_pos = [lines[0].index('S')]

for line in lines[1:]:
    next_laser_pos = []
    for pos in laser_pos:
        if line[pos] == '.':
            line[pos] = '|'
            next_laser_pos.append(pos)
        elif line[pos] == '^':
            next_laser_pos.append(pos - 1)
            next_laser_pos.append(pos + 1)
            line[pos+1] = '|'
            line[pos-1] = '|'
            total += 1
    laser_pos = next_laser_pos
print(total)

