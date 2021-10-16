# Leetcode 323
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        
        adjList = [[] for _ in range(n)]
        visited = [-1]*n
        for (src,des) in edges:
            adjList[src].append(des)
            adjList[des].append(src)
        
        def dfs(source):
            visited[source] = 1
            for neighbor in adjList[source]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    dfs(neighbor)
        
        def bfs(source):
            visited[source] = 1
            q = collections.deque([source])
            while len(q) != 0:
                node = q.popleft()
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        q.append(neighbor)
                        
        components = 0
        for v in range(n):
            if visited[v] == -1:
                components += 1
                bfs(v)
        
        return components
            
 # For both DFS and BFS       
 # Time complexity = O( V + E ) , V = push/pop of V vertices, E = looking at degrees/edges of each vertex
 # Space complexity = call stack = O(V)
