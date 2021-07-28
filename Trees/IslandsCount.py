# Given a boolean 2D matrix, find the number of islands.
# A group of connected 1s forms an island. For example, the below matrix contains 5 islands

## REVISE ##
'''
Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1} 
Output : 5
'''
class Graph:
    # Using DFS
    def __init__(self, row, col, graph):
        self.row = row
        self.col = col
        self.graph = graph

    def DFS(self,i,j):
        if i < 0 or i >= len(self.graph) or j < 0 or j >= len(self.graph[0]) or self.graph[i][j] != 1:
            return

        self.graph[i][j] = -1

        self.DFS(i - 1, j - 1)
        self.DFS(i - 1, j)
        self.DFS(i - 1, j + 1)
        self.DFS(i, j - 1)
        self.DFS(i, j + 1)
        self.DFS(i + 1, j - 1)
        self.DFS(i + 1, j)
        self.DFS(i + 1, j + 1)

    def countIsland(self):
        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if self.graph[i][j] == 1:
                    self.DFS(i, j)
                    count += 1

        return count


graph = [
    [1, 1, 0, 0, 0],
    [0, 1, 0, 0, 1],
    [1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]

row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print("Number of islands is:", g.countIsland())
