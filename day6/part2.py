total = 0

with open('day6/input.txt', 'r') as f:
    lines = [line.rstrip('\n') for line in f]

max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len) for line in lines]
split_indices = [i for i in range(max_len) if all(line[i] == ' ' for line in lines)]

def split_at_indices(line, indices):
    parts = []
    last_index = 0
    for i in indices:
        parts.append(line[last_index:i])
        last_index = i + 1
    parts.append(line[last_index:])
    return parts

split_lines = [split_at_indices(line, split_indices) for line in lines]

final_cols = list(zip(*split_lines))

for col in final_cols:
    max_len = max(len(item.strip()) for item in col)
    result = []
    for i in range(max_len):
        new = ''
        for item in col[:-1]:
            if len(item) >= i and item[i] != ' ':
                new += item[i]
        result.append(new.strip())
    result.append(col[-1].strip())
    final_cols[final_cols.index(col)] = tuple(result)

print(final_cols)

for col in final_cols:
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



