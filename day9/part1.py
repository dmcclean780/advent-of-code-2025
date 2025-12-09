with open('day9/input.txt', 'r') as f:
    lines = [line.strip().split(',') for line in f]

max_area = 0
for line in lines:
    for line2 in lines:
        x = abs(int(line[0]) - int(line2[0]) + 1)
        y = abs(int(line[1]) - int(line2[1]) + 1)
        area = x * y
        print(line, line2, x, y, area)
        if area > max_area:
            max_area = area

print(max_area)