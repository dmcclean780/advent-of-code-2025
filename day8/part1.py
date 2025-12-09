import heapq

total = 0

with open('day8/input.txt', 'r') as f:
    lines = [line.strip().split(',') for line in f]

comnections = 1000
circuits = []

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

for _ in range(comnections):
    dist, a, b = heapq.heappop(heap)

    new_circuit = set([a, b])
    for circuit in circuits:
        if a in circuit or b in circuit:
            new_circuit.update(circuit)
            circuits.remove(circuit)

    circuits.append(new_circuit)
    distances[a][b] = 0
    distances[b][a] = 0
print(circuits)

sizes = []
for circuit in circuits:
    sizes.append(len(circuit))

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
        

        



