class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        par = [i for i in range(n)]
        rank = [0] * n
        
        def find(curr):
            if par[curr] != curr:
                par[curr] = find(par[curr])
            return par[curr]

        def union(x,y):
            p, q = find(x), find(y)
            if p == q:
                return False
            if rank[p] > rank[q]:
                par[q] = p
            elif rank[p] < rank[q]:
                par[p] = q
            else:
                par[q] = p
                rank[p] += 1
            return True

        for u,v in edges:
            if not union(u,v):
                return False

        return True

