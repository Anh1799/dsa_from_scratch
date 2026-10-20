
from collections import deque

class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj:
            self.adj[vertex] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)

        if v not in self.adj[u]:
            self.adj[u].append(v)

        if u not in self.adj[v]:
            self.adj[v].append(u)

    def bfs(self, start):
        if start not in self.adj:
            raise KeyError(start)

        visited = {start}
        queue = deque([start])
        result = []

        while queue:
            vertex = queue.popleft()
            result.append(vertex)

            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return result

    def dfs(self, start):
        if start not in self.adj:
            raise KeyError(start)

        visited = set()
        result = []

        def visit(vertex):
            visited.add(vertex)
            result.append(vertex)

            for neighbor in self.adj[vertex]:
                if neighbor not in visited:
                    visit(neighbor)

        visit(start)
        return result


graph = Graph()

graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("C", "E")

print("BFS:", graph.bfs("A"))
print("DFS:", graph.dfs("A"))
