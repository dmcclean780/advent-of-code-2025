import heapq

total = 0

with open('day8/input.txt', 'r') as f:
    lines = [line.strip().split(',') for line in f]

comnections = 1000
circuits = [set([0])]

distances = []
for source in lines:
    connection_distances = []
    for dest in lines:
        distance = 0
        distance += (int(source[0]) - int(dest[0])) ** 2
        distance += (int(source[1]) - int(dest[1])) ** 2
        distance += (int(source[2]) - int(dest[2])) ** 2
        connection_distances.append(distance**0.5)
    distances.append(connection_distances)

heap = []
n = len(distances)

for i in range(n):
    for j in range(i+1, n):
        if distances[i][j] != 0:
            heapq.heappush(heap, (distances[i][j], i, j))

last_a, last_b = -1, -1
while len(circuits) > 1 or len(circuits[0]) < len(lines):
    dist, a, b = heapq.heappop(heap)
    last_a, last_b = a, b
    to_merge = []
    new_circuit = set([a, b])
    for circuit in circuits:
        if a in circuit or b in circuit:
            to_merge.append(circuit)
    
    for circuit in to_merge:
        new_circuit.update(circuit)
        circuits.remove(circuit)

    circuits.append(new_circuit)
    distances[a][b] = 0
    distances[b][a] = 0
    print(circuits)

print(int(lines[last_a][0]) * int(lines[last_b][0]))
        

        



