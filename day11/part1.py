memo = {}
def countPaths(graph, node, end):
    if node == end:
        return 1
    if node not in graph or not graph[node]:
        return 0
    if node in memo:
        return memo[node]

    total_paths = 0
    for neighbor in graph[node]:
        total_paths += countPaths(graph, neighbor, end)
    
    memo[node] = total_paths
    return total_paths
    

with open('day11/input.txt', 'r') as f:
    lines = [line.strip().split() for line in f]

graph = {}
start = "you"
end = "out"

for line in lines:
    node = line[0].replace(':', '')
    edges = line[1:]
    graph[node] = edges
graph[end] = []

print("Start:", graph[start])
print("End:", graph[end])
print("Graph:", graph)
total_paths = countPaths(graph, start, end)
print("Total paths from", start, "to", end, ":", total_paths)

