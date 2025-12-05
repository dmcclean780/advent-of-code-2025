total = 0

with open('day4/test.txt', 'r') as f:
    rows = [line.strip() for line in f]

row2 = rows.copy()
row2 = [list(row) for row in row2]

for i in range(len(rows)):
    for j in range(len(rows[i])):
        count = 0
        if rows[i][j] == '.':
            continue
        if i != 0:
            if rows[i-1][j] == '@':
                count += 1
            if j != 0:
                if rows[i-1][j-1] == '@':
                    count += 1
            if j < len(rows[i])-1:
                if rows[i-1][j+1] == '@':
                    count += 1   
        if i < len(rows)-1:
            if rows[i+1][j] == '@':
                count += 1
            if j != 0:
                if rows[i+1][j-1] == '@':
                    count += 1
            
            if j < len(rows[i])-1:
                if rows[i+1][j+1] == '@':
                    count += 1     
        if j != 0:
            if rows[i][j-1] == '@':
                count += 1
        if j < len(rows[i])-1:
            if rows[i][j+1] == '@':
                count += 1
        if count < 4:
            print(i, j)
            row2[i][j] = 'x'
            total += 1

for row in row2:
    print(''.join(row))


print(total)
