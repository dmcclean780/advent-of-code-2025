import pulp

with open('day10/input.txt', 'r') as f:
    lines = [line.strip().split() for line in f]

total = 0
for line in lines:
    print(line)
    goal = [int(x) for x in line[-1].replace('{', '').replace('}', '').split(',')]


    buttons = [tuple(map(int, b.strip('()').split(','))) for b in line[1:-1]]

    binary_buttons = []
    for positions in buttons:
        button_state = [1 if i in positions else 0 for i in range(len(goal))]
        binary_buttons.append(button_state)

    n = len(buttons)
    m = len(goal)

    # Convert buttons to binary representation
    binary_buttons = []
    for pos in buttons:
        binary_buttons.append([1 if i in pos else 0 for i in range(m)])

    # 1. Define ILP problem
    prob = pulp.LpProblem("MinimalButtonPresses", pulp.LpMinimize)

    # 2. Define integer variables (number of presses per button)
    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat='Integer') for i in range(n)]

    # 3. Objective: minimize total presses
    prob += pulp.lpSum(x)

    # 4. Constraints: each lamp must reach its target count
    for i in range(m):
        prob += pulp.lpSum(binary_buttons[j][i] * x[j] for j in range(n)) == goal[i]

    # 5. Solve the ILP
    prob.solve()

    # 6. Print results
    if pulp.LpStatus[prob.status] == 'Optimal':
        presses = [int(x[i].varValue) for i in range(n)]
        total += sum(presses)
    else:
        print("No solution found.")
            
print("Total:", total)

