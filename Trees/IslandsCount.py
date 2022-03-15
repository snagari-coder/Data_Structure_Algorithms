# Leetcode 200
# BFS and DFS together, see comments

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        numOfIslands = 0
        
        
        def dfs(r,c):
            visited.add((r,c))
            q = collections.deque()
            q.append((r,c))
            while q:
                row,col = q.popleft() # if popleft is changed to pop, it becomes dfs in 
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    r, c = row + dr,col + dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visited and grid[r][c] == '1':
                        q.append((r,c))
                        visited.add((r,c))
                
            
        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    
                    numOfIslands += 1
        return numOfIslands

# Time = O(M x N)
# Space = O(min(M,N))

###################################################################################################################################################
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
