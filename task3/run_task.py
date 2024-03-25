from Genome_Assembly_algorithms.EulerCycleFinder import EulerCycleFinder

vertexes_count, edges_count = map(int, input().split())  # a.k.a. n, m
edges = []
for _ in range(edges_count):
    v, to = map(int, input().split())
    edges.append([v, to])
print(*edges)
cycle = EulerCycleFinder(vertexes_count, edges_count, edges).get_cycle()
print(*cycle)

