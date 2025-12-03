total = 0

with open('day3/input.txt', 'r') as f:
    banks = [line.strip() for line in f]

banks = [list(map(int, s)) for s in banks]

for bank in banks:
    largest = ''
    removed_indexes = 0
    for i in range(1, 13):
        need = 13 - i
        end = len(bank) - need + 1
        slice = bank[:end]
        m = max(slice)
        index = slice.index(m)+1
        largest += str(m)
        bank = bank[index:]
    total += int(largest)


print(total)
