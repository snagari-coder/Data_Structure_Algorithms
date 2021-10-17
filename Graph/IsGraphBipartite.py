'''
Leetcode 785
A tree is a bipartite
A graph cycle with odd vertices/node is not bipartite. i.e 
In a tree, if there is cross edge, and visited neighbor is at the same level of node, then 
it is graph cycle with odd vertices, not bipartite

If the cross edge is in the adjacent level, then the grpah cycle has even vertices --> is bipartite
'''
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        adjList = graph
        n = len(adjList)
        visited = [-1] * n
        parent = [-1] * n
        distance = [-1] * n
        color = [-1] * n
        
        def bfs(source):
            visited[source] = 1
            distance[source] = 0
            q = collections.deque([source])
            while len(q) != 0:
                node = q.popleft()
                for neighbor in adjList[node]:
                    if visited[neighbor] == -1:
                        visited[neighbor] = 1
                        parent[neighbor] = node
                        distance[neighbor] = distance[node] + 1
                        q.append(neighbor)
                    else:
                        if parent[node] != neighbor: # cycle found
                            if distance[neighbor] == distance[node]: # odd vertices in cycle
                                return False 
            return True
        
        def dfs(source):
            visited[source] = 1
            if parent[source] == -1:
                color[source] = 0
            else: 
                color[source] = 1 - color[parent[source]]
                
            for neighbor in adjList[source]:
                if visited[source] == -1:
                    
                    parent[neighbor] = source
                    if dfs(neighbor) == False:
                        return False
                else:
                    if color[source] == color[neighbor]:
                        return False
            print(color)
            return True
        
        for v in range(n):
            if visited[v] == -1:
                #color[v] = 0
                if not bfs(v):
                    return False # even if one odd cycle was found, not bipartite
        return True # all connected components are bipartite, hence bipartite
