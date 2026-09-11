class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            rootX = find(x)
            rootY = find(y)

            if rootX == rootY:
                return 0
            if rank[rootY] > rank[rootX]:
                parent[rootX] = rootY
                rank[rootY] += rank[rootX]
            else:
                parent[rootY] = rootX
                rank[rootX] += rank[rootY]
        
            return 1

        res = n
        for x,y in edges:
            res -= union(x,y)
        return res
            