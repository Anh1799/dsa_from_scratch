
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

    def remove_edge(self, u, v):
        if u not in self.adj or v not in self.adj:
            return False

        if v not in self.adj[u]:
            return False

        self.adj[u].remove(v)

        if u != v:
            self.adj[v].remove(u)

        return True

    def bfs(self, start):
        if start not in self.adj:
            raise KeyError(start)

        visited = {start}
        queue = deque([start])
        result = []

        while queue:
            current = queue.popleft()
            result.append(current)

            for neighbor in self.adj[current]:
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

    def has_path(self, start, end):
        if start not in self.adj or end not in self.adj:
            return False

        visited = {start}
        queue = deque([start])

        while queue:
            current = queue.popleft()

            if current == end:
                return True

            for neighbor in self.adj[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return False

    def shortest_path(self, start, end):
        if start not in self.adj or end not in self.adj:
            return []

        queue = deque([start])
        parent = {start: None}

        while queue:
            current = queue.popleft()

            if current == end:
                break

            for neighbor in self.adj[current]:
                if neighbor not in parent:
                    parent[neighbor] = current
                    queue.append(neighbor)

        if end not in parent:
            return []

        path = []
        current = end

        while current is not None:
            path.append(current)
            current = parent[current]

        path.reverse()
        return path


# Example usage
if __name__ == "__main__":
    graph = Graph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "E")

    print("BFS:", graph.bfs("A"))
    print("DFS:", graph.dfs("A"))

    print("Path A to D?", graph.has_path("A", "D"))
    print("Shortest:", graph.shortest_path("A", "D"))

    graph.remove_edge("B", "D")

    print("After removing B-D:")
    print("Path A to D?", graph.has_path("A", "D"))
    print("Shortest:", graph.shortest_path("A", "D"))
