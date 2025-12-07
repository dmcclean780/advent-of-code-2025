total = 0

with open('day6/test.txt', 'r') as f:
    lines = [line.strip().split() for line in f]

print(lines)
columns = list(zip(*lines))
print(columns)

for col in columns:
    op = col[-1]
    the_sum = int(col[0])
    for val in col[1:-1]:
        val = int(val)
        if op == '+':
            the_sum += val
        elif op == '*':
            the_sum *= val
    total += the_sum

print(total)

