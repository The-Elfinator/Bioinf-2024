class EulerCycleFinder:

    def __init__(self, vertexes_count: int, edges_count: int, edges: list[list[int, int]]):
        self.vertex_count: int = vertexes_count
        self.edges_count: int = edges_count
        self.graph: list[list[int]] = [[] for _ in range(vertexes_count)]
        for edge in edges:
            v, to = edge
            v -= 1
            to -= 1
            self.graph[v].append(to)

    def get_cycle(self) -> list[int]:
        ans: list[int] = []
        stack: list[int] = [0]
        while len(stack) != 0:
            v = stack[-1]
            neighbours = self.graph[v]
            if len(neighbours) == 0:
                ans.append(v)
                stack.pop()
            else:
                to = neighbours.pop()
                stack.append(to)
        return list(map(lambda x: x+1, ans[::-1]))
