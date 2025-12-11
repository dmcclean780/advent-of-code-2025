with open('day10/input.txt', 'r') as f:
    lines = [line.strip().split() for line in f]
total = 0
for line in lines:
    print(line)
    goal = line[0].replace('[', '').replace(']', '')
    target_lamps = {i for i, char in enumerate(goal) if char == '#'}

    buttons = [tuple(map(int, b.strip('()').split(','))) for b in line[1:-1]]

    binary_buttons = []
    for positions in buttons:
        value = 0
        for pos in positions: 
            value |= (1 << pos)
        binary_buttons.append(value)

    binary_goal = 0
    for i in target_lamps:
        binary_goal |= (1 << i)

    found_solution = False
    n = len(binary_buttons)
    while not found_solution:
        for k in range(1, n + 1):
            for subset in range(1, 1 << n):
                if bin(subset).count('1') != k:
                    continue  # skip subsets not of size k

                state = 0
                for j in range(n):
                    if (subset >> j) & 1:
                        state ^= binary_buttons[j]

                if state == binary_goal:
                    print(f"presses: {k}")
                    total += k
                    found_solution = True
                    break
            if found_solution:
                break
            
print("Total:", total)

