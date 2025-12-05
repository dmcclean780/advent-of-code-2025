total = 0

with open('day4/input.txt', 'r') as f:
    rows = [line.strip() for line in f]

rows = [list(row) for row in rows]
row2 = rows.copy()
row2 = [list(row) for row in row2]

movable = True
while movable:
    movable = False 
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
                rows[i][j] = '.'
                total += 1
                movable = True
                row2[i][j] = 'x'
for row in row2:
    print(''.join(row))


print(total)
