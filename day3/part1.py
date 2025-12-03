total = 0

with open('day3/input.txt', 'r') as f:
    banks = [line.strip() for line in f]

banks = [list(map(int, s)) for s in banks]

for bank in banks:
    tens = bank[:-1]
    largest = str(max(tens))
    index = tens.index(int(largest)) + 1
    ones = bank[index:]
    largest += str(max(ones))
    total += int(largest)


print(total)
