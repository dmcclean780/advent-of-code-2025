import re

invalid_re = re.compile(r'^(\d+)\1$')

with open('day2/input.txt', 'r') as f:
    line = f.readline().strip()   # read the line, remove newline
    values = line.split(",")

total = 0
for v in values:
    bounds = v.split("-")
    total += sum(n 
               for n in range(int(bounds[0]), int(bounds[1]) + 1) 
               if invalid_re.fullmatch(str(n)))
print(total)