"""
A graph is a valid tree is there are no cycles and all the components are connected.
To check if there are cycles are not, we check if there is cross edge (BFS)or back egde(DFS) in the graph
To check if there is a cross egde: check if a node (which is not my parent) has been visited previously or not.
In a connected graph if a node X has been visited by A and also by B, then there is a cycle formed with X A B
"""
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        adjList = [[] for _ in range(n)]
        visited = [-1] * n
        parent = [-1] * n
        
        for (src,des) in edges:
            adjList[src].append(des)
            adjList[des].append(src)
            
        def bfs(source):
            visited[source] = 1
            q = collections.deque([source])
            while len(q) != 0:
                node = q.popleft()
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        parent[neighbor] = node
                        q.append(neighbor)
                    else:
                        if parent[node] != neighbor:
                            return True # cross edge exists
            return False
        
        def dfs(source):
            visited[source] = 1
            for neighbor in adjList[source]:
                if visited[neighbor] == -1:
                    visited[neighbor] = 1
                    parent[neighbor] = source
                    if dfs(neighbor):
                        return True
                else:
                    if parent[source] != neighbor:
                        return True # the neighbor has been visted 
                                    # and is not node's parent, hence cycle exists
            return False
       
        components = 0
        for v in range(n):
            if visited[v] == -1:
                components += 1
                if components > 1:
                    return False
                if dfs(v):
                    return False
        return True
                
                
