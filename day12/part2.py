memo = {}

def countPaths(graph, node, end, B, C, visited):
    seen_B, seen_C = visited

    # Update visited flags for current node
    if node == B:
        seen_B = True
    if node == C:
        seen_C = True

    # If we reached end, check if both B and C have been visited
    if node == end:
        return int(seen_B and seen_C)  # 1 if both visited, 0 otherwise

    # Memoization key: (node, seen_B, seen_C)
    key = (node, seen_B, seen_C)
    if key in memo:
        return memo[key]

    total_paths = 0
    for neighbor in graph.get(node, []):
        total_paths += countPaths(graph, neighbor, end, B, C, (seen_B, seen_C))

    memo[key] = total_paths
    return total_paths

with open('day11/input.txt', 'r') as f:
    lines = [line.strip().split() for line in f]

graph = {}
start = "svr"
B = "dac"
C = "fft"
end = "out"

for line in lines:
    node = line[0].replace(':', '')
    edges = line[1:]
    graph[node] = edges
graph[end] = []

print("Start:", graph[start])
print("End:", graph[end])
print("Graph:", graph)
total_paths = countPaths(graph, start, end, B, C, (False, False))
print("Valid paths including 'dac' and 'fft':", total_paths)

