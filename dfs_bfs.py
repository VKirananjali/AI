from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {vertex: [] for vertex in range(vertices)}

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True

    while queue:
        current = queue.popleft()
        print(current, end=' ')

        for neighbor in graph[current]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def dfs(graph, start, visited):
    if not visited[start]:
        print(start, end=' ')
        visited[start] = True

        for neighbor in graph[start]:
            dfs(graph, neighbor, visited)

if __name__ == "__main__":
    graph = Graph(5)

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)

    print("BFS starting from vertex 0:")
    bfs(graph.graph, 0)
    print("\nDFS starting from vertex 0:")
    dfs(graph.graph, 0, [False] * graph.vertices)
