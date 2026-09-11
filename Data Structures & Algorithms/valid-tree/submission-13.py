class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visit = set()

        def dfs(curr, prev):
            if curr in visit:
                return False
            visit.add(curr)
            for neigh in adj[curr]:
                if neigh == prev:
                    continue
                if not dfs(neigh, curr):
                    return False
            visit.remove(curr)
            return True

        for i in range(n):
            if not dfs(i, None):
                return False

        return True

